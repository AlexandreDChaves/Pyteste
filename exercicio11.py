#Dada uma lista, escreva um programa Python para trocar o primeiro e o último elemento da lista.
lista = [12, 35, 9, 56, 24,88,98,66,77,35,45,23]
print(lista[::-1])

#Dada uma lista em Python e forneceu as posições dos elementos,
#escreva um programa para trocar os dois elementos na lista.
lista1 = [1,2,3,4,5]
lista1[0], lista1[3] = lista1[3], lista1[0]
print(lista1)

#Dada uma String qualquer, imprima na tela a quantidade de caracteres que essa String possui.
#Exemplo de Entrada: ola tudo bem?
#Exemplo de Saída: 14

texto = "A jornada contiua intensa"
print(len(texto))

#Receba o nome do usuário como entrada e Imprima o nome do usuário com todas as letras em maiúsculo.
#Exemplo de Entrada: java
#Exemplo de Saída: JAVA

palavra = "java"
print(palavra.upper())

#Receba 3 valores (numeros inteiros) do usuário e imprima eles em ordem crescente.
#Exemplo de Entrada: a = 8 b =10 c = 5
#Exemplo de Saída: 5 8 10

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite um numero: "))
numeros = [n1,n2,n3]
numeros.sort()
print(numeros[0], numeros[1], numeros[2])

#Crie uma função que recebe dois parametros, nome e idade, imprima esses valores
#no formato: "nome, idade" - obs: deve ser usada uma função para realizar o exercício.

def pessoa(nome):
    nome = input("Digite seu nome: ")
    return nome

print(pessoa())

#Escreva um programa que verifique se o Array contém o número informado
#Exemplo de Entrada
#array = [1, 2, 'teste']
#numero = 4

#Exemplo de Saída
#Não tem numero 4
lista_mista = [1,2,3,4,'texto']
n1 = 0
print(n1 in lista_mista)