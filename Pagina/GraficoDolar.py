from selenium.webdriver.common.by import By
from Localizadores.Grafica import PagGrafica


class Graficador:

    def __init__(self, driver):
        self.driver=driver

    def irGrafica(self):
        seccion = self.driver.find_element(By.XPATH, PagGrafica.modulo)
        seccion.click()
    def fecha_inicio(self, fecha):
        calendario = self.driver.find_element(By.XPATH, PagGrafica.calendario_inicial)
        calendario.clear()
        calendario.send_keys(fecha)

    def fecha_fin(self, fecha):
        calendario = self.driver.find_element(By.XPATH, PagGrafica.calendario_final)
        calendario.clear()
        calendario.send_keys(fecha)

    def graficar(self):
        submit=self.driver.find_element(By.XPATH, PagGrafica.graficar)
        submit.click()
        grafica=self.driver.find_element(By.XPATH,PagGrafica.grafica)
        grafica.screenshot("grafica.png")