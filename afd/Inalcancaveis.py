from Inuteis import Inuteis
from Producao import Producao

class Inalcancaveis(Inuteis):
    
    def __init__(self, automato):
        super(Inalcancaveis, self).__init__(automato)


    def imprimir(self):
        return super().imprimir('\n\n# SEM INALCANCAVEIS:\n', True)

          
    def removerInalcancaveis(self):
        estados = self.gerarEstadosParaMinimizacao()
        self.visitaNovaProducaoInalcancavel(estados, 0) #Passa o 0 fixo pois para remover os inalcançáveis parte do estado incial;


    def visitaNovaProducaoInalcancavel(self, estados, transicao):
         if transicao in estados:
             if transicao in self.Finais:                                #Se a transição for um estado final
                 self.adicionaAutomatoMinimizado(transicao,-1,-1)        #adiciona no automato pois pelo estado inicial o atual é alcançado.

             for producao in estados[transicao]:                         #Percorre todas as produções daquela transição para seguir com a busca em profundidade
            
                if not estados[transicao][producao].temProducao():       #caso não tenha uma produção válida finaliza a recursão atual;
                    continue
            
                if estados[transicao][producao].visitado:                #Se a produção já foi visitada finaliza a recursão atual;
                    return
        
                estados[transicao][producao].visitado = True
                self.adicionaAutomatoMinimizado(transicao,producao,estados[transicao][producao].producao);  #Adiciona a produção no automato;
                self.visitaNovaProducaoInalcancavel(estados, estados[transicao][producao].producao);        #Busca recursivamente o estado final