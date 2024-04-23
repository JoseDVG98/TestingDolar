from time import sleep

from selenium.webdriver.common.by import By
from Localizadores.Grafica import PagGrafica
from Pagina.GraficoDolar import Graficador
from Utilidades.Config import ConfigWebDriver


class EvaluarPaginaGrafica(ConfigWebDriver):

    def test_grafica(self):
        pag_grafica=Graficador(self.driver)
        pag_grafica.irGrafica()
        sleep(3)
        pag_grafica.fecha_inicio("2024-02-01")
        sleep(3)
        pag_grafica.fecha_fin("2024-04-19")
        sleep(3)
        pag_grafica.graficar()
        sleep(3)



