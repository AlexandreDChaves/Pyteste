import math

#Peça ao usuário para inserir um número com muitas casas decimais.
#Multiplique esse número por dois e exiba a resposta.

numero = float(input('Digite um numero com muitas casas decimais: '))
resultado = numero * 2
print(resultado)


#Atualize o programa anterior para que ele exiba a resposta com duas casas decimais.

numero = float(input('Digite um numero com muitas casas decimais: '))
resultado = numero * 2
print(f"{resultado:.2f}")


#Peça ao usuário para inserir um número inteiro que seja maior que 500.
#Calcule a raiz quadrada desse número e exiba-a com duas casas decimais.

n1 = int(input("Digite um numero interio maior que 500: "))
resposta = math.sqrt(n1)
print(f"{resposta:.2f}")


#Exiba o valor de pi (π) com cinco casas decimais.

print(f"{math.pi:.5f}")


#Peça ao usuário para inserir o raio de um círculo (medida do ponto central até a borda).
#Calcule a área do círculo (π*raio²).

raio = int(input("Digite o numero do raio: "))
area = math.pi*(raio**2)
print(area)


#Peça o raio e a profundidade de um cilindro e calcule o volume total (área do círculo * profundidade),
#arredondado para três casas decimais.
raio = int(input("Digite o numero do raio: "))
cilindro = int(input("Digite o numero do cilindro: "))
area = math.pi*(raio**2)
volume = area * cilindro
print(f"{volume:.3f}")


#Peça ao usuário para inserir dois números. Use a divisão inteira para dividir 
#o primeiro número pelo segundo e também calcule o resto,
#exibindo a resposta(por exemplo, se eles inserirem 7 e 2, exiba “7 dividido por 2 é 3 com 1 restante”).
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
calculo = n1 // n2
resto = n1 % n2
print(f"{n1} divido por {n2} e {calculo} o resto da divisao e {resto}")


#Se o usuário digitar 1, deve-se pedir o comprimento de um dos lados e exibir a área.
#Se ele selecionar 2, deve-se pedir a base e a altura do triângulo e exibir a área.
#Se ele digitar qualquer outra coisa, deve-se mostrar uma mensagem de erro apropriada.

print("Digite 1 para calcular a area do quadrado e 2 para triangulo: ")
n = int(input())
if n == 1:
    lado = int(input("Digite o comprimento em um dos lados: "))
    area = lado * lado
    print(area)
elif n == 2:
    base = int(input("Digite o comprimento da base do triângulo: "))
    altura = int(input("Digite a altura do triângulo: "))
    area = (base * altura) /2
    print(area)
else:
    print("Opcao incorreta")
