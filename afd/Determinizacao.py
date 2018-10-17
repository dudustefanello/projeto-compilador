from Automatos import Automato

class Determinizacao(Automato):
    '''Classe que implementa a determinização de um automato'''

    # -- Inicialização da Classe
    def __init__(self, automato):
        super(Determinizacao, self).__init__()

        self.Estados = automato.Estados
        self.Alfabeto = automato.Alfabeto
        self.Finais = automato.Finais


    # -- Chama a função imprimir da classe pai
    def imprimir(self):
        return super().imprimir('\n\n# DETERMINIZADO:\n')


    # -- Inicia o processo de determinização
    def determinizar(self):
        self.buscarIndeterminismo() # Busca indeterminismos para determinizar


    # -- Adiciona uma nova produção ao conjunto de estados finais
    def adicionaEstadoFinal(self, producoes, novaProducao):
        for producao in producoes:              # Loop nas produções
            if producao in self.Finais:         # Para cada produção que for final
                self.Finais.add(novaProducao)   # Adiciona a nova produção também ao conjunto de finais


    # -- Substitui um indeterminismo por uma string concatenando as transições
    def substituiNovaProducao(self):
        if len(self.NovosEstados) > 0:                                                                  # Se foram criadas novas produções na determinização
            for estado in self.Estados:                                                                 # Para cada estado do automato
                for simbolo in sorted(self.Alfabeto):                                                   # e para cada símbolo do alfabeto
                    if len(self.Estados[estado][simbolo]) > 1:                                          # se a quantidade de transições por uma produção foi maior que 1
                        producaoAgrupada = self.geraProducaoAgrupada(self.Estados[estado][simbolo])     # gera uma "Produção Agrupada", para se conhecer a origem da nova produção
                        if producaoAgrupada in self.NovosEstados:                                       # Se essa produção estiver nas novas produções
                            self.Estados[estado][simbolo] = [self.NovosEstados[producaoAgrupada][0]]    # O automato recebe a nova produção gerada


    # -- Percorre o autômato identificando e tratando seus indeterminismos
    def buscarIndeterminismo(self):
        qtdEstados = len(self.Estados)                                                  # Marca a quantidade inicial de estados do autômato
        i = 0                                                                           # Zera a variável de índice
        while i < qtdEstados:                                                           # Faz um loop pelos estados
            for j in sorted(self.Alfabeto):                                             # Itera um laço pelo conjunto de símbolos do alfabeto
                if i in self.Estados and len(self.Estados[i][j]) > 1:                   # Se houver uma transição estiver indeterminada:
                    self.determinizarProducao(self.Estados[i][j])                       # Determiniza o estado

                    qtdEstados = len(self.Estados)                                      # Atualiza a quantidade de estados
            i += 1                                                                      # Incrmenta o índice.

            if i == qtdEstados:                                                         # Se a iteração estiver no último estado
                for novoEstado in list(self.NovosEstados):                              # Percorre a lista de novas produções
                    if self.NovosEstados[novoEstado][0] not in self.Estados:            # Se ela não estiver no conjunto de estados do automato
                        self.determinizarProducao(self.NovosEstados[novoEstado][1])     # Determiniza o novo estado
                        qtdEstados = len(self.Estados)                                  # Atualiza a quantidade de estados


    # -- Determiniza um estado do automato
    def determinizarProducao(self, producoes):
        estadoTemporario = dict()
        producaoAgrupada = self.geraProducaoAgrupada(producoes)

        if ((producaoAgrupada not in self.NovosEstados) or                                                      # Se a prudução agrupada não existir nas novas produções
            (self.NovosEstados[producaoAgrupada][0] not in self.Estados)):                                      # Ou se a nova regra não estiver no automato
            if (len(producoes) > 1) and (not self.existeProducaoAgrupada(producoes)):                           # se o tamanho dessas produções for maior que 1 e não existe produção agrupada pra ela
                novoEstado = self.pegarNovoEstadoDetrminizacao()                                                # Então paga o novo estado determinizado
                self.NovosEstados.update({self.geraProducaoAgrupada(producoes): [novoEstado,producoes]})        # e coloca ele na estrutura de novos estados

            for i in producoes:                                                                                 # Faz um loop nas produções que que contém a indeterminação
                for j in sorted(self.Alfabeto):                                                                 # Fazendo loop no conjunto de símbolos do alfabeto
                    if j in estadoTemporario:                                                                   # Se o o símbolo j já estiver no estado temporário:
                        lista = list(set(estadoTemporario[j] + self.pegarProducaoOriginal(self.Estados[i][j]))) # Adiciona a lista de transições de j
                        estadoTemporario[j] = lista                                                             # ao estado criado

                        if (len(lista) > 1) and (not self.existeProducaoAgrupada(lista)):                       # Se a largura dessa lista for maior que 1 e não existe produção agrupada pra ela
                            novoEstado = self.pegarNovoEstadoDetrminizacao()                                    # Enumera um novo estado
                            self.NovosEstados.update({self.geraProducaoAgrupada(lista): [novoEstado,lista]})    # Adiciona aos novos estados

                    else:                                                                                       # Se o o símbolo j não estiver no estado temporário:
                        producaoAtual = list(set(self.Estados[i][j]))                                           # Concatena as transições de j

                        if len(producaoAtual) > 1:                                                              # Se tiver mais de uma produção
                            producaoAgrupadaTemp = self.geraProducaoAgrupada(producaoAtual)                     # Gera uma nova produção agrupada
                            if self.existeProducaoAgrupada(producaoAgrupadaTemp):                               # e se essa produção já existe
                                estadoTemporario.update({j: list(set(self.NovosEstados[producaoAgrupada][1]))}) # Atualiza o estado temporário

                        elif (len(producaoAtual) > 0) and (self.existeNovoEstado(producaoAtual[0])):            # se não se essa proodução não for nula e existe um estado para essa transição
                            for prod in self.NovosEstados:                                                      # Efetua um loop nesses novos estados
                                if self.NovosEstados[prod][0] == producaoAtual[0]:                              # e para o estado que for igual à transição
                                    estadoTemporario.update({j: list(set(self.NovosEstados[prod][1]))})         # Atualiza o estado
                        else:                                                                                   # Senão
                            estadoTemporario.update({j: producaoAtual})                                         # Adiciona uma nova transição ao estado temporário

            self.setAlfabetoEstado(estadoTemporario);                                                           # Relaciona o estado temporário com os símbolos do alfabeto
            self.Estados.update({self.NovosEstados[producaoAgrupada][0]: estadoTemporario});                    # Adiciona o estado temporário ao dicionário de estados da classe
            self.adicionaEstadoFinal(producoes, self.NovosEstados[producaoAgrupada][0])                         # Verifica se deve adicionar aos estados finais
            self.substituiNovaProducao()                                                                        # Verifica as produção criadas


    # -- Insere os elementos de uma lista para uma string
    def geraProducaoAgrupada(self, lista):
        estado = ''
        for item in lista:                  # Para cada item da lista dada
            if estado == '':                # se for no inicio
                estado += str(item)         # Concatena o item
            else:                           # se for no meio
                estado += ',' + str(item)   # concatena com a vpirgula

        return estado                       # Retorna a string


    # -- Verifica se uma lista dada já foi inserida em um estado novo
    def existeProducaoAgrupada(self, lista):
        retorno = False

        if len(lista) > 1:                                          # Se o tamanho da lista dada for maior que um
            producaoAgrupadaTemp = self.geraProducaoAgrupada(lista) # Verifica pela sua possível produção agrupada
            return (producaoAgrupadaTemp in self.NovosEstados)
        else:                                                       # Senão
            for i in self.NovosEstados:                             # Percorre os novos estados
                if lista[0] in self.NovosEstados[i][1]:             # Verificando se a produção já existe
                    return True
        return retorno


    # -- Adiciona uma nova produção para contabilizar o novo tamanho do automato
    def pegarNovoEstadoDetrminizacao(self):
        novasProducoes = []
        for producao in self.NovosEstados:                          # Para cada produção dos novos estados
            novasProducoes.append(self.NovosEstados[producao][0])   # Adicona um na contagem
        return len(set(list(self.Estados) + novasProducoes))        # E retorna a quantidade. Utiliza lista para tratar repetições


    # -- Retorna a produção que está na lista de estados novos a partir de uma produção do automato
    def pegarProducaoOriginal(self, producaoOrig):
        retorno = list(set(producaoOrig))
        for producao in self.NovosEstados:
            for prod in producaoOrig:
                if self.NovosEstados[producao][0] == prod:
                    retorno = list(set(self.NovosEstados[producao][1]))

        return retorno


    # -- Verifica se uma produção dada está no conjunto de novos estados
    def existeNovoEstado(self, producao):
        if len(self.NovosEstados) > 0:
            for producaoAgrupada in self.NovosEstados:
                if self.NovosEstados[producaoAgrupada][0] == producao:
                    return True

        return False
