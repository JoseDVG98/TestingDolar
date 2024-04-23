from Pagina.DolarHistorico import HistoricoDolar
from Pagina.PaginaDolar import BuscarDolar
from Utilidades.Config import ConfigWebDriver


class EvaluarPaginaHistorico(ConfigWebDriver):


    def test_buscarHistorico(self):
        historico=HistoricoDolar('2024-1-1', self.driver)

        #historico.escogerFecha()
        #historico.escribirFecha()
        historico.irHistorico()

        historico.buscarFecha()

        historico.submit()

        dolar = BuscarDolar(self.driver).valorDolar()

        self.assertEqual('3,800.00', dolar)






