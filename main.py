import pygame
import random
import sys
from Recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados
from Recursos.trabalho import verificarColisao, patenteDoAstronauta

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
        tela.blit(texto, (330, 120))
        texto = fonte.render("Voce desviou de " + str(pontos) + " meteoros!", True, amarelo)
        tela.blit(texto, (360, 480))
        texto = fonte.render("Patente: " + patenteDoAstronauta(pontos), True, branco)
        tela.blit(texto, (360, 520))

        botao = pygame.draw.rect(tela, branco, (400, 580, 200, 50), border_radius=15)
        texto = fonte.render("Jogar Novamente", True, preto)
        tela.blit(texto, (415, 592))

        pygame.display.update()
        relogio.tick(60)


while True:
    pontos = jogar()
    fimDeJogo(pontos)
