from src.functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome

class Functions(Inicializar):
    #############################################
    ########### INICIALIZAR DRIVERS #############
    def abrir_navegador(self,URL=Inicializar.URL,navegador=Inicializar.NAVEGADOR):
        print('*+*+*+**+*+*+**+*+*+**+*+*+**+*+*+**+*+*+**+*+*+*')
        print(Inicializar.basedir)
        print('*+*+*+**+*+*+**+*+*+**+*+*+**+*+*+**+*+*+**+*+*+*')
        self.ventanas={}
        print('-------------')
        print(navegador)
        print('-------------')

        if navegador==('IExplorer'):
            caps=DesiredCapabilities.INTERNETEXPLORER.copy()
            caps['platform']='WINDOWS'
            caps['browserName']='internet explorer'
            caps['ignoreZoomSetting']=True
            caps['requireWindowFocus']=True
            caps['nativeEvents']=True
            self.driver=webdriver.Ie(Inicializar.basedir+"\\drivers\\IEDriverServer.exe",caps)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal=self.driver.window_handles[0]
            self.ventanas={'Principal':self.driver.window_handles[0]}
            self.nWindows=0
            return self.driver
