import random

score = 0
tentativas = 0
secretNumber = 0
playerNumber = 0
rangeMax = 1000
dificuldade = 0


#Determina a dificuldade do jogo.
def escolherDificuldade():
    global dificuldade
    global rangeMax

    dificuldade = int(input("""
    Em qual desta dificuldades você gostaria de jogar?
    1-Dificil   |   2-Médio   |   3-Facil
    """))
    
    if dificuldade == 1:
        print('Você acaba de escolher a dificuldade mais alta: Dificil.\n')
        rangeMax = 1000
        return rangeMax
    
    elif dificuldade == 2:
        print('Você acaba de escolher a dificuldade moderada: Medio.\n')
        rangeMax = 500
        return rangeMax
    
    else:
        print('Você acaba de escolher a dificuldade mais baixa: Facil.\n')
        rangeMax = 100
        return rangeMax


#Conta a quantidade de tentativas do usuario para acertar o número.
def contarTentativas():
    global tentativas
    tentativas = tentativas + 1
    
    return tentativas


#Conta a pontuação do jogador.
def contarScore():
    global score
    global tentativas
    
    if tentativas == 1:
        score = score + 10000
    elif tentativas == 2:
        score = score + 9000
    elif tentativas == 3:
        score = score + 8000
    elif tentativas == 4:
        score = score + 7000
    elif tentativas == 5:
        score = score + 6000
    elif tentativas == 6:
        score = score + 5000
    elif tentativas == 7:
        score = score + 4000
    elif tentativas == 8:
        score = score + 3000
    elif tentativas == 9:
        score = score + 2000
    else:
        score = score + 1000
    
    return score


#Função do jogo propriamente dita
def jogo():
    global playerNumber
    global secretNumber
    global rangeMax
    global score
    global tentativas

    playerNumber = 0
    tentativas = 0

    secretNumber = random.randrange(1, rangeMax)

    while playerNumber != secretNumber:
        
        playerNumber = int(input(f'Entre 1 e {rangeMax}, qual o seu palpite para o número secreto?: '))

        if  playerNumber > secretNumber:
            print(f'O número {playerNumber} é maior que o número secreto.')
            contarTentativas()

        elif playerNumber < secretNumber:
            print(f'O número {playerNumber} é menor que o número secreto.')
            contarTentativas()
    
    print('Você acertou o número secreto! Parabéns.')
    playerNumber = int(input("""
Deseja jogar novamente?
1-Sim  |  2-Não
    """))

    if playerNumber == 1:
        playerNumber = 0
        return playerNumber
    else:
        contarTentativas()
        contarScore()
        playerNumber = secretNumber
        return playerNumber


#Função principal que chama todas as outras.
def main():

    print("""
    Bem vindo ao jogo de adivinhação do número.
    Tente adivinhar no menor número de tentativas possiveis, o número secreto.
    """)

    escolherDificuldade()

    jogo()

    print(f'Esta foi a sua quantidade de tentativas: {tentativas}')
    print(f'Seu score: {score}\n')

    return print('Fim do jogo.')


main()