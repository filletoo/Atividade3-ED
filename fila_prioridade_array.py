class FilaPrioridadeArray:
    def __init__(self):
        #tamanhos
        self.tam_normal = 10
        self.tam_prio = 10
        #filas com e sem prioridade
        self.fila_normal = ['']*self.tam_normal
        self.fila_prio - ['']*self.tam_prio
        #indicadores
        self.inicio = -1
        self.fim = -1
        self.i_prio = -1
        self.f_prio = -1

    #redimensionar o array
    def resize(self, array, tam):
        novo = ['']*tam
        j = 0
        for i in range(len(array)):
            if array[i] != '':
                novo[j] = array[i]
                j += 1

        return novo
    
    def enqueue(self, item, prioridade = False):
        #Item sem prioridade
        if not prioridade:
            #verificar se precisa redimensionar
            if self.f_normal == self.tam_normal - 1:
                self.tam_normal *= 2
                self.fila_normal = self.resize(self.fila_normal, self.tam_normal)

            self.fila_normal[self.f_normal + 1] = item
            self.f_normal += 1

        #Item com prioridade
        elif prioridade:
            #verificar se precisa redimensionar
            if self.f_prio == self.tam_prio - 1:
                self.tam_prio *= 2
                self.fila_prio = self.resize(self.fila_prio, self.tam_prio)

            self.fila_prio[self.f_prio + 1] = item
            self.f_prio += 1

    def dequeue(self, prioridade = True):
        #se for pra pegar da fila de prioridade e tiver gente nela
        if (prioridade or (not (self.i_normal < self.f_normal))) and self.i_prio < self.f_prio:
            #verificar se precisa redimensionar
            if self.f_prio - self.i_prio <= self.tam_prio//4:
                self.tam_prio /= 2
                self.fila_prio = self.resize(self.fila_prio, self.tam_prio)

            #pegar 1 item e mover indicador de inicio
            if self.i_prio < self.f_prio:
                aux = self.fila_prio[self.i_prio + 1]
                self.fila_prio[self.i_prio + 1] = ''
                self.i_prio += 1
            return aux

        #pegar da fila normal se tiver gente nela
        elif self.i_normal < self.f_normal:
            #verificar se precisa redimensionar
            if self.f_normal - self.i_normal <= self.tam_normal//4:
                self.tam_normal /= 2
                self.fila_normal = self.resize(self.fila_normal, self.tam_normal)

            atender = ['']*2
            for i in range(2):
            #pegar item e mover indicador de inicio
                if self.i_normal < self.f_normal:
                    aux = self.fila_normal[self.i_normal + 1]
                    self.fila_normal[self.i_normal + 1] = ''
                    self.i_normal += 1
                    atender[i] = aux
            return atender

        return None
