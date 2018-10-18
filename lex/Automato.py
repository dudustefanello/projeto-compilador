import sys

from EpsilonTransicao import EpsilonTransicao
from Determinizacao import Determinizacao    
from Inalcancaveis import Inalcancaveis      
from Automatos import Automato               
from Mortos import Mortos                    

class ImportaAutomato():
    ''' Classe de importação do Automato Finito

        Importa as regras do Automato Finito construído na
        disciplina de LFA
    '''

    automato = Automato()
    livreEpsilon = EpsilonTransicao(automato)
    determinizado = Determinizacao(automato)
    semInalcancaveis = Inalcancaveis(automato)
    semMortos = Mortos(semInalcancaveis)


    def __iniciaAutomato(self):
        self.automato.carrega('./afd/linguagem.in')


    def __removeEpsilonTransicao(self):
        self.livreEpsilon = EpsilonTransicao(self.automato)
        self.livreEpsilon.eliminarEpsilonTransicoes()


    def __determinizar(self):
        self.determinizado = Determinizacao(self.automato)
        self.determinizado.determinizar()


    def __removerInalcancaveis(self):
        self.semInalcancaveis = Inalcancaveis(self.automato)
        self.semInalcancaveis.removerInalcancaveis()


    def __removerMortos(self):
        self.semMortos = Mortos(self.semInalcancaveis)
        self.semMortos.removerMortos()


    def __init__(self, *args):
        self.__iniciaAutomato()
        self.__removeEpsilonTransicao()
        self.__determinizar()
        # self.__removerInalcancaveis()
        # self.__removerMortos()



    def getDicionarios(self, path):
        # return self.automato.pegarAutomato(), self.automato.Finais
        # return self.livreEpsilon.pegarAutomato(), self.livreEpsilon.Finais
        return self.determinizado.pegarAutomato(), self.determinizado.Finais
        # return self.semInalcancaveis.pegarAutomato(), self.semInalcancaveis.Finais
        # return self.semMortos.pegarAutomato(), self.semMortos.Finais
