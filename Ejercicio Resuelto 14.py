# Ejercicio Número 14

class CC:
    
    @staticmethod
    def CalcularCuadrado(Numero):
        Cuadrado = pow(Numero, 2)
        return Cuadrado
    
    @staticmethod
    def CalcularCubo(Numero):
        Cubo = pow(Numero, 3)
        return Cubo
    

def Valores():
    
    Numero = float(input("Ingrese el Número del cual desea conocer su Cuadrado y su Cubo: "))

    Cuadrado = CC.CalcularCuadrado(Numero)
    Cubo = CC.CalcularCubo(Numero)
    
    print(f"El Cuadrado y el Cubo del número {Numero} son: Cuadrado: {Cuadrado}, Cubo: {Cubo}.")


Valores()

