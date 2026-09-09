import random
print("Bem vindo ao jogo de adivinhar o número!")


while True:
    #Função que gera um numero aleatorio
    numero_secreto = random.randint(1, 100)

    print(numero_secreto)

    tentativas_restantes = 5

    print("Pense em um número de 1 a 100")
    print("Você tem 5 tentativas para adivinhar o número secreto.")

    while tentativas_restantes > 0:
        #palpite do usuario
        palpite = input("Digite seu palpite: ")

        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        # Convertendo o palpite para inteiro
        palpite = int(palpite)

        #Ver se esta no intervalo
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue

        # Descontar tentativas
        tentativas_restantes -= 1

        #verificar se o palpite é correto
        if palpite == numero_secreto:
            print(f"Você acertou! Voce ainda tinha {5 - tentativas_restantes} tentativas restantes.")
        elif palpite < numero_secreto:
            print("Seu número é maior que esse")
        else: 
            print("Seu número é menor que esse")

        print(f"Tentativas restantes: {tentativas_restantes}")

    else: 
        print("Você perdeu! o numero secreto era:", numero_secreto)
    break