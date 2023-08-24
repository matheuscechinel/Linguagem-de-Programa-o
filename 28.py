candidatos = {
    1: "Candidato 1",
    2: "Candidato 2",
    3: "Candidato 3"
}

num_eleitores = int(input("Digite o número total de eleitores: "))
votos = {1: 0, 2: 0, 3: 0}

for i in range(num_eleitores):
    print(f"Eleitor {i + 1}:")
    voto = int(input("Digite o número do candidato (1, 2 ou 3): "))
    if voto in votos:
        votos[voto] += 1

for candidato, total_votos in votos.items():
    print(f"Total de votos para {candidatos[candidato]}: {total_votos}")