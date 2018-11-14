import sys

sys.path.append('./afd')
sys.path.append('./lex')

from Analisador import Analisador

analisador = Analisador()
analisador.analisar('./codigo.in') 
