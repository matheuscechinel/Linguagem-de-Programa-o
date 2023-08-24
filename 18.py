nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 * 5 + nota2 * 5 + nota3 * 10) / 20

if media >= 6.0:
    situacao = "aprovado"
else:
    situacao = "reprovado"

print("Média:", media)
print("Situação:", situacao)