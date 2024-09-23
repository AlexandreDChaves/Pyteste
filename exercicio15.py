#Descrição do Problema
#Crie um programa para verificar se as palavras são palíndromos,
#ou seja,que podem ser lidas da mesma forma de trás para frente.
palavra = 'reviver'
palavra_pali = palavra[::-1]
print(palavra_pali)

#Descrição do Problema
#Crie um programa que permite ao usuário construir uma playlist
#de músicas. Utilize um array para armazenar as músicas, e loops
#para permitir que o usuário adicione, remova, ou visualize a playlist.

playlist = []
while True:
    acao = input("Digite 'adicionar' para inserir uma música,\n 'remover' para remover uma música,\n ou 'sair' para finalizar: ").lower()

    if acao == 'adicionar':
        musica = input("Digite o nome da música para adicionar: ")
        playlist.append(musica)
        print(f"Música '{musica}' adicionada à playlist.")

    elif acao == 'remover':
        musica = input("Digite o nome da música para remover: ")
        if musica in playlist:
            playlist.remove(musica)
            print(f"Música '{musica}' removida da playlist.")
        else:
            print(f"Música '{musica}' não está na playlist.")

    elif acao == 'sair':
        break

    else:
        print("Ação inválida. Tente novamente.")

# Exibindo a playlist final
print("Playlist final:")
for play in playlist:
    print(play)


   