#Peça ao usuário para inserir seu primeiro nome e, em seguida,
#exiba o comprimento do primeiro nome. Depois, peça o sobrenome e exiba o comprimento do sobrenome.
#Junte o primeiro nome e o sobrenome com um espaço entre eles e exiba o resultado.
#Finalmente, exiba o comprimento do nome completo (incluindo o espaço).

'''nome = input("Digite seu nome: ")
print(len(nome))
sobrenome = input("Digite seu sobrenome: ")
print(len(sobrenome))
nome_completo = nome + " - " + sobrenome
print(nome_completo)
print(len(nome_completo))'''

#Peça ao usuário para digitar sua matéria escolar favorita.
#Exiba-a com "-" após cada letra, por exemplo, E-s-p-a-n-h-o-l-.

materia = input("Digite sua materia favorita: ")
resultado = '-'.join(materia) + '-.'
print(resultado)


#Mostre ao usuário uma mensagem na linha de texto e peça um ponto de início e um ponto de término.
#Exiba os caracteres entre esses dois pontos.
msg = "A chave estava dentro do bau"
inicio = ' * '
print(inicio ,msg, end=" * ")


#Peça ao usuário para digitar seu nome e depois diga a ele quantas vogais há em seu nome.
nome = input('Digite seu nome: ')
vogais = ['a', 'e', 'i', 'o', 'u']
count = 0
nome = nome.lower()
for x in nome:
    if x in vogais:
        count = count +1
print('vogais', count)


#Peça ao usuário para inserir uma nova senha. Peça para inseri-la novamente.
#Se as duas senhas coincidirem, exiba “Obrigado”. Se as letras estiverem corretas,
#mas em maiúsculas e minúsculas diferentes, exiba a mensagem “Elas devem estar no mesmo caso”,
#caso contrário, exiba a mensagem “Incorreto”.

senha = input("Digite uma senha: ")
confere_senha = input("Repita a mesma senha: ")
if senha.lower().upper() == confere_senha.lower().upper():
    print("Senha correta")
else:
    print("Senha nao confere")


#Peça ao usuário para digitar uma palavra e, em seguida, exiba-a de trás para frente em linhas
#separadas.

palavra = input("Digite uma palavra: ")
print(palavra[::-1])