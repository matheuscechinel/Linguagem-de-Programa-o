nome = input("Digite o nome do funcionário: ")
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

salario_bruto = horas_trabalhadas * valor_hora
desconto_inss = salario_bruto * 0.02
salario_liquido = salario_bruto - desconto_inss

print("Nome:", nome)
print("Salário líquido:", salario_liquido)