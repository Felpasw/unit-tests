from collections import Counter
import unittest
# comando para rodar  python -m unittest v02.py

if __name__ == '__main__':
        unittest.main()


class UtilitariosAnaliseTexto:

    def __init__(self, texto):
        self.texto = texto


    def contar_palavras_unicas(self):
        """Conta o número de palavras únicas na string."""
        return len(set(self.texto.lower().split()))

    def frequencia_caracteres(self):
        """Retorna a frequência de cada caractere em um dicionário, ignorando espaços."""
        caracteres = [char.lower() for char in self.texto if char.isalnum()]
        return dict(Counter(caracteres))

    def palavra_mais_longa(self):
        """Retorna a palavra mais longa na string. Em caso de empate, retorna a primeira."""
        palavras = self.texto.split()
        return max(palavras, key=len) if palavras else ""

    def detectar_palavras_chave(self, palavras_comuns=None):
        """Detecta as palavras-chave, ignorando palavras comuns (stopwords)."""
        if palavras_comuns is None:
            palavras_comuns = []  

        frequencia = self.frequencia_palavras()

        palavras_filtradas = {palavra: freq for palavra, freq in frequencia.items() 
                              if palavra.lower() not in [comum.lower() for comum in palavras_comuns]}

        palavras_ordenadas = sorted(palavras_filtradas.items(), key=lambda x: x[1], reverse=True)

        return dict(palavras_ordenadas)
    
    def frequencia_palavras(self):
        """Retorna a frequência de cada palavra na string."""
        palavras = self.texto.lower().split()
        return dict(Counter(palavras))

    def palavras_mais_comuns(self, n=3):
        """Retorna as `n` palavras mais comuns em um dicionário, incluindo suas frequências."""
        freq_dict = self.frequencia_palavras()
        palavras_ordenadas = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        return dict(palavras_ordenadas[:n])

    def eh_anagrama(self, palavra1, palavra2):
        """Verifica se duas palavras são anagramas entre si, ignorando maiúsculas/minúsculas."""
        return sorted(palavra1.lower()) == sorted(palavra2.lower())
    
    def fatores_primos(self, numero):
        """Verifica se um número é primo, ou seja, se tem exatamente 2 divisores."""
        if numero <= 1:
            return False  
    
        divisores = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1
    
        return divisores == 2  

    def prefixo_comum(self, lista_palavras):
        """Encontra o prefixo comum mais longo em uma lista de palavras."""
        if not lista_palavras:
            return ""
        palavra_curta = min(lista_palavras, key=len)
        for i, char in enumerate(palavra_curta):
            if any(palavra[i] != char for palavra in lista_palavras):
                return palavra_curta[:i]
        return palavra_curta




if __name__ == "__main__":
    unittest.main()



