#Defina o total como 0 para começar. Enquanto o total for 50 ou menos,
#peça ao usuário para digitar um número. Adicione esse número ao total e imprima a mensagem
#"O total é... [total]". Pare o loop quando o total for superior a 50.

total = 0
while total <= 50:
    numero = int(input("Digite um numero: "))
    total += numero
    print(total)


#Peça ao usuário para inserir um número. Continue pedindo até que ele insira um valor maior que 5 e,
#em seguida, exiba a mensagem "O último número que você inseriu foi [número]" e pare o programa.

n1 = 0
while n1 <= 5:
   n1 = int(input("Digite um numero: "))
print(n1)


#Peça ao usuário para inserir um número e depois outro número. Some esses dois números
#e pergunte se ele quer adicionar outro número. Se ele digitar "s",
#peça para inserir outro número e continue somando números até que ele não responda "s".
#Quando o loop parar, exiba o total.

n1 = int(input('Digite um numero: '))
total = n1
resposta = 'sim'
while resposta == 'sim':
    n2 = int(input('Digite outro numero: '))
    total = n1 + n2
    resposta = input("Deseja add outro numero? ")
print(total)


#Peça o nome de alguém que o usuário quer convidar para uma festa. Após isso,
#exiba a mensagem “[nome] foi convidado(a)” e adicione 1 à contagem. Em seguida,
#pergunte se ele quer convidar mais alguém. Continue repetindo isso até que ele não queira mais
#convidar ninguém para a festa e, então, exiba quantas pessoas foram convidadas para a festa.

cont = 1
resposta = 'sim'
while resposta == 'sim':
    nome = input("Digite o nome do convidado: ")
    print(nome, "foi convidado")
    cont += 1
    resposta = input("Deseja convidar mais alguem? ")
print("O total de convidados foram: ", cont)


#Crie uma variável chamada compnum e defina o valor como 50. Peça ao usuário para inserir um número.
#Enquanto o palpite dele não for igual ao valor de compnum, diga se o palpite dele é muito baixo ou 
#muito alto e peça para ele tentar novamente. Se ele inserir o mesmo valor que compnum,
#exiba a mensagem "Muito bem, você precisou de [contagem] tentativas".

compnum = 50
cont = 0
n1 = int(input("Digite um número: "))
while n1 != compnum:
    if n1 < compnum:
        print("Valor baixo")
    elif n1 > compnum:
        print("Valor alto")
    
    n1 = int(input("Digite um número: "))
    cont += 1

print(f"Muito bem, você precisou de {cont} tentativas")


#Peça ao usuário para inserir um número entre 10 e 20. Se ele inserir um valor abaixo de 10,
#exiba a mensagem "Muito baixo" e peça para ele tentar novamente. Se ele inserir um valor acima de 20,
#exiba a mensagem "Muito alto" e peça para ele tentar novamente. Continue repetindo isso até que ele
#insira um valor entre 10 e 20.

num = int(input("Digite um número entre 10 e 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Muito baixo")
    else:
        print("Muito alto")
    num = int(input("Digite um número entre 10 e 20: "))

print("OK")
         
       