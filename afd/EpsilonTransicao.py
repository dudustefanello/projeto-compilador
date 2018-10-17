from Automatos import Automato

class EpsilonTransicao(Automato):
    
    def __init__(self, automato):
        super(EpsilonTransicao, self).__init__()

        self.Estados = automato.Estados
        self.Alfabeto = automato.Alfabeto
        self.Finais = automato.Finais


    def imprimir(self):
        return super().imprimir('\n\n# LIVRE DE EPSILON TRANSICOES:\n')


    def eliminarEpsilonTransicoes(self):
        self.buscarEpsilonTransicoes() 


    def buscarEpsilonTransicoes(self):        
        if super().EPSILON not in self.Alfabeto:
            return

        producoesComEpsilon = set()
        qtdEpsilon = len(producoesComEpsilon)
        qtdEstados = len(self.Estados) 
        idxEpsilon = self.Alfabeto
        i = 0

        while i < qtdEstados:                                                                       # Faz um loop pelos estados
            if i in self.Estados and len(self.Estados[i][super().EPSILON]) > 0:                             # Se houver uma transição com épsion
                self.removerEpsilonTransicoes(i, self.Estados[i][super().EPSILON][0], producoesComEpsilon)
                qtdEstados = len(self.Estados)                                                     # Atualiza a quantidade de estados
            i += 1

        self.removerEpsilonTransicoesEstados()


    def removerEpsilonTransicoes(self, transicaoOriginal, transicaoEpsilon, producoesComEpsilon):
        if len(self.Estados[transicaoOriginal][self.EPSILON]) > 0:

            for producao in list(self.Estados[transicaoEpsilon]):
                if producao != self.EPSILON and len(self.Estados[transicaoEpsilon][producao]) > 0:                    
                    self.Estados[transicaoEpsilon][producao] = (list(set(self.Estados[transicaoEpsilon][producao] + self.Estados[transicaoOriginal][producao])))                    
                    producoesComEpsilon.update(set(self.Estados[transicaoOriginal][self.EPSILON]))                    
        
        if len(self.Estados[transicaoEpsilon][self.EPSILON]) > 0:            
            if self.Estados[transicaoEpsilon][self.EPSILON][0] not in producoesComEpsilon:
                self.removerEpsilonTransicoes(transicaoEpsilon, self.Estados[transicaoEpsilon][self.EPSILON][0], producoesComEpsilon)



    def removerEpsilonTransicoesEstados(self):
        if self.EPSILON not in self.Alfabeto:
            return
        
        qtdEstados = len(self.Estados) 
        i = 0
        
        while i < qtdEstados:                           # Faz um loop pelos estados
            if i in self.Estados:                       # Se houver uma transição com Épsilon
                self.Estados[i].pop(self.EPSILON)           # Remove as produções do Épsilon
                qtdEstados = len(self.Estados)         # Atualiza a quantidade de estados
            i += 1

        self.Alfabeto.remove(self.EPSILON)




