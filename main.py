import unittest
from Test_1 import EvaluarPaginaDolar
from Test_2 import EvaluarPaginaHistorico
from Test_3 import EvaluarPaginaCalculadora
from Test_4 import EvaluarPaginaGrafica

if __name__ == '__main__':
    test_dolar = unittest.defaultTestLoader.loadTestsFromTestCase(EvaluarPaginaDolar)
    test_historico = unittest.defaultTestLoader.loadTestsFromTestCase(EvaluarPaginaHistorico)
    test_calculadora = unittest.defaultTestLoader.loadTestsFromTestCase(EvaluarPaginaCalculadora)
    test_grafica = unittest.defaultTestLoader.loadTestsFromTestCase(EvaluarPaginaGrafica)

    suit=unittest.TestSuite()
    suit.addTests(test_historico)
    runner=unittest.TextTestRunner(verbosity=2).run(suit)






