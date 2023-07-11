class HuffmanBinaryTree:
  """
  Clase que implementa un árbol binario de Huffman
  Autor:<Estudiantes>
  """ 
  def __init__(self):
    """
    Constructor de la clase
    """
    self.key = None
    self.left = None
    self.right = None

  def getNumberKey(self):
    """
    Retorna el valor de la llave, 
    si es un string retorna -1, si es un 
    numero retorna el numero.
    """
    if isinstance(self.key, str):
        return -1
    return self.key

  def getLeft(self):
    """
    Retorna el hijo izquierdo del arbol.
    """
    return self.left

  def getRight(self):
    """
    Retorna el hijo derecho del arbol.
    """
    return self.right
  
  def traverse(self):
    """
    Realiza un recorrido en profundidad del árbol
    e imprime los nodos y sus conexiones.
    """
    self._traverse_helper(self, "")

  def _traverse_helper(self, node, indent):
    """
    Función auxiliar para realizar el recorrido en profundidad.
    """
    if node is not None:
        print(indent + str(node.getNumberKey()))
        print(indent + "├─ Left:")
        self._traverse_helper(node.getLeft(), indent + "│  ")
        print(indent + "└─ Right:")
        self._traverse_helper(node.getRight(), indent + "   ")  