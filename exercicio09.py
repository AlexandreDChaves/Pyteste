#Crie uma tupla contendo os nomes de cinco países e exiba a tupla inteira. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e,
#em seguida, exiba o número do índice (ou seja, a posição na lista) desse item na tupla.

'''paises = ('Brasil', 'Dinamarca', 'Hungria', 'Russia', 'Noruega')
print(paises)
indice = input("Inserir o nome de um dos cinco paises: ")
print(paises.index(indice))


#Crie uma lista com dois tipos de esportes. Pergunte ao usuário qual é o esporte favorito dele
#e adicione isso ao final da lista. Ordene a lista e exiba-a.

lista_esporte = ['futebol', 'basquete']
lista_esporte.append(input("Inserir o esporte favorito: "))
lista_esporte.sort()
print(lista_esporte)


#Crie uma lista com seis disciplinas escolares. Pergunte ao usuário qual dessas disciplinas
#ele não gosta. Exclua a disciplina que ele escolheu da lista antes de exibir a lista novamente.

lista_disciplina = ['matematica', 'geografia', 'historia', 'biologia', 'quimica', 'fisica']
print(lista_disciplina)
pergunta = input("Qual dessas disciplinas voce nao gosta? ")
lista_disciplina.remove(pergunta)
print(lista_disciplina)'''


#Peça ao usuário para inserir quatro de seus alimentos favoritos e armazene-os em um dicionário,
#de modo que eles sejam indexados com números começando de 1. Exiba o dicionário completo,
#mostrando o número do índice e o item. Pergunte ao usuário qual deles ele quer remover e
#retire-o da lista. Ordene os dados restantes e exiba o dicionário.

'''alimentos = {}
for i in range(1,5):
  alimento = input("Digite 4 alimentos favoritos: ")
  alimentos[i] = alimento

print("Seus alimentos favoritos: ")
for index, alimento in alimentos.items():
  print(f"{index}: {alimento}")

remover = int(input("Qual desses alimentos gostaria de remover? "))
if remover in alimentos:
  del alimentos[remover]

ordenar = dict(sorted(alimentos.items()))# Reordenar o dicionário
print("\nAlimentos ordenados após a remoção: ")
for index, alimento in alimentos.items():
  print(f"{index}: {alimento}")


#Insira uma lista com dez cores. Peça ao usuário um número inicial entre 0 e 4 e um número final
#entre 5 e 9. Exiba a lista de cores entre os números inicial e final fornecidos pelo usuário.

cores = ['azul', 'vermelho', 'amarelo', 'verde', 'roxo', 'marrom', 'lilas', 'laranja', 'rosa', 'violeta']
n1 = int(input('Digite um numero entre 0 e 4: '))
n2 = int(input('Agora digite um numero entre 5 e 9: '))
print(cores[n1:n2])


#Crie uma lista com quatro números de três dígitos. Exiba a lista para o usuário,
#mostrando cada item da lista em uma linha separada.
#Peça ao usuário para inserir um número de três dígitos. Se o número que ele digitou coincidir 
#com um da lista, exiba a posição desse número na lista, caso contrário, exiba a mensagem 
#"Esse número não está na lista".

lista_numeros = [150,729,850,999]
for i in lista_numeros:
    print(i)

n1 = int(input("Digite um numero com tres digitos: "))
if n1 in lista_numeros:
    print("Posicao do numero é: ", lista_numeros.index(n1))
else:
    print("Esse numero nao esta na lista")'''


#Crie uma lista vazia chamada "nums". Peça ao usuário para inserir números.
#Após cada número ser inserido, adicione-o ao final da lista nums e exiba a lista.
#Depois que ele tiver inserido três números, pergunte se ele ainda deseja que o último número
#inserido seja salvo. Se ele disser "não", remova o último item da lista. Exiba a lista de números.

nums = []
count = 0
while count < 3:
    n1 = int(input("Digite tres numeros: "))
    nums.append(n1)
    print(nums)
    count = count +1
    ultimo_numero = input("Deseja salvar o ultimo numero sim ou não? ")
    if ultimo_numero == 'nao':
        nums.remove(n1)
    print(nums)
        
       
    
    
