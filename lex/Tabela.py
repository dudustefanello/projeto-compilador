class Tabela(list):

    def __init__(self, *args):
        super(Tabela, self).__init__(*args)

    
    def reconhece(self, estado, linha):
        self.append((estado, linha))
        