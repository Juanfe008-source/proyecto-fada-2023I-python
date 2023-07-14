class HuffmanDecoding:
    """
    Clase HuffmanDecoding
    Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
    Autor: <Juan Felipe Alarcon
            Sergio Estrada castro
            Jean Carlo Enriquez
            Luis Miguel parra>
    Version: <1>
    """
    def __init__(self):
        pass

    def decode(self, text, tree):
        """
        Decodifica un texto en base a un árbol de Huffman.
        :param text: texto a decodificar
        :param tree: árbol de Huffman
        :return: texto decodificado
        """
        decoded_text = ""
        node = tree
        for bit in text:
            if bit == "0":
                node = node.left
            elif bit == "1":
                node = node.right
            if node.key[1] is not None:
                decoded_text += node.key[1]
                node = tree
        return decoded_text
