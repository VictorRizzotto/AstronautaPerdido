import pygame
import random
import sys
import os
from Recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador
from Recursos.trabalho import verificarColisao, patenteDoAstronauta

# quando o jogo roda pelo executavel, entra na pasta do executavel
# para conseguir achar a pasta bases/
if hasattr(sys, "frozen"):
    os.chdir(os.path.dirname(sys.executable))

limpar_tela()
inicializarBancoDeDados()
pygame.init()

while True:
    nome = input("Digite seu nome de astronauta: ")
    if len(nome) > 0:
        break
    else:
        print("Nome Invalido!")

tamanho = (1000, 700)
pygame.display.set_caption("Astronauta Perdido")
icone = pygame.image.load("bases/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

branco = (255, 255, 255)
preto = (0, 0, 0)
amarelo = (255, 220, 80)

fundo = pygame.image.load("bases/fundo.png")
fundoFim = pygame.image.load("bases/fundoFim.png")
fundoInicio = pygame.image.load("bases/fundoInicio.png")

astronauta = pygame.image.load("bases/astronauta.png")
astronauta = pygame.transform.scale(astronauta, (80, 80))
meteoro = pygame.image.load("bases/meteoro.png")
meteoro = pygame.transform.scale(meteoro, (70, 70))

somMeteoro = pygame.mixer.Sound("bases/meteoro.wav")
somExplosao = pygame.mixer.Sound("bases/explosao.wav")
pygame.mixer.music.load("bases/musica.wav")

fonte = pygame.font.SysFont("arial", 24)
fonteGrande = pygame.font.SysFont("arial", 60, bold=True)


def sair():
    pygame.quit()
    sys.exit()


def jogar():
    fundoX1 = 0
    fundoX2 = 1000
    astronautaX = 100
    astronautaY = 300
    movimentoX = 0
    movimentoY = 0
    velocidadeAstronauta = 6
    meteoroX = 1000
    meteoroY = random.randint(0, 630)
    velocidadeMeteoro = 5
    pontos = 0

    pygame.mixer.music.play(-1)
    pygame.mixer.Sound.play(somMeteoro)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movimentoY = -velocidadeAstronauta
                elif evento.key == pygame.K_DOWN:
                    movimentoY = velocidadeAstronauta
                elif evento.key == pygame.K_LEFT:
                    movimentoX = -velocidadeAstronauta
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = velocidadeAstronauta
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    movimentoY = 0
                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimentoX = 0

        # move o astronauta e nao deixa sair da tela
        astronautaX = astronautaX + movimentoX
        astronautaY = astronautaY + movimentoY
        if astronautaX < 0:
            astronautaX = 0
        elif astronautaX > 920:
            astronautaX = 920
        if astronautaY < 0:
            astronautaY = 0
        elif astronautaY > 620:
            astronautaY = 620

        # move o meteoro, quando ele sai da tela o jogador ganha 1 ponto
        meteoroX = meteoroX - velocidadeMeteoro
        if meteoroX < -70:
            pygame.mixer.Sound.play(somMeteoro)
            meteoroX = 1000
            meteoroY = random.randint(0, 630)
            pontos = pontos + 1
            velocidadeMeteoro = velocidadeMeteoro + 1

        # fundo andando
        fundoX1 = fundoX1 - 1
        fundoX2 = fundoX2 - 1
        if fundoX1 <= -1000:
            fundoX1 = 1000
        if fundoX2 <= -1000:
            fundoX2 = 1000

        tela.fill(preto)
        tela.blit(fundo, (fundoX1, 0))
        tela.blit(fundo, (fundoX2, 0))
        tela.blit(astronauta, (astronautaX, astronautaY))
        tela.blit(meteoro, (meteoroX, meteoroY))
        texto = fonte.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (860, 15))

        # colisao usando a funcao do arquivo trabalho.py
        if verificarColisao(astronautaX, astronautaY, 80, 80, meteoroX, meteoroY, 70, 70, 15):
            escreverDados(nome, pontos)
            return pontos

        pygame.display.update()
        relogio.tick(60)


def fimDeJogo(pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(somExplosao)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair()
            elif evento.type == pygame.MOUSEBUTTONUP:
                if botao.collidepoint(evento.pos):
                    return

        tela.blit(fundoFim, (0, 0))
        texto = fonteGrande.render("GAME OVER", True, branco)
        tela.blit(texto, (500 - texto.get_width() / 2, 120))
        texto = fonte.render("Voce desviou de " + str(pontos) + " meteoros!", True, amarelo)
        tela.blit(texto, (360, 480))
        texto = fonte.render("Patente: " + patenteDoAstronauta(pontos), True, branco)
        tela.blit(texto, (360, 520))

        botao = pygame.draw.rect(tela, branco, (400, 580, 200, 50), border_radius=15)
        texto = fonte.render("Continuar", True, preto)
        tela.blit(texto, (500 - texto.get_width() / 2, 592))

        pygame.display.update()
        relogio.tick(60)


def boasVindas():
    # busca o melhor jogador salvo no banco
    nome_maior, maior_pontos, dataJogada, horaJogada = maior_pontuador()

    larguraBotao = 220
    alturaBotao = 60
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    larguraBotao = 210
                    alturaBotao = 55
            elif evento.type == pygame.MOUSEBUTTONUP:
                larguraBotao = 220
                alturaBotao = 60
                if botao.collidepoint(evento.pos):
                    return

        tela.blit(fundoInicio, (0, 0))

        texto = fonteGrande.render("ASTRONAUTA PERDIDO", True, amarelo)
        tela.blit(texto, (500 - texto.get_width() / 2, 50))
        texto = fonte.render("Bem-vindo(a), " + nome + "!", True, branco)
        tela.blit(texto, (60, 160))

        # explicacao rapida da mecanica
        texto = fonte.render("Como jogar:", True, amarelo)
        tela.blit(texto, (60, 220))
        texto = fonte.render("- Use as SETAS do teclado para mover o astronauta.", True, branco)
        tela.blit(texto, (60, 260))
        texto = fonte.render("- Desvie dos meteoros que vem da direita.", True, branco)
        tela.blit(texto, (60, 295))
        texto = fonte.render("- Cada meteoro que passar vale 1 ponto. Eles ficam cada vez mais rapidos!", True, branco)
        tela.blit(texto, (60, 330))
        texto = fonte.render("- Se encostar em um meteoro, e fim de jogo.", True, branco)
        tela.blit(texto, (60, 365))

        # melhor jogador
        texto = fonte.render("Recorde: " + nome_maior + " - " + str(maior_pontos) + " pontos", True, amarelo)
        tela.blit(texto, (60, 425))
        texto = fonte.render("Data: " + dataJogada + "   Hora: " + horaJogada, True, amarelo)
        tela.blit(texto, (60, 460))

        # unico botao: iniciar partida (para fechar usa o X da janela)
        botaoX = 500 - larguraBotao / 2
        botaoY = 560 - alturaBotao / 2
        botao = pygame.draw.rect(tela, branco, (botaoX, botaoY, larguraBotao, alturaBotao), border_radius=15)
        texto = fonte.render("Iniciar Partida", True, preto)
        tela.blit(texto, (500 - texto.get_width() / 2, 560 - texto.get_height() / 2))

        pygame.display.update()
        relogio.tick(60)


while True:
    boasVindas()
    pontos = jogar()
    fimDeJogo(pontos)
