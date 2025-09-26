from enum import Enum

class TipoCombustible(Enum):
    
    Gasolina = 1
    Bioetanol = 2
    Diesel = 3
    GasNatural = 4
    
class TipoAutomovil(Enum):
    
    Cuidad = 1
    SubCompacto = 2
    Compacto = 3
    Familiar = 4
    Ejecutivo = 5
    SUV = 6
    
class TipoColor(Enum):
    
    Blanco = 1
    Negro = 2
    Rojo = 3
    Naranja = 4
    Amarillo = 5
    Verde = 6
    Azul = 7
    Violeta = 8 
    
class Automovil():
    
    def __init__(self, Marca: str, Modelo: int, Motor: int, TipoCombustible: TipoCombustible, TipoAutomovil: TipoAutomovil, NumeroPuertas: int, CantidadAsientos: int, VelocidadMaxima: int, Color: TipoColor, VelocidadActual: int):
        
        self.Marca = Marca
        self.Modelo = Modelo
        self.Motor = Motor
        self.TipoCombustible = TipoCombustible
        self.TipoAutomovil = TipoAutomovil
        self.NumeroPuertas = NumeroPuertas
        self.CantidadAsientos = CantidadAsientos
        self.VelocidadMaxima = VelocidadMaxima
        self.Color = Color
        self.VelocidadActual = VelocidadActual
        
    
    def getMarca(self):
        return self.Marca

    def getModelo(self):
        return self.Modelo

    def getMotor(self):
        return self.Motor

    def getNumeroPuertas(self):
        return self.NumeroPuertas

    def getCantidadAsientos(self):
        return self.CantidadAsientos

    def getVelocidadMaxima(self):
        return self.VelocidadMaxima

    def getColor(self):
        return self.Color

    def getVelocidadActual(self):
        return self.VelocidadActual

    
    def setMarca(self, Marca: str):
        self.Marca = Marca

    def setModelo(self, Modelo: int):
        self.Modelo = Modelo

    def setMotor(self, Motor: int):
        self.Motor = Motor

    def setNumeroPuertas(self, NumeroPuertas: int):
        self.NumeroPuertas = NumeroPuertas

    def setCantidadAsientos(self, CantidadAsientos: int):
        self.CantidadAsientos = CantidadAsientos

    def setVelocidadMaxima(self, VelocidadMaxima: int):
        self.VelocidadMaxima = VelocidadMaxima

    def setColor(self, Color: TipoColor):
        self.Color = Color

    def setVelocidadActual(self, VelocidadActual: int):
        self.VelocidadActual = VelocidadActual

    
    def Acelerar(self, incrementoVelocidad: int):
        if self.VelocidadActual + incrementoVelocidad < self.VelocidadMaxima:
            self.VelocidadActual += incrementoVelocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")


    def Desacelerar(self, decrementoVelocidad: int):
        if (self.VelocidadActual - decrementoVelocidad) > 0:
            self.VelocidadActual -= decrementoVelocidad
        else:
            print("\nNo se puede decrementar a una velocidad negativa.")


    def Frenar(self):
        self.VelocidadActual = 0


    def CalcularTiempoLlegada(self, distancia: int):
        if self.VelocidadActual > 0:
            return distancia / self.VelocidadActual
      

    def Imprimir(self):
        print("\n")
        print(f"Marca = {self.Marca}")
        print(f"Modelo = {self.Modelo}")
        print(f"Motor = {self.Motor}")
        print(f"Tipo de Combustible = {self.TipoCombustible.name}")
        print(f"Tipo de Automovil = {self.TipoAutomovil.name}")
        print(f"Número de puertas = {self.NumeroPuertas}")
        print(f"Cantidad de asientos = {self.CantidadAsientos}")
        print(f"Velocidad máxima = {self.VelocidadMaxima}")
        print(f"Color = {self.Color.name}")
        print(f"Velocidad actual = {self.VelocidadActual}")
   

class Ejercicio23:
    
    def main():
        Auto1 = Automovil("Ford", 2018, 3,TipoCombustible.Diesel, TipoAutomovil.Ejecutivo,5, 6, 250,TipoColor.Negro, 40)

        Auto1.Imprimir()
        Auto1.setVelocidadActual(100)
        print("\nPruebas de Velocidad: Velocidad actual =", Auto1.VelocidadActual)

        Auto1.Acelerar(20)
        print("\nVelocidad actual =", Auto1.VelocidadActual)

        Auto1.Desacelerar(50)
        print("\nVelocidad actual =", Auto1.VelocidadActual)

        Auto1.Frenar()
        print("\nVelocidad actual =", Auto1.VelocidadActual)

        Auto1.Desacelerar(20)


if __name__ == "__main__":

    Ejercicio23.main()