class TestesUnitarios(unittest.TestCase):

    def test_contar_palavras_unicas(self):
        txt = "a casa é bonita e a casa é grande"
        t = UtilitariosAnaliseTexto(txt)
        self.assertEqual(t.contar_palavras_unicas(), 6)  
        
    def test_frequencia_caracteres(self):
        t = UtilitariosAnaliseTexto("a b a c")
        
        resultado_esperado = {'a': 2, 'b': 1, 'c': 1}
        self.assertEqual(t.frequencia_caracteres(), resultado_esperado)

        t.texto = "a b a c"
        resultado_esperado = {'a': 2, 'b': 1, 'c': 1}
        self.assertEqual(t.frequencia_caracteres(), resultado_esperado)

        t.texto = "a, b! a."
        resultado_esperado = {'a': 2, 'b': 1}
        self.assertEqual(t.frequencia_caracteres(), resultado_esperado)

        t.texto = "AaBb"
        resultado_esperado = {'a': 2, 'b': 2}
        self.assertEqual(t.frequencia_caracteres(), resultado_esperado)

        t.texto = ""
        resultado_esperado = {}
        self.assertEqual(t.frequencia_caracteres(), resultado_esperado)

    def test_palavra_mais_longa(self):
        t = UtilitariosAnaliseTexto("a casa é bonita e grande")
        
        resultado_esperado = "bonita"
        self.assertEqual(t.palavra_mais_longa(), resultado_esperado)

        t.texto = "a casa é grande"
        resultado_esperado = "grande" 
        self.assertEqual(t.palavra_mais_longa(), resultado_esperado)

        t.texto = "única"
        resultado_esperado = "única"
        self.assertEqual(t.palavra_mais_longa(), resultado_esperado)

        t.texto = ""
        resultado_esperado = ""
        self.assertEqual(t.palavra_mais_longa(), resultado_esperado)

        t.texto = "abacaxi abacate abacaba"
        resultado_esperado = "abacaxi"  
        self.assertEqual(t.palavra_mais_longa(), resultado_esperado)
    
    def test_detectar_palavras_chave(self):
        texto = "a casa é bonita e a casa é grande e a casa está limpa"
        palavras_comuns = ["a", "é", "e", "está"]
        t = UtilitariosAnaliseTexto(texto)
        resultado_esperado = {'casa': 3, 'bonita': 1, 'grande': 1, 'limpa': 1}
        self.assertEqual(t.detectar_palavras_chave(palavras_comuns), resultado_esperado)

    
      
    def test_palavras_mais_comuns(self):
        t = UtilitariosAnaliseTexto("a casa é bonita e a casa é grande")
        
        resultado_esperado = {'a': 2, 'casa': 2, 'é': 2}  
        self.assertEqual(t.palavras_mais_comuns(), resultado_esperado)

        resultado_esperado = {'a': 2, 'casa': 2}
        self.assertEqual(t.palavras_mais_comuns(2), resultado_esperado)

        t.texto = "a a a a a"
        resultado_esperado = {'a': 5}
        self.assertEqual(t.palavras_mais_comuns(), resultado_esperado)

        t.texto = "a casa é bonita"
        resultado_esperado = {'a': 1, 'casa': 1, 'é': 1}  
        self.assertEqual(t.palavras_mais_comuns(), resultado_esperado)

        t.texto = ""
        resultado_esperado = {}
        self.assertEqual(t.palavras_mais_comuns(), resultado_esperado)
    
    def test_eh_anagrama(self):
        t = UtilitariosAnaliseTexto("")

        resultado_esperado = True
        self.assertEqual(t.eh_anagrama("listen", "silent"), resultado_esperado)

        resultado_esperado = False
        self.assertEqual(t.eh_anagrama("hello", "world"), resultado_esperado)

        resultado_esperado = True
        self.assertEqual(t.eh_anagrama("Listen", "Silent"), resultado_esperado)

        resultado_esperado = False
        self.assertEqual(t.eh_anagrama("hello", "helloo"), resultado_esperado)

        resultado_esperado = False
        self.assertEqual(t.eh_anagrama("", "nonempty"), resultado_esperado)

        resultado_esperado = True
        self.assertEqual(t.eh_anagrama("", ""), resultado_esperado)

    
    def test_fatores_primos(self):
        t = UtilitariosAnaliseTexto("")  

        self.assertTrue(t.fatores_primos(2))  
        self.assertTrue(t.fatores_primos(3))  
        self.assertTrue(t.fatores_primos(5))  
        self.assertTrue(t.fatores_primos(7))  
        self.assertTrue(t.fatores_primos(11))  

        
        self.assertFalse(t.fatores_primos(1))  
        self.assertFalse(t.fatores_primos(4))  
        self.assertFalse(t.fatores_primos(6))  
        self.assertFalse(t.fatores_primos(10))  
        self.assertFalse(t.fatores_primos(15))  

        
        self.assertFalse(t.fatores_primos(-7))  
    
    def test_prefixo_comum(self):
        t = UtilitariosAnaliseTexto("")

        resultado_esperado = "fl"
        self.assertEqual(t.prefixo_comum(["flower", "flow", "flight"]), resultado_esperado)

    

