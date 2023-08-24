print("Lojas Quase Dois - Tabela de preços")
print("Quantidade\tValor")

preco_item = 1.99
for quantidade in range(1, 51):
    total = quantidade * preco_item
    print(f"{quantidade}\t\tR$ {total:.2f}")