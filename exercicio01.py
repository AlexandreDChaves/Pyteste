#Peça o primeiro nome do usuário e exiba a mensagem de saída 'Olá 
nome = input("Digite seu nome: ")
print("Olá " + nome)

#Peça o primeiro nome do usuário e, em seguida, peça o sobrenome e 
# exiba a mensagem de saída 'Olá [Primeiro Nome] [Sobrenome]

nome = input("Digite seu nome: ")
sobre_nome = input("Digite seu sobrenome: ")
print("Olá " + nome + " " + sobre_nome)

#Peça ao usuário para digitar dois números. Some-os e exiba a resposta.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
resposta = n1 + n2
print(resposta)

#Peça ao usuário para digitar três números. Some os dois primeiros números e, em seguida,
#multiplique esse total pelo terceiro número.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))
resposta = (n1 + n2) * n3
print(resposta)

#Peça o valor total da conta, depois pergunte quantas pessoas estão na mesa.
#Divida o valor total da conta pelo número de pessoas e mostre quanto cada pessoa deve pagar

conta_total = float(input("Digite o valor total da conta: "))
numero_pessoas = input("Digite a quantidade de pessoas: ")
numero_pessoas = int(numero_pessoas)
valor_por_pessoa = conta_total / numero_pessoas
print(valor_por_pessoa)

#Peça ao usuário para digitar um número maior que 100 e, em seguida, digitar um número menor que 10.
#Informe a eles quantas vezes o número menor cabe no número maior.

n100 = int(input("Digite um numero maior que cem: "))
n10 = int(input("Digite um numero menor que dez: "))
resultado = n100 // n10
print(resultado)