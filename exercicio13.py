import random

#Calcule a soma dos dígitos de um número inteiro.
#Exemplo de Entrada:12345
#Exemplo de Saída:15

soma = 0
numero = 123
while numero > 0:
    soma += numero % 10
    numero = int(numero / 10)
print(soma)

#Outra solução:

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())
 
print(sum_digits('texto123numero456x7'))

#Conte quantas vogais (inclusive com acentuações) existem em uma string.
#Exemplo de Entrada:"programação"
#Exemplo de Saída: 5 vogais

texto = 'programação'
vogais = 'aeiouAEIOUãÃ'
contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
print(f"A quantidade de vogais são : {contador}")

#Conte quantos números positivos e negativos existem em um array de inteiros.
#Exemplo de Entrada: [-2, 5, -6, 8, 0, -1, 3]
#Exemplo de Saída: Positivos: 4   Negativos: 3

numbers = [-2,5,-6,8,0,-1,3]
positivos = 0
negativos = 0
for number in numbers:
    if number > 0:
        positivos = positivos + 1
    elif number < 0:
        negativos = negativos + 1
print(positivos)
print(negativos)

#Crie um programa que gere senhas aleatórias de 8 caracteres, combinando letras maiúsculas, minúsculas e números.
#Exemplo de Saída: A senha gerada é: A2bF9zP7
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']

mesclar = numeros + letras

senha = ''.join(random.sample(mesclar, 8))
print(senha)

#Crie um programa que gere uma sequência espelho. Dada uma sequência de números, o programa deve criar uma nova sequência que seja a sequência original seguida da mesma sequência em ordem inversa.
#Exemplo de Entrada: [1, 2, 3]
#Exemplo de Saída: [1, 2, 3, 3, 2, 1]
lista = [1,2,3]
lista1 = lista + lista[::-1]
print(lista1)