from fila_prioridade_array import *

fila = FilaPrioridadeArray()

menu = '''-------------------------
1. Chegada de pessoa para atendimento
2. Realizar atendimento
3. Listar pessoas na fila
4. Sair
-------------------------
Opção: '''

atender_prioridade = False

while True:
    opcao = input(menu)

    if opcao == '1':
        nome = input("Indique o nome da pessoa: ")
        
        while True:
            prioridade = input("Ela tem prioridade? (s/n)").lower()
            if prioridade not in "sn":
                print("Indique uma opção válida")
            else:
                if prioridade == 's': prioridade = True
                else: prioridade = False
                break

        fila.enqueue(nome, prioridade)

    if opcao == '2':
        fila.dequeue(atender_prioridade)
        atender_prioridade = not atender_prioridade

    if opcao == '3':
        print("Pessoas com prioridade:")
        for i in range(fila.i_prio, fila.f_prio):
            print(fila.fila_prio[i])

        print()
        print("Pessoas sem prioridade:")
        for i in range(fila.i_normal, fila.f_normal):
            print(fila.fila_normal[i])
        print()
