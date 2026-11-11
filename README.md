# Astronauta Perdido

Jogo feito em Python com Pygame para a disciplina de Pensamento Computacional,
adaptado a partir do jogo base Iron Man do professor
(https://github.com/profmarcossantos/IronManV2).

## Desenvolvedores

| Nome completo | RA |
|---|---|
| Victor Augusto Rizzotto | 1140225 |
| Davi Migliorini Bonissoni | 1140196 |

## História do jogo

O astronauta Leo saiu da nave para consertar uma antena, mas o cabo de
segurança se rompeu e ele ficou à deriva no espaço. Agora, usando apenas
o jetpack, ele precisa sobreviver a uma chuva de meteoros que fica cada vez
mais rápida enquanto espera o resgate. Quantos meteoros você consegue desviar?

## Como jogar

1. Rode o jogo e digite seu nome no terminal.
2. Na tela de boas-vindas, clique em **Iniciar Partida**.
3. Use as **setas do teclado** para mover o astronauta.
4. Cada meteoro desviado vale 1 ponto. Se encostar em um, é fim de jogo.
5. Para fechar o jogo, use o **X** da janela.

## Tecnologias utilizadas

- Python 3
- Pygame (janela, imagens, sons e teclado)
- cx_Freeze (geração do executável)
- JSON (arquivo `base.atitus` que guarda nome, pontos, data e hora)
- Git e GitHub (controle de versão)

## Estrutura

```
main.py              -> arquivo principal do jogo
setup.py             -> gera o executável (python setup.py build)
bases/               -> imagens, ícone, música e sons
Recursos/funcoes.py  -> funções do banco de dados
Recursos/trabalho.py -> funções novas: verificarColisao e patenteDoAstronauta
build/               -> executável gerado
```

## ▶Como executar

```
pip install pygame
python main.py
```

Para gerar o executável:

```
pip install cx_freeze
python setup.py build
```
