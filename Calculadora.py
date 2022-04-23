class Calculadora:
    def __init__(self):
        self.__numero1=None
        self.__numero2=None
    
    @property
    def numero1(self):
        return self.__numero1
     
    @property
    def numero2(self):
        return self.__numero2
    
    @numero1.setter
    def numero1(self, numero1):
        self.__numero1=numero1

    @numero2.setter
    def numero2(self, numero2):
        self.__numero2=numero2
    
    def suma(self, n1, n2):
        return n1 + n2