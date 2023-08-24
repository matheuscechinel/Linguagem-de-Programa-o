lista = [4, 8, 15, 16, 23, 42]
elemento = int(input("Digite o número que você quer verificar: "))

if elemento in lista:
    posicao = lista.index(elemento)
    print("O elemento", elemento, "está na posição", posicao)
else:
    print("O elemento", elemento, "não está na lista.")
