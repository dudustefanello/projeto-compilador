import sys

class ErroLexico(Exception):
    """ Classe de tratamento de exceções
        da etapa de análise léxixa

        Tipos de Erros:
        + 1: Caractere não pertence à linguagem
        + 2: Cadeia de caracteres não é um token válido
    """


    def __init__(self, tipo, caractere, linha, coluna):
        """ Mostra no console as informações de erro e  impede a exibição de traceback

            :param tipo: Número da mensagem de erro que deve ser exibida
            :param caractere: Caractere que apresentou erro
            :param linha: Linha que apresentou erro
            :param coluna: Coluna onde está o caractere que apresentou erro
        """
        sys.tracebacklimit = 0

        self.__mostramensagem(tipo, caractere)
        self.__mostralinha(linha)
        self.__mostracoluna(coluna)


    def __mostramensagem(self, tipo, caractere):
        """ Motra a mensagem de acordo com o tipo de erro informado

            :param tipo: Número da mensagem de erro que deve ser exibida
            :param caractere: Caractere que apresentou erro
        """
        if tipo == 1:
            print('\nO caractere ' + caractere + ' não pertence à linguagem!')
        elif tipo == 2:
            print('\nA cadeia de caracteres não é um token válido!')
        elif tipo == 3:
            pass


    def __mostralinha(self, linha):
        """ Imprime na tela a linha em que o erro aconteceu

            :param linha: Linha que apresentou erro
        """
        codigo = open('./codigo.in').read().splitlines()
        print(codigo[linha])


    def __mostracoluna(self, coluna):
        """ Mostra em qual posição da linha foi encontrado o erro

            :param coluna: Coluna onde está o caractere que apresentou erro
        """
        for i in range(coluna - 1):
            print(' ', end = '')

        print('^')
