#Peça dois números. Se o primeiro for maior que o segundo, exiba o segundo número primeiro e depois o primeiro número, caso contrário,
#mostre o primeiro número primeiro e depois o segundo.

n1 = 3
n2 = 5
if n1 > n2:
    print(n2, n1)
else:
    print(n1, n2)


#Peça ao usuário para digitar um número entre 10 e 20 (inclusive). Se ele digitar um número dentro desse intervalo, exiba a mensagem 'Ok',
#caso contrário, exiba a mensagem 'Resposta incorreta.

numero = int(input("Digite um numero entre 10 a 20: "))
if numero >= 10 and numero <= 20:
    print("Ok")
else:
    print('Resposta incorreta')


#Peça ao usuário para digitar sua cor favorita. Se ele digitar 'red', 'RED' ou 'Red', exiba a mensagem 'Eu também gosto de vermelho', 
#caso contrário, exiba a mensagem 'Eu não gosto de [cor], eu prefiro vermelho

cor = input("Digite sua cor preferida: ")
if cor == "vermelho" or cor == "Vermelho" or cor == "VERMELHO":
    print("Eu também gosto de: ", cor)
else:
    print(f"Eu não gosto da {cor}, eu prefiro vermelho")


#Pergunte ao usuário se está chovendo e converta a resposta para letras minúsculas,
#para que não importe em que caso ele digite. Se ele responder 'sim', pergunte se está ventando.
#Se ele responder 'sim' a essa segunda pergunta, exiba a mensagem 'Está ventando para
#um guarda-chuva', caso contrário, exiba a mensagem 'Leve um guarda-chuva'.
# Se ele não respondeu 'sim' à primeira pergunta, exiba a mensagem 'Aproveite seu dia.

pergunta = input("Esta chovendo? ")
pergunta = pergunta.lower()
if pergunta == 'sim':
    pergunta2 = input("esta ventando? ")
    pergunta2 = pergunta2.lower()
    if pergunta2 == 'sim':
        print("Está ventando para um guada-chuva")
    else:
        print("Leve um gurda-chuva")
else:
    print('Aproveite seu dia')


#Pergunte a idade do usuário. Se ele tiver 18 anos ou mais, exiba a mensagem 
#'Você pode votar', se ele tiver 17 anos, exiba a mensagem 'Você pode aprender a dirigir',
#se ele tiver 16 anos, exiba a mensagem 'Você pode comprar um bilhete de loteria',
#se ele tiver menos de 16 anos, exiba a mensagem 'Você nao tem idade suficiente.

idade = int(input("Qual é a sua idade? "))
if idade >= 18:
    print("Voce pode votar")
elif idade == 17:
    print("Voce pode aprender a dirigir")
elif idade == 16:
    print("Voce pode comprar um bilhete na loteria")
else:
    print("Voce não tem idade suficiente")


#Peça ao usuário para digitar um número. Se for menor que 10,
#exiba a mensagem 'Muito baixo', se o número estiver entre 10 e 20,
#exiba 'Correto', caso contrário, exiba 'Muito alto.

number = int(input("Digite um numero: "))
if number < 10:
    print("Muito baixo")
elif number >= 10 and number <= 20:
    print("Correto")
else:
    print("Muito alto")
