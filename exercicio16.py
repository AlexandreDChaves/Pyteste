#Descrição do Problema
#Desenvolva um programa que monitora a temperatura de uma sala ao longo do dia.
#Armazene as leituras de temperatura em um array e use loops para calcular a média,
#a temperatura mais alta e a mais baixa.
#Exemplo de Entrada: Temperaturas registradas ao longo do dia, exemplo: [27.6, 32.3, 29.5]
#Exemplo de Saída:Média de temperatura, temperatura mais alta e mais baixa.

temperaturas = [27.6, 32.3, 29.5]
valor_min = min(temperaturas)
valor_max = max(temperaturas)
media = sum(temperaturas)/ len(temperaturas)
print(f"Valor minimo: {valor_min}, valor máximo: {valor_max} e a media: {media}")

#Descrição do Problema:
#Faça um programa para gerenciar reservas em um hotel. Use um dicionario para representar os quartos
#disponíveis e outro para os ocupados. Permita que usuários façam reservas,
#cancelamentos e busquem por quartos vazios.


qtd_quartos = {
    'reservados': 0,
    'cancelados': 0,
    'disponiveis': 20
}
while True:
    print(f"Quartos disponiveis: {qtd_quartos['disponiveis']} ")
    opcao = input("Escolha (r)eserva, (c)ancelar ou (s)air do programa: ").lower()
    if opcao == 'r':
        quarto_reservado = int(input("Quantos quartos deseja reservar? "))
        if quarto_reservado <= qtd_quartos['disponiveis']:
            qtd_quartos['reservados'] += quarto_reservado
            qtd_quartos['disponiveis'] -= quarto_reservado
            print(f"Quartos reservados: {quarto_reservado}")
        else:
            print("Não há quartos disponiveis")    
    elif opcao == 'c':
        quarto_cancelado = int(input("Quantos quartos deseja cancelar? "))
        if quarto_cancelado <= qtd_quartos['reservados']:
            qtd_quartos['reservados'] -= quarto_cancelado
            qtd_quartos['cancelados'] += quarto_cancelado
            qtd_quartos['disponiveis'] += quarto_cancelado
            print(f"Quartos cancelados: {quarto_cancelado}")
        else:
            print("Não há quartos para cancelar")
    elif opcao == 's':
        break
        
    else:
        print("Opção inválida tente novamente")

