# Ejercicio Número 17

import math 

class AL:
    
    @staticmethod
    def CalcularArea(Radio):
        Area = math.pi * pow(Radio, 2)
        return Area
    
    @staticmethod
    def CalcularLongitud(Radio):
        Longitud = 2 * math.pi * Radio 
        return Longitud
    
class Ejercicio_17:
    
    def ValoresCirculo():

        Radio = float(input("Ingrese el Radio del círuclo que desea calcular: "))

        AreaCirculo = AL.CalcularArea(Radio)
        Longitud = AL.CalcularLongitud(Radio)
        
        print(f"El Area del Círculo de radio {Radio} es de {AreaCirculo} y su longitud es de {Longitud}.")
        
    
Ejercicio_17.ValoresCirculo()

