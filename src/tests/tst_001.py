from src.functions.Functions import Functions as Selenium
import unittest

class test_001(Selenium, unittest.TestCase):
    def setUp(self):
        Selenium.abrir_navegador(self)
    
    def test_001(self):
        self.Variable_A=50
        self.Variable_B=50
        self.RESULTADO=self.Variable_A+self.Variable_B

        self.assertTrue(self.RESULTADO>=100,f'El valor no es 10')
    
    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()