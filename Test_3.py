from Pagina.DolarCalculadora import Calculadora
from Utilidades.Config import ConfigWebDriver


class EvaluarPaginaCalculadora(ConfigWebDriver):


    def test_calcular_peso_dolar(self):
        pag_calculadora = Calculadora(self.driver)
        pag_calculadora.irCalculadora()
        pag_calculadora.pesosAdolar()
        valor=pag_calculadora.calcular('50000')
        self.assertEqual("12.85",valor.split()[1])

    def test_calcular_dolar_peso(self):
        pag_calculadora = Calculadora(self.driver)
        pag_calculadora.irCalculadora()
        pag_calculadora.dolarApesos()
        valor = pag_calculadora.calcular('50000')
        self.assertEqual("12.85",valor.split()[1])


