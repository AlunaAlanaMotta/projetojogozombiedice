"""
Aluna: ALANA MOTTA DA CRUZ
CURSO: GESTÃO DE TECNOLOGIA DA INFORMAÇÃO
DISCIPLINA: RACIOCÍNIO COMPUTACIONAL
PROFESSOR-TUTOR: GALBAS MILLEO FILHO
"""
#importando bibliotecas

import random
from time import sleep

#definindo uma função para reutilizar deixando o a execução mais bonita


def formatacao(txt):
    print('\033[36m-=\033[m' * 20)
    print(txt)
    print('\033[36m-=\033[m' * 20)
    sleep(1)


#apresentação inicial do jogo

formatacao(f'\033[31m SEJA BEM VINDO AO JOGO ZOMBIE DICE\033[m')

#pedindo a quantidade de número de jogadores, deve ser mais do que um jogador, pois não é possível jogar sozinho

num_jogadores = 0
while num_jogadores < 2:
    num_jogadores = int(input('Digite o número de jogadores: '))
    if num_jogadores < 2:
        print('\033[31mTente novamente! Para jogar precisa ter no mínimo 2 jogadores!\033[m')

#Criando uma lista com a quantidade de jogadores, inserindo no nome de cada jogador

lista_jogadores = []
for c in range(0, num_jogadores):  # para cada jogador em quantidade de jogadores
    nome = input(f'Digite o nome do {c + 1}º jogador: ').upper()  # pedindo o nome dos jogadores
    lista_jogadores.append(nome)  # jogando os nomes dos jogadores na lista

#mostrando para os jogadores que o jogo irá começar

formatacao(f'\033[35mIniciando o jogo...\033[m')

#definindo as faces do dado verde,onde são 3 cérebros, 2 passos, e 1 tiro


def dado_verde():
    dadoVerde = ("C", "P", "C", "T", "P", "C")
    return dadoVerde


#defindo as faces do dado amarelo, onde são 2 cérebros, 2 tiros e 2 passos


def dado_amarelo():
    dadoAmarelo = ("T", "P", "C", "T", "P", "C")
    return dadoAmarelo


#definindo as faces do dado vermelho, onde são 3 tiros, 2 passos e 1 cérebro


def dado_vermelho():
    dadoVermelho = ("T", "P", "T", "C", "P", "T")
    return dadoVermelho


#adicionando os dados na lista copos

copodados = [dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(),
             dado_amarelo(), dado_amarelo(), dado_amarelo(), dado_amarelo(),
             dado_vermelho(), dado_vermelho(), dado_vermelho()]

dados_sorteados = []
jogador_atual = 0
tiros = 0
cerebros = 0
passos = 0
pontos = []

#para cada jogador, adicionando os pontos

for i in range(0, num_jogadores):
    pontos.append(0)

#definindo a função para sortear os dados e retornar as cores dos dados sorteados


def sortear_dados(cor_dado=()):
    for n in range(0, 3):
        num_sorteado = random.randint(0, 12)
        dado_sorteado = copodados[num_sorteado]
        if dado_sorteado == dado_verde():
            cor_dado = ('\033[32mVERDE\033[m')
        elif dado_sorteado == dado_amarelo():
            cor_dado = ('\033[33mAMARELO\033[m')
        elif dado_sorteado == dado_vermelho():
            cor_dado = ('\033[31mVERMELHO\033[m')
        sleep(1)
        print(f'Dado sorteado: {cor_dado}')
        dados_sorteados.append(dado_sorteado)
    print('\033[36m-=\033[m' * 20)
    return cor_dado


#começando a rodada para cada jogador

while True:
    print(f'\033[35mTurno do jogador atual: \033[m', f'{lista_jogadores[jogador_atual]}')
    print('\033[36m-=\033[m' * 20)

    #chamando a função para mostrar quais foram os dados sorteados e suas cores

    sortear_dados()

    #para cada dado sorteado em dados sorteados mostrando para o jogador qual face do dado ele tirou

    for dado_sorteado in dados_sorteados:
        num_facedado = random.randint(0, 5)
        if dado_sorteado[num_facedado] == "C":
            print(f'Você comeu um CÉREBRO!')
            cerebros += 1

        elif dado_sorteado[num_facedado] == "T":
            print('Você levou um TIRO!')
            tiros += 1

        else:
            print('Você tirou PASSOS! Sua vítima escapou!')
            passos += 1

    #mostrando ao jogador atual qual foi a pontuação obtida naquela rodada

    formatacao('\033[35mSCORE ATUAL\033[m')
    print(f'CÉREBROS: {cerebros}')
    print(f'TIROS: {tiros}')
    print('\033[36m-=\033[m' * 20)

    # se a quantidade de tiros for maior que 2, então o jogador atual perde a rodada e os pontos caso ele tenha algum
    # e o jogo continua com o próximo jogador

    if tiros > 2:
        print(f'{lista_jogadores[jogador_atual]} você perdeu essa rodada! levou {tiros} tiros!')
        print('\033[36m-=\033[m' * 20)
        tiros = 0
        cerebros = 0
        passos = 0
        dados_sorteados = []
        jogador_atual += 1

        #se a quantidade de jogadores da lista acabar, então volta para o primeiro jogador da lista e assim por diante

        if jogador_atual == len(lista_jogadores):
            jogador_atual = 0
        print(f'\033[35mIndo para a rodada do próximo jogador:\033[m {lista_jogadores[jogador_atual]}')

    # perguntando se o jogador atual deseja continuar ou parar a rodada

    else:
        resposta = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]

        # se a responta do jogador atual for não então o jogo vai continuar com o próximo jogador da rodada
        # e computara os pontos dos jogadores

        if resposta == 'N':
            pontos[jogador_atual] += cerebros
            jogador_atual += 1
            dados_sorteados = []
            tiros = 0
            passos = 0
            cerebros = 0

            if jogador_atual == len(lista_jogadores):
                jogador_atual = 0
    # se os pontos do jogador atual for maior ou igual a 13 então ele vence o jogo e finaliza parabenizando o jogador

    if pontos[jogador_atual] >= 13:
        print(f'\033[32mParabéns, {lista_jogadores[jogador_atual]} você VENCEU!\033[m')
        formatacao("FINALIZANDO O JOGO!")
        break

    # limpando os dados sorteados para a próxima rodada

    dados_sorteados.clear()
    print('\033[36m-=\033[m' * 20)

    #mostrando a pontuação de cada jogador

    for i in range(0, num_jogadores):
        print(f' {lista_jogadores[i]}: {pontos[i]} pontos!', end='')
    print()
    print('\033[36m-=\033[m' * 20)

















