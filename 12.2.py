def main():
    filmes = ["Matrix", "O Senhor dos Anéis"]
    jogos = ["The Witcher 3", "Dark Souls"]
    livros = ["1984", "Harry Potter"]
    esporte = ["Futebol", "Basquete"]

    listas = [filmes, jogos, livros, esporte]

    livro_acessado = livros[0]
    print("Item da lista livros:", livro_acessado)

    item_removido = esporte.pop(0)
    print("Item removido da lista esporte:", item_removido)

    if _name_ == "_main_":
    main()