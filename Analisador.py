from AnaliseLexica import AnaliseLexica

class Analisador(object):
    ''' Classe geral de gerenciamento das etapas de compilação

        Implementa as seguintes funcionalidades do projeto:
        + Análise léxica
    ''' 

    lexico = AnaliseLexica()
    

    def __init__(self, *args):
        super(Analisador, self).__init__(*args)
    

    def analiseLexica(self, codigo):
        self.lexico.analise(codigo)


    def analisar(self, codigo):
        ''' Método que chama os métodos das etapas de análise
            do código fonte.
        '''
        self.analiseLexica(codigo)
