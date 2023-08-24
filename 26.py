 while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break

while True:
    idade = int(input("Digite a idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break

while True:
    salario = float(input("Digite o salário (maior que zero): "))
    if salario > 0:
        break

while True:
    sexo = input("Digite o sexo: ")
    if sexo.lower() in ['m', 'f']:
        break

while True:
    estado_civil = input("Digite o estado civil: ")
    if estado_civil.lower() in ['solteiro', 'casado', 'viuvo', 'divorciado']:
        break