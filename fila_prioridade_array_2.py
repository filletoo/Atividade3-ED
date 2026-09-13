class PessoaNaFila:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

class FilaPrioridadeArray:
    def __init__(self):
        #tamanhos
        self.tam = 20
        #filas com e sem prioridade
        self.fila = ['']*self.tam
        #indicadores
        self.quant = 0
        self.fim = -1

    #redimensionar o array
    def redimensionar_fila(self):
        tam = self.tam
        array = self.fila
        novo = ['']*tam
        j = 0
        for i in range(self.fim + 1):
            if array[i] != '':
                novo[j] = array[i]
                j += 1

        self.fim = self.tam - 1
        return novo
    
    def enqueue(self, pessoa):
        #ver se precisa redimensionar
        if self.fim == self.tam - 1:
            self.tam *= 2
            self.redimensionar_fila()

        self.fila[self.fim + 1] = pessoa
        self.fim += 1
        self.quant += 1

    def dequeue(self, prioridade):
        if self.isEmpty(): return False

        com_prio = sem_prio = 0
        for i in range(self.fim + 1):
            if self.fila[i] != '':
                if self.fila[i].prioridade:
                    com_prio += 1
                else:
                    sem_prio += 1

        #ver se precisa redimensionar
        if self.quant == self.tam//4:
            self.tam //= 2
            self.redimensionar_fila()
            self.fim = self.quant - 1

        if (prioridade and com_prio != 0) or sem_prio == 0:
            atender = ['']
            for i in range(self.fim + 1):
                if self.fila[i] != '' and self.fila[i].prioridade:
                    atender[0] = self.fila[i]
                    self.fila[i] = ''
                    self.quant -= 1
                    break
        
        if (not prioridade and sem_prio != 0) or com_prio == 0:
            atender = ['']*2
            j = 0
            for i in range(self.fim + 1):
                if self.fila[i] != '' and not self.fila[i].prioridade:
                    atender[j] = self.fila[i]
                    self.fila[i] = ''
                    j += 1
                    self.quant -= 1
                if j == 2: break
        return atender

    def isEmpty(self):
        return (self.quant == 0)