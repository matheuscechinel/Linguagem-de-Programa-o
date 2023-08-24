candidatos = ["Candidato 1", "Candidato 2", "Candidato 3", "Candidato 4"]

total_votos = [0, 0, 0, 0, 0, 0]  # [Candidato 1, Candidato 2, Candidato 3, Candidato 4, Nulos, Brancos]

while True:
    voto = int(input("Digite o código do candidato (1 a 4), 5 para voto nulo ou 6 para voto em branco: "))

    if voto >= 1 and voto <= 4:
        total_votos[voto - 1] += 1
    elif voto == 5:
        total_votos[4] += 1
    elif voto == 6:
        total_votos[5] += 1
    else:
        print("Voto inválido!")

    continuar = input("Deseja registrar outro voto? (s/n): ")

    if continuar.lower() != "s":
        break

print("Total de votos para cada candidato:")
for i in range(4):
    print(f"{candidatos[i]}: {total_votos[i]}")

print("Total de votos nulos:", total_votos[4])
print("Total de votos em branco:", total_votos[5])

# Verifica quem ganhou a eleição
votos_candidatos = total_votos[:4]
votos_maximos = max(votos_candidatos)

if votos_candidatos.count(votos_maximos) > 1:
    print("A eleição terminou em empate.")
else:
    indice_ganhador = votos_candidatos.index(votos_maximos)
    ganhador = candidatos[indice_ganhador]
    print("O candidato vencedor é:", ganhador)
