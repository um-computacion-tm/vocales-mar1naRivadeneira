import unittest 

#def contar_vocales(mi_string):
#   resultado = {}
#   for letra in mi_string:
#      if letra == 'a':
#         if 'a' not in resultado:
#             resultado['a'] = 0
#         resultado['a'] = resultado['a'] +1
# return resultado

def contar_vocales(mi_string):
    resultado = {}
    for letra in mi_string.lower():
        if letra in 'aeiou':
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado 




class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado,{})
        
class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado,{'a',1})
        
class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado,{'a',2})
        
class TestContarVocales(unittest.TestCase):
    def test_casa(self):
        resultado = contar_vocales('CASA')
        self.assertEqual(resultado,{'a',2})
        
def test_contar_bese(self):

        resultado = contar_vocales('bese')

        self.assertEqual(resultado, {'e': 2})

def test_contar_besa(self):

        resultado = contar_vocales('besa')

        self.assertEqual(resultado, {'a': 1, 'e': 1})

def test_contar_casanova(self):

        resultado = contar_vocales('casanova')

        self.assertEqual(resultado, {'a': 3, 'o': 1})

def test_contar_mUrciElago(self):

        resultado = contar_vocales('mUrciElago')

        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

class TestContarVocales(unittest.TestCase):
    def test_HOLA(self):
        resultado = contar_vocales('HOLA')
        self.assertEqual(resultado,{'a': 1, 'o': 1})
        
class TestContarVocales(unittest.TestCase):
    def test_CARpetA(self):
        resultado = contar_vocales('CARpetA')
        self.assertEqual(resultado,{'a': 2, 'e': 1})
        
class TestContarVocales(unittest.TestCase):
    def test_gUsaNO(self):
        resultado = contar_vocales('gUsaNO')
        self.assertEqual(resultado,{'a': 1, 'o': 1, 'u' : 1})
        
        


        


unittest.main()     

       