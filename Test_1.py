import unittest

from Pagina.PaginaDolar import BuscarDolar
from Utilidades.Config import ConfigWebDriver


#class EvaluarPaginaDolar(ConfigWebDriver):
class EvaluarPaginaDolar(unittest.TestCase):

    def test_buscarEvaluar(self):
        valor_dolar=BuscarDolar(self.driver).valorDolar()
        self.assertEqual('3,764.23',valor_dolar)








