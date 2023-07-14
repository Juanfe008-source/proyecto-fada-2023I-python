from huffman.huffmanbinarytree import HuffmanBinaryTree
from huffman.huffmandecoding import HuffmanDecoding

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Juan Felipe Alarcon
            Sergio Estrada castro
            Jean Carlo Enriquez
            Luis Miguel parra>
    Version: <1>
    """
    def __init__(self):
        self.tree = None
        self.table = None
        self.summary = None
        self.text = None

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        self.text = text
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
        # Porcentaje de compresión
        total = self.count_characters(self.text)
        total2 = self.count_characters(self.encode(self.text))

        porcentaje_compresion = self.calculate_compression(total, total2)

        # Numero de nodos
        total_nodos_huffman = self.contar_nodos_huffman(self.tree)

        # Profundidad del arbol
        profundidad_arbol = self.obtener_profundidad_huffman(self.tree)

        # Construcción del resumen:
        summary = f"Total de caracteres: {total}\n"
        summary += f"Total de caracteres binarios: {total2}\n"
        summary += f"Porcentaje de compresión: {porcentaje_compresion}%\n"
        summary += f"Total de nodos del árbol de Huffman: {total_nodos_huffman}\n"
        summary += f"Profundidad del árbol de Huffman: {profundidad_arbol}\n"

        return summary
    
    def count_characters(self, text):
        """
        Cuenta el número total de caracteres en el texto.
        :param text: texto para contar los caracteres
        :return: número total de caracteres
        """
        contador = {}
        total_caracteres = 0
        for caracter in text:
            if caracter in contador:
                contador[caracter] += 1
            else:
                contador[caracter] = 1
            total_caracteres += 1
        return total_caracteres
    

    def calculate_compression(self, total_caracteres, total_caracteres_binarios):
        """
        Calcula el porcentaje de compresión.
        :param total_caracteres: número total de caracteres en el texto original
        :param total_caracteres_binarios: número total de caracteres en el texto codificado
        :return: porcentaje de compresión
        """
        valor1 = total_caracteres
        valor2 = valor1 * 256
        valor3 = total_caracteres_binarios
        Fc = (1 - (valor3 / valor2)) * 100
        FCR = round(Fc, 4)
        return FCR
    
    def contar_nodos_huffman(self, nodo):
        if nodo is None:
            return 0

        return 1 + self.contar_nodos_huffman(nodo.left) + self.contar_nodos_huffman(nodo.right)
    
    def obtener_profundidad_huffman(self, nodo):
        if nodo is None:
            return 0

        profundidad_izquierda = self.obtener_profundidad_huffman(nodo.left)
        profundidad_derecha = self.obtener_profundidad_huffman(nodo.right)

        return max(profundidad_izquierda, profundidad_derecha) + 1
    
# Crear una instancia de HuffmanCoding
huffman = HuffmanCoding()

# Codificar un texto
texto_original = """once upon a time, in a quiet little town nestled between hills and a river, lived a kind and gentle artist named leila. she loved to spend her days painting the serene landscapes and the people of her town. leila was well known for her captivating work, and people from far and wide would visit the town just to purchase her paintings.

one day, as leila was painting the town square, she noticed a young boy standing a few feet away. he watched as leila brush moved across the canvas, capturing the essence of the square. intrigued by the boy fascination, leila invited him to try his hand at painting.

the boy, whose name was eli, was initially hesitant. he confessed that he had never painted before and was afraid he would not be any good at it. leila reassured him, emphasizing that everyone has to start somewhere. she handed him a brush, and with a few strokes, eli began to paint.

days turned into weeks, and weeks into months. leila and eli spent many afternoons together, painting the picturesque town and its lively inhabitants. eli skills improved dramatically, and soon, he was creating art that was just as captivating as leila.

word spread about eli talent, and people flocked to see his work. leila was overjoyed to see eli succeed. she believed in the power of art and its ability to touch peoples hearts. she was pleased to have shared this passion with eli.

however, as years passed, leila grew old and frail. one day, she could not paint anymore. eli was heartbroken. he asked leila what he could do to help. leila, with a soft smile, told him to keep painting and sharing his art with the world.

so, eli did. he continued to paint and tell stories through his work, just as leila had taught him. he carried on her legacy, and the town tradition of art lived on. in a way, leila never truly left. her spirit lived on through eli paintings, in every stroke and splash of color.

in the end, the story of leila and eli is not just about art. it is about mentorship, about passing on ones knowledge and passion to another. it is about leaving a lasting impact on someones life. through her kindness and guidance, leila made a profound impact on eli life. and in return, eli ensured that leila love for art would continue to inspire others, long after she was gone.

"""

texto_codificado = huffman.encode(texto_original)

# Imprimir el texto codificado
print("Texto original:", texto_original)
print("Texto codificado:", texto_codificado)

# Obtener el árbol de Huffman, la tabla de codificación y la tabla de resumen
arbol_huffman = huffman.getTree()
tabla_codificacion = huffman.getTable()
tabla_resumen = huffman.getSummary()

# Imprimir el árbol de Huffman
print("\nÁrbol de Huffman:")
arbol_huffman.traverse()

# Imprimir la tabla de codificación
print("\nTabla de Codificación:")
for simbolo, codigo in tabla_codificacion.items():
    print(simbolo, ":", codigo)

# Crear una instancia de HuffmanDecoding
decodificador = HuffmanDecoding()

# Decodificar el texto
texto_decodificado = decodificador.decode(texto_codificado, arbol_huffman)

# Imprimir el texto decodificado
print("\nTexto decodificado:", texto_decodificado)

# Imprimir resumen
print("\nTabla de resumen:")
print(tabla_resumen)


