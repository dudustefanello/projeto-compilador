import sys

class ErroLexico(Exception):
    ''' Classe de tratamento de exceções
        da etapa de análise léxixa

        Tipos de Erros:
        + 1: Caractere não pertence à linguagem
    '''

    def __init__(self, tipo, caractere, linha, coluna):
        ''' Mostra no console as informações de erro e 
            impede a exibição de traceback
        '''
        sys.tracebacklimit = 0

        self.__mostraMensagem(tipo, caractere)
        self.__mostraLinha(linha)
        self.__mostraColuna(coluna)


    def __mostraMensagem(self, tipo, caractere):
        ''' Motra a mensagem de acordo com o tipo
            de erro informado
        '''
        if tipo == 1:
            print('\nO caractere ' + caractere + ' não pertence à linguagem!')
        elif tipo == 2:
            print('\nA cadeia de caracteres não é um token válido!')
        elif tipo == 3:
            pass

    
    def __mostraLinha(self, linha):
        ''' Imprime na tela a linha em que
            o erro aconteceu
        '''
        codigo = open('./codigo.in').read().splitlines()
        print(codigo[linha])


    def __mostraColuna(self, coluna):
        ''' Mostra em qual posição da linha
            foi encontrado o erro
        '''
        for i in range(coluna):
            print(' ', end = '')

        print('^')