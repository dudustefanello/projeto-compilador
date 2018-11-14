from Automato import ImportaAutomato
from Excecoes import ErroLexico
from Tabela import Tabela


class AnaliseLexica(object):
    """ Classe de Implementação da etapa de Análise Léxica
    """

    separadores = ['\n', ' ']
    separadoresTokens = ['(', ')', '+', '-', '.']

    automato = ImportaAutomato()
    tabela = Tabela()
    regras = dict()
    finais = set()
    estado = int()
    linha = int()
    coluna = int()


    def __init__(self, *args):
        super(AnaliseLexica, self).__init__(*args)
        self.regras, self.finais = self.automato.getdicionarios(3)


    def analise(self, codigo):
        """ Executa a análise léxica do código fonte.

            :param codigo: path do código fonte para análise
        """
        self.estado = 0
        self.linha = 0
        self.coluna = 0

        # self.__printregras()

        self.__percorrecodigo(codigo)

        self.__printtabela()


    def __percorrecodigo(self, codigo):
        """ Executa um laço nos caracteres do código fonte
            testanto os caracteres um a um.

            :param codigo: path do código fonte para análise
        """
        for i in open(codigo).read():
            self.__testacaractere(i)
            self.coluna += 1


    def __testacaractere(self, i):
        """ Verifica se o caractere encontrado pode ser processado

            :param i: caractere para testar
        """
        if i in self.regras[self.estado]:
            self.__caracterevalido(i)

        elif i in self.separadores:
            self.__reconheceestado(i)
            self.__novalinha(i)

        else:
            raise ErroLexico(1, i, self.linha, self.coluna)


    def __caracterevalido(self, i):
        """ Verifica se um caractere pertencente à linguagem
            é válido dado o estado atual da análise.
            Tokens que também são separadores fazem parte do alfabeto da linguagem.

            :param i: caractere para testar
        """
        if self.regras[self.estado][i]:
            self.__saltaestado(i)

        elif i in self.separadoresTokens:
            self.__reconheceseparadorespecial(i)

        else:
            raise ErroLexico(2, i, self.linha, self.coluna)


    def __reconheceseparadorespecial(self, i):
        """ Reconhece um estado que é separador e token.

            :param i: carctere para testar
        """
        self.__reconheceestado(i)
        self.__saltaestado(i)
        self.__reconheceestado(i)


    def __novalinha(self, i):
        """ Incrementa contador de linhas sempre que encontrar '\n'

            :param i:  caractere para testar
        """
        if i == '\n':
            self.coluna = 0
            self.linha += 1


    def __saltaestado(self, i):
        """ Troca o estado da análise de acordo com o

            :param i: caractere para testar
        """
        if len(self.regras[self.estado][i]) > 1:
            raise ErroLexico('INDETERMINISMO NO ESTADO ' + str(self.estado))

        elif len(self.regras[self.estado][i]) == 1:
            self.estado = self.regras[self.estado][i][0]


    def __printregras(self):
        """ Imprime todas as regras do automato, estado por estado.
        """
        for i in self.regras:
            print(i, self.regras[i])


    def __printtabela(self):
        """ Imprime todas as linhas da tabela de símbolos
        """
        print('\n\nTABELA DE SIMBOLOS:\n')
        for i in self.tabela:
            print(i)


    def __reconheceestado(self, i):
        """ Insere um estado reconhecido na tabela de símbolos

            :param i: caractere para testar
        """
        if self.estado not in self.finais:
            print(self.finais)
            raise ErroLexico(3, i, self.linha, self.coluna)

        self.tabela.reconhece(self.estado, self.linha)
        self.estado = 0
