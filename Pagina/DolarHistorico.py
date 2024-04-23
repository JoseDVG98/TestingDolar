from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.support.select import Select
from Pagina import PaginaDolar
from Localizadores.Historico import PagHistorico


class HistoricoDolar:

    meses={'Enero':'1',
           'Febrero':'2',
           'Marzo':'3',
           'Abril':'4',
           'Mayo':'5',
           'Junio':'6',
           'Julio':'7',
           'Agosto':'8',
           'Septiembre':'9',
           'Octubre':'10',
           'Noviembre':'11',
           'Diciembre':'12'
    }

    def __init__(self,fecha,driver):
        self.driver=driver
        self.fecha=fecha

    def irHistorico(self):
        seccion = self.driver.find_element(By.XPATH,PagHistorico.modulo)
        seccion.click()

    def submit(self):
        submit = self.driver.find_element(By.XPATH, PagHistorico.submit)
        submit.click()

    def escogerFecha(self):
        fecha=self.fecha.split("-")
        self.irHistorico()
        calendario=self.driver.find_element(By.XPATH, PagHistorico.calendario)
        calendario.click()
        fecha_mes_ano=self.driver.find_element(By.XPATH,PagHistorico.mesyano_calendario)
        fecha_mes_ano.click()
        ano=self.driver.find_element(By.XPATH, PagHistorico.ano_calendario.format(fecha[0]))
        #La pagina no tiene el año 2024 para escogerlo desde el calendario, por eso se deja la prueba hasta este punto

    def escribirFecha(self):
        self.irHistorico()
        calendario = self.driver.find_element(By.XPATH, PagHistorico.calendario)
        calendario.clear()
        calendario.send_keys(self.fecha)

    def buscarFecha(self):
        value=True
        fecha = self.fecha.split("-")
        calendario = self.driver.find_element(By.XPATH, PagHistorico.calendario)
        calendario.click()
        reversa=self.driver.find_element(By.XPATH, PagHistorico.reversa_calendario)
        while(value):
            fecha_cal=self.driver.find_element(By.XPATH, PagHistorico.mesyano_calendario)
            fecha_cal=fecha_cal.text.split()
            fecha_cal[0]=self.meses[fecha_cal[0]]
            print(fecha_cal)
            if fecha[0] == fecha_cal[1] and fecha[1] == fecha_cal[0]:
                dia = self.driver.find_element(By.XPATH,PagHistorico.dia_calendario.format(ano=fecha[0], mes=int(fecha[1])-1, dia=fecha[2]))
                dia.click()
                value = False
            else:
                print("evaluación-----------------------------------------------------------------",fecha)
                reversa.click()













