Original disponível em https://github.com/laurivansareta/TrabalhoLFA.git

# Autômato finito determinístico quase mínimo livre de épsilon transições

**Eduardo Stefanello, Laurivan Sareta**

Universidade Federal da Fronteira Sul,  Rodovia SC 484 - Curso de Ciência da Computação

eduardo@stefanello.cc, laurivansareta@gmail.com

***Abstract.*** *The objective of this work was to implement the load of a finite automaton from a file with the relation of tokens and regular grammars of any language, the elimination of the epsilons transitions, determination and minimization (without the application of classes of equivalence) of this automaton.*

***Resumo.*** *O objetivo deste trabalho foi a implementação da carga de um autômato finito a partir de um arquivo com a relação de tokens e gramáticas regulares de uma linguagem qualquer, a eliminação das épsilons transições, determinização e minimização (sem a aplicação de classes de equivalência) desse autômato.*

## 1. Introdução.
De acordo com Hopcroft, em Teoria dos Autômato, um autômato finito determinístico é uma máquina de estados finita que tem a função de aceitar ou rejeitar cadeias de símbolos de uma determinada entrada.

Neste trabalho, a implementação buscou gerar um autômato a partir de um arquivo do arquivo de texto.

## 2. Método.
A aplicação foi desenvolvida em Python, por ser uma linguagem de propósito geral de alto nível e com estrutura simples.

A IDE utilizada foi a Microsoft Visual Studio, por ser uma ferramenta grátis e de fácil utilização, além de ser uma ótima ferramenta para debug.

A primeira etapa de desenvolvimento foi a carga inicial do autômato e inserindo numa estrutura de estados, a partir de um arquivo contendo apenas os tokens de uma linguagem.

A segunda etapa consistiu em fazer a leitura da gramática regular da linguagem, passada pelo mesmo arquivo, após os tokens e inserir os novos estados que foram criados pela gramática na mesma estrutura que já continha o autômato de reconhecimento dos tokens.

A próxima etapa consistiu em implementar o algoritmo de determinização do autômato, que continha diversos indeterminismos. Optamos por implementar primeiro a determinização pela sua prioridade em relação à eliminação das épsilons transições para a entrega do trabalho, apesar da segunda preceder a primeira em termos de aplicação prática.

Após a determinização, implementamos a eliminação de épsilons transições do autômato. Uma vez implementado, esse algoritmo é executado antes da determinização, pois pode gerar indeterminismos.

Por último, foi implementada a minimização, eliminando estamos mortos e inalcançáveis, o que fizemos através do conceito de busca em profundidade, da teoria dos grafos (TRÉMAUX, 1876).

## 3. Estruturas.
A estrutura utilizada para a gravação dos estados do autômato foi feita em uma estrutura de dicionário (dict(), Python) de estados; cada estado é um dicionário de transições, e cada transição contém uma lista (list(), Python) de estados.

Foi implementada uma lista de estados para poder inserir transições indeterminísticas, apesar do estado final não necessitar de tal estrutura para representar as mesmas transições.

Foi utilizada também a estrutura de conjunto (set(), Python), para representar o alfabeto da linguagem, além de outras necessidades em procedimentos do código. Foi escolhida essa estrutura por ela não permitir inserção de itens iguais e economizarmos o tratamento de verificar se o símbolo está ou não no alfabeto.

## 4. Indeterminismos.
Em teoria da computação, um autômato não determinístico é uma máquina de estados em que para cada par de estado e símbolo pode haver mais de um próximo estado possível, caracterizando uma linguagem computacionalmente irreconhecível.

M. O. Rabin  e D. Scott provaram pela primeira vez em 1959 que existe equivalência entre máquinas de estados determinísticas e não determinísticas, encontrando uma unicidade computacional.

## 5. Determinização.
A determinização do autômato foi a parte mais demorada deste trabalho, pois necessitou uma refatoração, já que a primeira implementação feita não respeitava todas as regras do teorema de Rabin e Scott para determinização

O algoritmo de minimização desse trabalho segue a sequência básica de encontrar um determinismo, criar um novo estado, substituir o indeterminismo pelo novo estado em todos os lugares onde ele aparecer e armazenar as informações dessa troca, para posteriormente poder fazer a mesma troca quando o mesmo indeterminismo aparecer no decorrer do processo.

A refatoração citada foi necessária pois na primeira implementação não armazenávamos o indeterminismo e o estado utilizado para substituí-lo, então no decorrer da execução do algoritmo, um indeterminismo já tratado anteriormente voltava a aparecer e o programa criava um novo estado sem necessidade.

## 6. Épsilon Transição.
Uma épsilon transição é caracterizada por transições em que é possível passar de um estado para outro sem consumir nenhum caractere da entrada da linguagem.

