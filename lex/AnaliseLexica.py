from Automato import ImportaAutomato
from Excecoes import ErroLexico
from Tabela import Tabela

class AnaliseLexica(object):
    '''Classe de Implementação da etapa de Análise Léxica
    '''

    separadores = ['\n', ' ']
    automato = ImportaAutomato()
    tabela = Tabela()
    regras = dict()
    finais = set()
    estado = int()
    linha = int()
    coluna = int()


    def __init__(self, *args):
        super(AnaliseLexica, self).__init__(*args)
        self.regras, self.finais = self.automato.getDicionarios('./afd/automato.txt')


    def analise(self, codigo):
        ''' Executa a análise léxica do código fonte.
        '''
        self.estado = 0
        self.linha = 0
        self.coluna = 0

        self.printRegras()

        self.__percorreCodigo(codigo)

        self.printTabela()


    def __percorreCodigo(self, codigo):
        ''' Executa um laço nos caracteres do código fonte
            testanto os caracteres um a um.
        '''
        for i in open(codigo).read():
            self.__testaCaractere(i)
            self.coluna += 1


    def __testaCaractere(self, i):
        ''' Verifica se um caractere é válido dado o estado
            atual da análise
        '''

        print('\nEstado ' + str(self.estado), end='')

        if i in self.regras[self.estado]:
            self.__caractereValido(i)

        elif i in self.separadores:
            self.reconheceEstado(i)
            self.__novaLinha(i)

        else:
            raise ErroLexico(1, i, self.linha, self.coluna)


    def __caractereValido(self, i):
            print(' contem ' + i, end=', ')

            if self.regras[self.estado][i]:
                self.__saltaEstado(i)

            else:
                self.printRegras()
                print(self.estado)
                raise ErroLexico(2, i, self.linha, self.coluna)


    def __novaLinha(self, i):
        if i == '\n':
            self.coluna = 0
            self.linha += 1


    def __saltaEstado(self, i):
        if len(self.regras[self.estado][i]) > 1:
            raise ErroLexico('INDETERMINISMO NO ESTADO ' + str(self.estado))

        elif len(self.regras[self.estado][i]) == 1:
            self.estado = self.regras[self.estado][i][0]

        print('salta para ' + str(self.estado), end='')


    def printRegras(self):
        for i in self.regras:
            print(i, self.regras[i])


    def printTabela(self):
        print('\n\nTABELA DE SIMBOLOS:\n')
        for i in self.tabela:
            print(i)


    def reconheceEstado(self, i):
        if self.estado not in self.finais:
            print(self.finais)
            raise ErroLexico(3, i, self.linha, self.coluna)

        self.tabela.reconhece(self.estado, self.linha)
        self.estado = 0
