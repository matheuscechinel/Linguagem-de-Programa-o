lista = []
for i in range(5):
    item = input("Digite um item para a lista: ")
    lista.append(item)

itens_repetidos = find_repeated_items(lista)

print("Itens repetidos:")
for item in itens_repetidos:
    print(item)


def find_repeated_items(lista):
    itens_repetidos = []
    contagem = {}

    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1

    for item, quantidade in contagem.items():
        if quantidade > 1:
            itens_repetidos.append(item)

    return itens_repetidos


if _name_ == "_main_":
    main()