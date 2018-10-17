from Inuteis import Inuteis

class Mortos(Inuteis):
    
    def __init__(self, automato):
        super(Mortos, self).__init__(automato)
    
    def imprimir(self):
        return super().imprimir('\n\n# SEM MORTOS:\n')

    def removerMortos(self):
        estados = self.gerarEstadosParaMinimizacao()
        self.AutomatoMinimizado = dict()

        for transicao in estados:
            for producao in estados[transicao]:
                self.visitaNovaProducaoMortos(estados, transicao)
                estados[transicao][producao].chegouEstadoTerminal = self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao)
        

    def visitaNovaProducaoMortos(self, estados, transicao):
        if transicao in estados:
            if (transicao in self.Finais) and (estados[transicao] == {}) :
                self.adicionaAutomatoMinimizado(transicao,-1,-1)
                return True

            for producao in estados[transicao]:

                if estados[transicao][producao].chegouEstadoTerminal or (transicao in self.Finais):
                    return True
            
                if not estados[transicao][producao].temProducao():        #caso não tenha uma produção válida
                    return False

                if estados[transicao][producao].visitado:
                    continue

        
            estados[transicao][producao].visitado = True
                       
            
            if self.visitaNovaProducaoMortos(estados, estados[transicao][producao].producao):
                estados[transicao][producao].chegouEstadoTerminal = True
                self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao)
                return True

        return False