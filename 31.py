import random

vitorias_consecutivas = 0

while True:
    jogador_escolha = input("Escolha par ou ímpar: ").lower()
    jogador_numero = int(input("Digite um número: "))

    computador_numero = random.randint(1, 10)
    print("Número do computador:", computador_numero)

    soma = jogador_numero + computador_numero
    resultado = "par" if soma % 2 == 0 else "ímpar"

    print(f"Soma: {soma} ({resultado})")

    if resultado == jogador_escolha:
        print("Você ganhou!")
        vitorias_consecutivas += 1
    else:
        print(f"Você perdeu! Total de vitórias consecutivas: {vitorias_consecutivas}")
        break