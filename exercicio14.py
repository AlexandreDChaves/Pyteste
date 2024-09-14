import random
import string

#Crie um programa que conte quantas vezes uma letra específica aparece em uma frase.
#Exemplo de Entrada: "Felizmente, funciona."  Letra: 'e'
#Exemplo de Saída:3
frase = "Felizmente, funcioana."
contador = frase.count('e')
print(contador)

#Crie um programa que valide senhas com os seguintes critérios: pelo menos 8 caracteres, pelo menos uma letra maiúscula, pelo menos uma letra minúscula e pelo menos um número.
#Exemplo de Entrada: "Seguranca123"
#Exemplo de Saída: senha válida
numeros = string.digits
lestras_minusculas = string.ascii_lowercase
lestras_maiusculas = string.ascii_uppercase
simbolos = string.punctuation
caracteres = numeros + lestras_minusculas + lestras_maiusculas + simbolos

tamanho = 13

senha = [random.choice(numeros), random.choice(lestras_minusculas), 
         random.choice(lestras_maiusculas), random.choice(simbolos)]

senha += random.choices(caracteres, k=tamanho - len(senha))

random.shuffle(senha)
senha = ''.join(senha)
if len(senha) < 13:
    print('senha fraca')
else:
    print('senha forte')

print(senha)

#Crie um programa que gere frases aleatórias combinando palavras de diferentes categorias.
#Exemplo de Entrada: (Sem Entrada)
#Exemplo de Saída: O gato preto saltou sobre o muro

animais = ['gato', 'cachorro', 'passaro']
cores = ['preto', 'branco', 'caramelo']
frases = ['fugiu para o mato', 'caiu da arvore', 'subiu no telhado']
#frase_completa = [random.choice(animais), random.choice(cores), random.choice(frases)]
frase_completa = random.choice(animais) + ' ' + random.choice(cores) + ' ' + random.choice(frases)
print(frase_completa)

