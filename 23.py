soma = 0
contador = 0
maior = float('-inf')
menor = float('inf')

while True:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break

media = soma / contador

print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
[14: 50, 24 / 0
8 / 2023] Matheus: soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (digite 1000 para parar): "))
    if numero == 1000:
        break
    soma += numero
    contador += 1

print("Quantidade de números digitados:", contador)
print("Soma dos números:", soma)