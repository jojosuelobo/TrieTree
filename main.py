class TrieNode:
    """Uma node na estrutura da trie"""

    def __init__(self, char):
        # O caracter dentro da node
        self.char = char

        # O caracter dentro da node
        self.is_end = False

        # Contador indicando quantas vezes a palavra foi inserida
        self.counter = 0

       # Chaves sao caracteres e valores sao as nodes
        self.children = {}
      
class Trie(object):
    """Objeto da Trie"""

    def __init__(self):
        """
        a Trie tem no minimo a root node.
        a root node nao guarda nenhum caractere
        """
        self.root = TrieNode("")
    
    def insert(self, word):
        """insere uma palavra na Trie"""
        node = self.root
        
        # Loop por cada caractere da palavra
        # Checa se nao existe uma child contendo o caracter, cria uma nova childNode para a node atual
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # Se o caractere nao foi encontrado, cria uma nova node na Trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # Marca o final de uma palavra
        node.is_end = True

        # Incrementa o contador para indicar que vemos essa palavra mais uma vez
        node.counter += 1
        
    def dfs(self, node, prefix):
        """Primeira travesia da Trie
        
        Args:
      - node: node que comeca
      - prefix: o atual prefixo, para delinear a palavra enquanto atravesa a Trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, x):
        """
        Dado um input (um prefixo), recupera todas palvras quardadas na Trie com esse prefixo organiza                as palavras pelo numero de vezes que foram inseridas
        """
        self.output = []
        node = self.root
        
        # checar se o prefixo esta na Trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # caso nao ache o prefixo, retorna uma lista vazia
                return []
        
        # Atravessa a Trie para pegar todos candidatos
        self.dfs(node, x[:-1])

        # Armazena resultado encontrado (List[]), na variavel "busca"
        return sorted(self.output, key=lambda x: x[1], reverse=True)

def procurar(pesquisa):
  # Armazena resultado encontrado (List[]), na variavel "busca"
  busca = t.query(pesquisa)
  print(f"\nResultados em sistema para: {pesquisa}")

  # Se Busca for vazio (null == []), significa que não foram retornados valores para a pesquisa
  # Ou seja, valor não conta na árvore
  if busca == []:
    print("> Não foram encontrado resultados para " + pesquisa)
  else:
    for resultado in busca:
      print(f"> ({resultado[1]}x) {resultado[0]}")

def procurarEspecifico(palavra):
  alarme = False
  # Armazena resultado encontrado (List[]), na variavel "busca"
  list = t.query(palavra)
  for resultado in list:
    # Checa item por item da list se é igual a palavra
    if resultado[0] == palavra:
      print(f"\nPalavra {palavra} consta em sistema.")
      alarme = True
  if alarme == False:
    print(f"\nPalavra {palavra} NÃO consta em sistema.")

# MAIN
t = Trie()
# Popula a árvoré com pré registros
t.insert("abrantes é professor de medicina")
t.insert("abrantes é professor de medicina")
t.insert("abrantes é professor de matematica")
t.insert("abrantes é professor de computação")
t.insert("abrantes é professor de arquitetura")
t.insert("abrantes é professor de filosofia")
t.insert("abrantes é professor de filosofia")
t.insert("abrantes é professor de filosofia") 
t.insert("abrantes")
t.insert("fred é um bobão")
#print(t.query("abrantes"))

# Condição de loop
condicao = True
while condicao == True:
  print("[1]: Inserir palavra | [2]: Consultar | [3]: Sair")
  opcao = input("-> ")
  if opcao == "1":
    palavra = input("Informe a palavra a ser inserida: ")
    t.insert(palavra.lower())
  if opcao == "2":
    palavra = input("Informe a palavra a ser consultada: ")
    procurarEspecifico(palavra.lower())
    procurar(palavra.lower())
  if opcao == "3":
    condicao = False
  else:
    print()
