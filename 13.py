def main():
    numeros = []
    for i in range(5):
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)

    soma = sum(numeros)
    print("A soma dos números é:", soma)

if _name_ == "_main_":
    main()