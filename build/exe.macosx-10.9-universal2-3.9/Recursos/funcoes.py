import os
import json
from datetime import datetime


def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def inicializarBancoDeDados():
    # se o arquivo nao existir, cria um vazio
    try:
        banco = open("base.atitus", "r")
        banco.close()
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("base.atitus", "w")
        banco.close()


def lerDados():
    banco = open("base.atitus", "r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}
    return dadosDict


def escreverDados(nome, pontos):
    dadosDict = lerDados()

    data_br = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")

    # so salva se for o primeiro jogo ou se fez mais pontos que antes
    if nome in dadosDict:
        if pontos > dadosDict[nome][0]:
            dadosDict[nome] = [pontos, data_br, hora]
    else:
        dadosDict[nome] = [pontos, data_br, hora]

    banco = open("base.atitus", "w")
    banco.write(json.dumps(dadosDict))
    banco.close()


def maior_pontuador():
    dadosDict = lerDados()

    nome_maior = "Ninguem"
    maior_pontos = 0
    dataJogada = "--/--/----"
    horaJogada = "--:--:--"

    for nome in dadosDict:
        info = dadosDict[nome]
        pontos = info[0]
        if pontos > maior_pontos:
            maior_pontos = pontos
            nome_maior = nome
            dataJogada = info[1]
            horaJogada = info[2]

    return nome_maior, maior_pontos, dataJogada, horaJogada
