def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("Escolha uma opção:")
print("1 - Converter de Fahrenheit para Celsius")
print("2 - Converter de Celsius para Fahrenheit")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit é igual a {celsius:.2f} Celsius.")
elif opcao == 2:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius é igual a {fahrenheit:.2f} Fahrenheit.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")