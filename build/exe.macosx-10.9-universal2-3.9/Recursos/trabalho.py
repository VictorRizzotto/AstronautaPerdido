# Funcoes novas criadas para o trabalho


def verificarColisao(x1, y1, largura1, altura1, x2, y2, largura2, altura2, folga):
    # Verifica se dois quadrados estao encostando um no outro.
    # A folga deixa a colisao mais justa, porque as imagens tem espaco vazio nas bordas.
    if x1 + largura1 - folga > x2 and x1 + folga < x2 + largura2:
        if y1 + altura1 - folga > y2 and y1 + folga < y2 + altura2:
            return True
    return False


def patenteDoAstronauta(pontos):
    # Devolve uma patente de acordo com a quantidade de pontos
    if pontos < 5:
        return "Cadete Espacial"
    elif pontos < 10:
        return "Piloto de Foguete"
    elif pontos < 20:
        return "Capitao das Estrelas"
    else:
        return "Lenda da Galaxia"
