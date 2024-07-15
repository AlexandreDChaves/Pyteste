import random

#Exibir um número inteiro aleatório entre 1 e 100.
num = random.randint(1,100)
print(num)


#Exibir uma fruta aleatória de uma lista de cinco frutas

frutas = ['banana', 'uva', 'limão', 'pêra']
frutas_aleatoria = random.choice(frutas)
print(frutas_aleatoria)


#Escolha aleatoriamente entre cara ou coroa ("c" ou "k"). Peça
#ao usuário para fazer a escolha dele. Se a escolha do usuário for a mesma
#que o valor selecionado aleatoriamente, exiba a mensagem
#"Você ganhou", caso contrário exiba "Que azar". No final, diga
#ao usuário se o computador selecionou cara ou coroa.

cara_coroa = input("Digite cara ou coroa: ")
pc_cara_coroa = ['cara', 'coroa']
cara_coroa_aleatorio = random.choice(pc_cara_coroa)
if cara_coroa_aleatorio == cara_coroa:
    print("Voce ganhou")
else:
    print("Que azar")
print("escolha da máquina", cara_coroa_aleatorio)


'''Crie um quiz de matemática que faça cinco perguntas gerando
aleatoriamente dois números inteiros para formar a pergunta
(ex.: [num1] + [num2]). Peça ao usuário para digitar a
resposta. Se ele acertar, adicione um ponto ao placar dele. No
final do quiz, diga quantas ele acertou de cinco.'''

pontos = 0
for i in range(1,6):
    n1 = random.randint(1,50)
    n2 = random.randint(1,50)
    resposta = n1 + n2
    print(n1, "+", n2, "=")
    pergunta = int(input("Digite a sua resposta: "))
    print()
    if resposta == pergunta:
      pontos = pontos +1
print(pontos)


'''Exiba cinco cores e peça ao usuário para escolher uma. Se ele
escolher a mesma que o programa escolheu, diga "Muito bem",
caso contrário, exiba uma resposta espirituosa que envolva a
cor correta, por exemplo, "Aposto que você está VERDE de inveja"
ou "Você provavelmente está se sentindo AZUL agora". Peça
para ele adivinhar novamente; se ele ainda não acertar,
continue dando a mesma dica e peça ao usuário para
inserir uma cor até que ele acerte.'''

cores = ['azul', 'verde', 'vermelho', 'amarelo', 'roxo']
cores_aleatoria = random.choice(['azul', 'verde', 'vermelho', 'amarelo', 'roxo'])
print(cores)
escolha_cores = input("Escolha uma cor: ")
if cores_aleatoria == escolha_cores:
    print("Muito bem")
else:
    print("Não foi dessa vez")