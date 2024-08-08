#Escreva um programa que imprima os valores e as chaves do hash
#Exemplo de Entrada: { nome: 'Jett', idade: 19 }
#Exemplo de Saída:
#Nome é Jett Idade é 19

pessoa = {
    'nome': "Lee", 'idade': 56
}
print(pessoa)
#Atualizando os dados do dicionário
pessoa.update({'profissao': 'programador'})
print(pessoa)

#Escreva um programa que transforme um Array (que está disposto na sequência chave e valor) em uma estrutura de Hash.
#Exemplo de Entrada: ["nome", "corretora abc", "tipo", "empresa", "negocio", "aluguel e vendas"]
#Exemplo de Saída: { nome: "corretora abc", tipo: "empresa", negocio: "aluguel e vendas" }

lista = ["nome", "corretora abc", "tipo", "empresa", "negocio", "aluguel e vendas"]
lista_dic = [("nome", "corretora abc"), ("tipo", "empresa"), ("negocio", "aluguel e vendas")]
lista_dic = dict(lista_dic)
print(lista_dic)

#Escreva um programa que solicite ao usuário um número inteiro positivo e calcule a soma de todos os números pares menores ou iguais a esse número.
#Exemplo de Entrada: Digite um número inteiro positivo: 10
#Exemplo de Saida: A soma dos números pares até 10 é 30.

numeros = int(input("Digite um número inteiro positivo: "))
contador = 0
for i in range(numeros+1):
    if i % 2 == 0:
        contador+=i

print(f"A soma de todos os números pares menores ou iguais a {numeros} é: {contador}")

#Crie um programa que solicita ao usuário um número inteiro e gera a tabuada de multiplicação desse número até 10, exibindo-a na tela.
#Exemplo de Entrada: Digite um número inteiro positivo: 8
#Exemplo de Saída:
#8x1 = 8

n1 = int(input("Digite um numero inteiro positivo: "))
for i in range(1,11):
    print(f"{n1} x {i} = {n1*i}")


#Descubra o maior elemento em um array de inteiros.
#Exemplo de Entrada: [3, 7, 2, 8, 9, 4]
#Exemplo de Saída: O maior numero é 9

lista = [3,7,9,5,8,4]
maior_valor = lista[0]
for i in lista:
    if i > maior_valor:
        maior_valor = i
print(f"O maior valor da lista é: {maior_valor}")
