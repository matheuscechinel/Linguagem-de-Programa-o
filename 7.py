preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.05
acrescimo = preco * 0.15
novo_preco_desconto = preco - desconto
novo_preco_acrescimo = preco + acrescimo
print("Novo preço com 5% de desconto:", novo_preco_desconto)
print("Novo preço com 15% de acréscimo:", novo_preco_acrescimo)