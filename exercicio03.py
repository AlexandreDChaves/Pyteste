#Peça ao usuário para digitar seu primeiro nome e, em seguida, exiba o comprimento do nome

nome = input("Digite seu nome: ")
print(len(nome))


#Peça ao usuário para digitar seu primeiro nome e, em seguida, peça para digitar seu sobrenome. Junte-os com um espaço entre eles e exiba o nome completo
#e o comprimento do nome completo.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(len(nome + sobrenome))


#Peça ao usuário para digitar seu primeiro nome e sobrenome em letras minúsculas.
#Mude para a forma capitalizada (title case) e junte-os. Exiba o resultado final.

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_junto = nome.capitalize() + sobrenome.capitalize()
print(nome_junto)


#Peça para o usuario digitar um nome de uma cidade e exiba o comprimento da string.
#Peça um número de início e um número de término e, em seguida, 
#exiba apenas essa seção do texto (lembre-se de que o Python começa a contar a partir de 0 e não de 1)

cidade = input("Digite o nome de uma cidade: ")
print(len(cidade))
incio = int(input("Digite numero inicial"))
fim = int(input("Digite numero final"))
resultado = (cidade[incio:fim])
print(resultado)


#Peça ao usuário para inserir o seu primeiro nome. Se o comprimento do primeiro nome for menor que cinco
#caracteres, peça para ele inserir o seu sobrenome e junte-os (sem espaço) e exiba o nome em letras
#maiúsculas. Se o comprimento do primeiro nome for cinco ou mais caracteres, 
#exiba o primeiro nome em letras minúsculas.

nome = input("Digite seu nome: ")
if len(nome) < 5:
    sobrenome = input('Digite seu sobrenome: ')
    nome_completo = nome.upper() + sobrenome.upper()
    print(nome_completo)
else:
    print(nome.lower())