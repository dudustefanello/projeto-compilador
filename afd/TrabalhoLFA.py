from EpsilonTransicao import EpsilonTransicao       # Importa a implementação da eliminação de épsilon transições
from Determinizacao import Determinizacao           # Importa a implementação da determinização
from Inalcancaveis import Inalcancaveis             # Importa a implementação da remoção de inalcançáveis
from Automatos import Automato                      # Importa as implementações gerais do automato
from Mortos import Mortos                           # Importa a implementação de remoção de mortos

automato = Automato()                               # Instancia a classe Automato
automato.carrega('liguagem.txt')                    # Carrega o automato a partir do arquivo de texto
automato.imprimir('\n\n# AUTOMATO LIDO:\n', True)   # Imprime automato lido

livreEpsilon = EpsilonTransicao(automato)           # Instancia o objeto para remover epsilons transicões
livreEpsilon.eliminarEpsilonTransicoes()            # Busca as épsilon transições e trata as mesmas
livreEpsilon.imprimir()                             # Imprimir automato livre de épsilon transições

determinizado = Determinizacao(automato)            # Instancia o objeto para determinização
determinizado.determinizar()                        # Faz a determinização do autômato
determinizado.imprimir()                            # Imprimir automato determinizado

semInalcancaveis = Inalcancaveis(automato)          # Instancia o objeto para remover estados inalcançáveis
semInalcancaveis.removerInalcancaveis()             # Remove os estados inalcançáveis
semInalcancaveis.imprimir()                         # Imprimir automato final

semMortos = Mortos(semInalcancaveis)                # Instancia o objeto para remover estados mortos
semMortos.removerMortos()                           # Remove os estados mortos
semMortos.imprimir()                                # Imprime automato minimizado


