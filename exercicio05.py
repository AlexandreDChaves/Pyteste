#Peça ao usuário para inserir seu nome e, em seguida, exiba o nome dele três vezes.

nome = input("Digite seu nome: ")
for i in range(0,3):
    print(nome)


#Altere o programa anterior para que ele peça ao usuário para inserir seu nome e um número e,
#em seguida, exiba o nome dele aquele número de vezes.

nome = input("Digite seu nome: ")
numero = input("Digite um numero: ")
for i in range(0,3):
    print(nome, numero)


#Peça ao usuário para inserir seu nome e exiba cada letra do nome em uma linha separada.

nome = input("Digite seu nome: ")
for nomes in nome:
    print(nomes)


#Altere o programa anterior para também pedir um número. Exiba o nome deles (uma letra por vez em cada linha)
#e repita isso pelo número de vezes que eles inseriram.

nome = input("Digite seu nome: ")
numero = int(input("Digite um numero: "))
for x in range(0,numero):
    for i in nome:
        print(i)


#Peça ao usuário para inserir um número entre 1 e 10 e, em seguida, exiba a tabuada desse número.

n = int(input("Digite um numero entre 1 a 10: "))
for x in range(1,11):
    resultado = n * x
    print(f"{n} x {x} = {resultado}")


#Peça um número abaixo de 50 e, em seguida, faça uma contagem regressiva de 50
#até esse número, certificando-se de mostrar o número que eles inseriram na saída.

n1 = int(input("Digite um numero menor que 50: "))
for i in range(50, n1,-1):
    print(i)
    print(n1)


#Peça ao usuário para inserir seu nome e um número. Se o número for menor que 10,
#exiba o nome dele aquele número de vezes; caso contrário, exiba a mensagem "Muito alto" três vezes.

nome = input("Digite seu nome: ")
numero = input("Digite um numero: ")
if numero < 10:
    for i in range(numero):
        print(nome, numero)
else:
    for i in range(3):
        print("Muilto alto")


#Defina uma variável chamada total como 0. Peça ao usuário para inserir cinco números e,
#após cada entrada, pergunte se ele quer que aquele número seja incluído.
#Se ele quiser, então adicione o número ao total. Se ele não quiser que seja incluído,
#não adicione ao total. Após ele ter inserido todos os cinco números, exiba o total.

total = 0
for i in range(5):
    n = int(input("Digite um numero: "))
    pergunta = input("Deseja guardar esse numero sim ou nao? ")
    if pergunta == "sim":
        total = total + n
    else:
        break
print(total)


#Pergunte em qual direção o usuário quer contar (para cima ou para baixo).
#Se ele selecionar para cima, então peça a ele o número máximo e conte de 1 até esse número.
#Se ele selecionar para baixo, peça a ele para inserir um número abaixo de 20 e conte de 20 até esse 
#número. Se ele inserir algo diferente de para cima ou para baixo, exiba a mensagem "Eu não entendo".

pergunta = input("Qual direção deseja quer contar pra cima ou para baixo? ")
if pergunta == "pra cima":
    n1 = int(input("Digite um numero: "))
    for i in range(1,n1):
        print(i)
    print(n1)
elif pergunta == "para baixo":
    n1 = int(input("Digite um numero abaixo de 20: "))
    for i in range(20,n1,-1):
     print(i)
    print(n1)
else:
    print("Eu não entendo")


#Pergunte quantas pessoas o usuário quer convidar para uma festa.
#Se ele inserir um número abaixo de 10, peça os nomes e, após cada nome,
#exiba “[nome] foi convidado”. Se ele inserir um número igual ou superior a 10,
#exiba a mensagem “Muitas pessoas”.

pergunta = int(input("Quantas pessoas vão a festa: "))
if pergunta < 10:
    nome = input("digite os nomes dos convidados: ")
    for i in range(pergunta):
        print(nome, "foi convidado")
else:
    print("Muitas pessoas")
