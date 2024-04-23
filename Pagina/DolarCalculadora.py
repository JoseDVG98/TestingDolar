from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.support.select import Select
from Localizadores.Calculadora import PagCalculadora


class Calculadora:

    def __init__(self,driver):
        self.driver=driver

    def irCalculadora(self):
        seccion = self.driver.find_element(By.XPATH, PagCalculadora.modulo)
        seccion.click()

    def calcular(self,valor):
        input=self.driver.find_element(By.XPATH, PagCalculadora.input_valor)
        input.clear()
        input.send_keys(valor)
        submit=self.driver.find_element(By.XPATH, PagCalculadora.calcular)
        submit.click()
        valor=self.driver.find_element(By.XPATH, PagCalculadora.valor)
        time.sleep(10)
        return valor.text


    def dolarApesos(self):
        check=self.driver.find_element(By.XPATH,PagCalculadora.check_dolar_peso)
        check.click()

    def calendarioCalculadora(self):
        calendario = self.driver.find_element(By.XPATH, PagCalculadora.calendario)
        calendario.clear()
        calendario.send_keys(self.fecha)

    def pesosAdolar(self):
        check = self.driver.find_element(By.XPATH, PagCalculadora.check_peso_dolar)
        check.click()






