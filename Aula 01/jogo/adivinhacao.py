import random

def jogar():
    print("*" * 33)
    print("Bem vindo(a) ao jogo de Adivinhação!")
    print("*" * 33)

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um número ente 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Inválido! Digite um número ente 1 e 100")
            continue

        print(f"Você digitou {chute}")

        if (chute == numero_secreto):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

            if (chute > numero_secreto):
                print("O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            else:
                print("O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()