#Ejercicio Número 5

import math

class CalculosSX:
    
    @staticmethod
    def CalcularSuma(SumaInicial, ValorX):
        
        Suma = SumaInicial + ValorX
        return Suma
    
    @staticmethod
    def CalcularX(ValorX,ValorY):
        
        x = ValorX + pow(ValorY, 2)
        return x
    
class Ejercicio_5:
    
    def Suma():   

        SumaInicial = float(input("Ingrese el valor inicial de la suma: "))
        ValorX = float(input("Ingrese el valor inicial de x: "))
        ValorY = float(input("Ingrese el valor inicial de y: "))

        Suma = CalculosSX.CalcularSuma(SumaInicial, ValorX) # Suma es igual a 20
        x = CalculosSX.CalcularX(ValorX, ValorY) # x va a ser igual 1620

        Suma = Suma + (x/ValorY) # Suma va a ser igual a "20 + (1620/40)" = 60.5
        
        print(f"\nEl valor de la suma es: {Suma}") 
    

Ejercicio_5.Suma()
