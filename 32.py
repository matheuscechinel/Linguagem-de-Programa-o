num_cidades = 5
acidentes = []
veiculos = []

for i in range(num_cidades):
    cidade = int(input("Digite o código da cidade: "))
    veiculos_passeio = int(input("Digite o número de veículos de passeio: "))
    acidentes_vitimas = int(input("Digite o número de acidentes de trânsito com vítimas: "))

    veiculos.append(veiculos_passeio)
    acidentes.append(acidentes_vitimas)

media_veiculos = sum(veiculos) / num_cidades
menor_indice = min(acidentes)
maior_indice = max(acidentes)

cidade_menor_indice = acidentes.index(menor_indice) + 1
cidade_maior_indice = acidentes.index(maior_indice) + 1

print("Média de veículos nas cinco cidades juntas:", media_veiculos)
print(f"Menor índice de acidentes pertence à cidade {cidade_menor_indice} com {menor_indice} acidentes.")
print(f"Maior índice de acidentes pertence à cidade {cidade_maior_indice} com {maior_indice} acidentes.")