# algorithms
some raw algorithms topics in python - alguns conceitos básicos de algoritmos em python.
1 - Lista Ligada ou Linked List que pode ser usada para a criação de uma Fila(FIFO - Queue) ou Pilha(LIFO - Stack)-
Tudo é Grafo!!! mesmo a estrutura mais básica em algoritmo é um grafo...
o tipo e suas características, depois descobriremos....
voltando ao 1 tópico....Lista Ligada ou Linked List, que pode ser simples,duplamente ligada ou circular( DoubledLinkedList and  Cicled List):
Verdade que não é o objeto Lista que está ligado ou conectado, mas seus componentes ou elementos,os Nós ou Nodes;
e o resultado desse conjunto é a Lista Ligada que dependendo da ordem de inserção e retirada, como a ordem dos Nodes é acessado, serve como uma Fila ou uma Pilha.
Composição é o termo usado para construir esse objeto,
e o conhecimento prévio de POO( programação orientada à objetos) ajuda e muito,talvez essencial !!!
Então, vamos construir ou compor um objeto chamado de Lista Ligada, com outros objetos Nodes,
pois o acesso as informações desta Lista é feito por uma variável que adressa,
ou aponta (ponteiro ou pointer - Head da Lista!) para o 1° objeto da Lista,
que é 1° Node da Lista...pensem como uma corrente...
o próximo Node é acessado pelo, e somente pelo pointer do PRIMEIRO NODE (Node.next).
A partir do 2° Node, o acesso é pelo ponteiro do 1° Node...confuso? Não viu nada inocente !!!
Node é um objeto, definido por sua classe, Lista Ligada é outro objeto, definido por sua classe e composto de Nodes....
Lista ligada => sua Head => 1° Node => ponteiro ou pointer.next do 1° Node => 2° Node => pointer.next do 2° Node => 3° Node.....


