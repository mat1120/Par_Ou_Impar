from random import randint
vitorias = 0
while True:
    jogador = int(input("Digite um numero entre 1 e 10: "))
    escolha = str(input("Escolha entre [I/P]: ")).upper().strip()[0]
    computador = randint(1, 10)
    soma = jogador + computador
    while escolha not in "PpIi":
        escolha = str(input("Escolha entre [I/P]: ")).upper().strip()[0]
    print("Voce jogou {} e escolheu {}, o computador escolheu {}, a soma deu {}".format(jogador, escolha, computador, soma))
    print("Deu Par" if soma % 2 == 0 else "Deu Impar")
    if escolha == "P":
        if soma % 2 == 0:
            print("Voce ganhou")
            vitorias += 1
        else:
            print("Voce perdeu")
            break
    elif escolha == "I":
        if soma % 2 == 1:
            print("Voce ganhou")
            vitorias += 1
        else:
            print("Voce perdeu")
            break
    print("Vamos jogar novamente")
print("Fim de jogo,voce venceu {} vezes".format(vitorias))












