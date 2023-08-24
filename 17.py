altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M/F): ")

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido.")
    peso_ideal = None

if peso_ideal:
    print("O peso ideal é:", peso_ideal)