from fila_prioridade_array_2 import *

def mostrar_estatisticas(atendidas):
    com_prio = 0
    sem_prio = 0
    total = len(atendidas)

    for p in atendidas:
        if p.prioridade: com_prio += 1
        else: sem_prio += 1

    print(f"Total de pessoas atendidas: {total}")
    print(f"Percentual de atendimentos com prioridade: %{com_prio/total*100:.2f}")
    print(f"Percentual de atendimentos sem prioridade: %{sem_prio/total*100:.2f}")

fila = FilaPrioridadeArray()

menu = '''-------------------------
1. Chegada de pessoa para atendimento
2. Realizar atendimento
3. Listar pessoas na fila
4. Sair
-------------------------
Opção: '''

atender_prioridade = False
pessoas_atendidas = []

while True:
    opcao = input(menu)

    if opcao == '1':
        nome = input("Indique o nome da pessoa: ")
        
        '''while True:
            prioridade = input("Ela tem prioridade? (s/n)").lower()
            if prioridade not in "sn":
                print("Indique uma opção válida")
            else:
                if prioridade == 's': prioridade = True
                else: prioridade = False
                break
        '''
        if '*' in nome:
            prioridade = True
        else:
            prioridade = False

        pessoa = PessoaNaFila(nome, prioridade)
        fila.enqueue(pessoa)

    if opcao == '2':
        if fila.isEmpty():
            print("Não há mais pessoas para atender na fila")
            continue

        atender = fila.dequeue(atender_prioridade)

        if atender[0].prioridade == atender_prioridade:
            atender_prioridade = not atender_prioridade

        for i in range(len(atender)):
            if atender[i] != '':
                pessoas_atendidas.append(atender[i])
 
    if opcao == '3':
        print("Pessoas com prioridade:")
        for i in range(fila.fim + 1):
            if fila.fila[i] != '':
                if fila.fila[i].prioridade:
                    print(fila.fila[i].nome)

        print()
        print("Pessoas sem prioridade:")
        for i in range(fila.fim + 1):
            if fila.fila[i] != '':
                if not fila.fila[i].prioridade:
                    print(fila.fila[i].nome)

    if opcao == '4':
        if not fila.isEmpty():
            print("Você não pode sair agora, ainda há pessoas na fila")
        else: 
           
            break

mostrar_estatisticas(pessoas_atendidas)