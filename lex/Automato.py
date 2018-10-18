from Automatos import Automato
from Determinizacao import Determinizacao
from EpsilonTransicao import EpsilonTransicao
from Inalcancaveis import Inalcancaveis
from Mortos import Mortos


class ImportaAutomato():
    """ Classe de importação do Automato Finito

        Importa as regras do Automato Finito construído na disciplina de LFA
    """

    automato = Automato()
    livreEpsilon = EpsilonTransicao(automato)
    determinizado = Determinizacao(automato)
    semInalcancaveis = Inalcancaveis(automato)
    semMortos = Mortos(semInalcancaveis)


    def __init__(self):
        self.__iniciaautomato()
        self.__removeepsilontransicao()
        self.__determinizar()
        self.__removerinalcancaveis()
        self.__removermortos()


    def __iniciaautomato(self):
        """ Faz a carga do automato finito
        """
        self.automato.carrega('./afd/linguagem.in')


    def __removeepsilontransicao(self):
        """ Elimina epsilons transições do automato
        """
        self.livreEpsilon = EpsilonTransicao(self.automato)
        self.livreEpsilon.eliminarEpsilonTransicoes()


    def __determinizar(self):
        """ Determiniza o automato finito
        """
        self.determinizado = Determinizacao(self.automato)
        self.determinizado.determinizar()


    def __removerinalcancaveis(self):
        """ Executa a primeira etapa da minimização do automato, a remoção de estados inalcancáveis
        """
        self.semInalcancaveis = Inalcancaveis(self.automato)
        self.semInalcancaveis.removerInalcancaveis()


    def __removermortos(self):
        """ Executa a segunda etapa da minimização do automato, a remoção de estados mortos
        """
        # self.semMortos = Mortos(self.semInalcancaveis)
        # self.semMortos.removerMortos()


    def getdicionarios(self, escolha):
        """ Retorna o dicionario carregado de acordo com a escolha da etapa:
            + 1: Automato indeterminístico
            + 2: Automato livre de epsilons transições
            + 3: Automato determinizado
            + 4: Automato sem estados inalcancáveis
            + 5: Automato sem estados mortos

            :return: Dicionario do autômato carregado
        """
        if escolha == 1:
            return self.automato.pegarAutomato(), self.automato.Finais
        elif escolha == 2:
            return self.livreEpsilon.pegarAutomato(), self.livreEpsilon.Finais
        elif escolha == 3:
            return self.determinizado.pegarAutomato(), self.determinizado.Finais
        elif escolha == 4:
            return self.semInalcancaveis.pegarAutomato(), self.semInalcancaveis.Finais
        elif escolha == 5:
            return self.semMortos.pegarAutomato(), self.semMortos.Finais

