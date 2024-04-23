from selenium.webdriver.common.by import By
from Localizadores.Dolar import PagPrincDolar



class BuscarDolar:

    def __init__(self, driver):
        self.driver=driver

    def valorDolar(self):
        dolar = self.driver.find_element(By.XPATH, PagPrincDolar.valor)
        return dolar.text