M. O. Rabin  e D. Scott provaram pela primeira vez em 1959 que existe equivalência entre máquinas de estados determinísticas e não determinísticas, encontrando uma unicidade computacional.

## 7. Remoção de Épsilon Transição.
Uma vez encontrada uma épsilon transição, ela deve ser removida para otimizar o processo de reconhecimento.

Nossa implementação remove as épsilons transições da seguinte forma: encontrada uma épsilon transição no estado hipotético ‘S’ para o estado ‘A’:

  1. O programa substitui em ‘S’ a transição para ‘A’ por todas as transições de ‘A’.
  2. Havendo num estado hipotético ‘B’, uma transição para ‘S’ por um símbolo     hipotético ‘x’ da linguagem, deverá ser adicionado em ‘B’ uma transição para ‘A’, através do mesmo símbolo ‘x’
  3. Se o estado ‘A’ for um estado final, então o estado ‘S’ também deverá ser final.

No cenário descrito acima, no item 2 o algoritmo gerará um indeterminismo em ‘B’ pelo símbolo ‘x’ e é por isso que no programa final, a eliminação de épsilon transição deve ser executada antes da determinização.

## 8. Minimização do Autômato.
Na minimização de um autômato devem ser entendidos três conceitos importantes:

  - **Estados Mortos:** São os estados que jamais alcançam um estado final, por isso também são chamados de estados armadilha;
  - **Estados Inalcançáveis:** São os estados que nunca se pode alcançar partindo do estado inicial;
  - **Estados Indistinguíveis:** São conjuntos de estados que são iguais entre si. Não foi necessário eliminar os estados indistinguíveis do autômato para esse trabalho.

Um autômato mínimo não tem nenhuma das situações descritas acima. Como não foi necessário eliminar a última situação, nosso autômato gerado não é mínimo de fato, por isso foi chamado que “quase mínimo” no título deste artigo.

## 9. Remoção de Mortos e Inalcançáveis.
O algoritmo implementado para esse trabalho, utiliza o conceito de busca em profundidade, percorrendo o autômato de forma semelhante à como se busca um nodo em um grafo e identificando os estados mortos e inalcançáveis.

Tomando a analogia do autômato como um grafo, cada estado pode ser representao como um vértice, cada um desses vértices pode ter _n_ arestas, que podem ser entendidas como as transições do autômato finito determinístico.

Não seria possível concluir a mesma analogia antes da determinização do autômato, já que por uma transição apenas, um autômato não determinístico pode atingir vários outros estados, situação que não existe em grafos, pois uma aresta liga apenas um vértice a outro.

### 9.1 Remoção de Inalcançáveis
Na remoção de estados inalcançáveis, a busca em profundidade percorre todos os estados, passando por todas as suas transições de uma e adicionando cada estado visitado em uma nova estrutura, semelhante a estrutura inicial do autômato.

Foi necessária a implementação dessa nova estrutura pois no processo de minimização ocorriam erros ao tentar alterar a estrutura do autômato dentro da recurssão. Ao final do processo o autômato final está em uma estrutura diferente do automato simplesmente determinizado.

### 9.2 Remoção de Mortos
Na remoção de estados mortos, a busca em profundidade percorre o autômato o quanto for possível, partindo de cada um dos estado alcançáveis.

Se a BFS chegar à um estado onde todas os estados de suas transições já foram visitados, ou chegar à um estado final, o algoritmo mantém o estado no autômato.  

### Referências
HOPCROFT, John E.; MOTWANI, Rajeev; ULLMAN, Jeffrey D. (2001). “Introduction to Automata Theory, Languages, and Computation” 2 ed. [S.l.]: Addison Wesley. ISBN 0-201-44124-1. Consultado em 19 de novembro de 2012.

TRÉMAUX, Charles Pierre (1859–1882) “École Polytechnique of Paris” (X:1876)
Conferência pública, 2 de dezembro de 2010 – pelo professor Jean Pelletier-Thibert na Académie de Macon (Borgonha – França) – (Abstrato publicado nos anais da Academia, Março de 2011 – ISSN: 0980-6032).

5\. Data Structures - Python 3.7.0 Documentation Disponível: https://docs.python.org/3/tutorial/datastructures.html.

M. O. Rabin and D. Scott, “Finite Automata and their Decision Problems”, IBM Journal of Research and Development, 3:2 (1959) pp. 115–125.

BERSTEL, Jean; BOASSON, Luc; CARTON, Olivier; FAGNOT, Isabelle (2010), “Minimization of Automata”, Automata: from Mathematics to Applications, European Mathematical Society, arXiv:1010.5318
