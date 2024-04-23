import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from Utilidades.Utilidades import abrirPagina


class ConfigWebDriver(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(r"C:\Users\jose.velasquez\Desktop\Drivers\geckodriver.exe")
        self.driver = webdriver.Firefox(service=service)
        self.driver.implicitly_wait(5)
        abrirPagina(self.driver)


    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
