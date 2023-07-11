from huffmanbinarytree import HuffmanBinaryTree
from huffmandecoding import HuffmanDecoding

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        self.tree = None
        self.table = None
        self.summary = None

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        # Construir el árbol de Huffman
        frequency = {}
        for char in text:
            frequency[char] = frequency.get(char, 0) + 1
        nodes = []
        for key, value in frequency.items():
            node = HuffmanBinaryTree()
            node.key = (value, key)
            nodes.append(node)
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.key[0])
            left = nodes[0]
            right = nodes[1]
            parent = HuffmanBinaryTree()
            parent.key = (left.key[0] + right.key[0], None)
            parent.left = left
            parent.right = right
            nodes = nodes[2:]
            nodes.append(parent)
        self.tree = nodes[0]

        # Generar la tabla de codificación
        self.table = {}
        self.generate_table(self.tree, "")

        # Codificar el texto
        encoded_text = ""
        for char in text:
            encoded_text += self.table[char]
        return encoded_text

    def generate_table(self, node, code):
        """
        Genera la tabla de codificación recursivamente.
        :param node: nodo actual
        :param code: código actual
        """
        if node.key[1] is not None:
            self.table[node.key[1]] = code
        else:
            self.generate_table(node.left, code + "0")
            self.generate_table(node.right, code + "1")

    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        return self.tree

    def getTable(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        return self.table

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        raise NotImplementedError("Aún no implementado")
    

# Crear una instancia de HuffmanCoding
huffman = HuffmanCoding()

# Codificar un texto
texto_original = "mi pasion es programar"  
texto_codificado = huffman.encode(texto_original)

# Imprimir el texto codificado
print("Texto original:", texto_original)
print("Texto codificado:", texto_codificado)

# Obtener el árbol de Huffman y la tabla de codificación
arbol_huffman = huffman.getTree()
tabla_codificacion = huffman.getTable()
#tabla_resumen = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion.items():
    print(simbolo, ":", codigo)

# Imprimir resumen
#print(tabla_resumen)

# Crear una instancia de HuffmanDecoding
decodificador = HuffmanDecoding()

# Decodificar el texto
texto_decodificado = decodificador.decode(texto_codificado, arbol_huffman)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado)