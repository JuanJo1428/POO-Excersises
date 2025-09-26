import math

class Circulo:

    def __init__(self, Radio: int):
        self.Radio = Radio

    def calcularAreaC(self):
        return math.pi * pow(self.Radio, 2)

    def calcularPerimetroC(self):
        return 2 * math.pi * self.Radio


class Rectangulo:

    def __init__(self, Base: int, Altura: int):
        self.Base = Base
        self.Altura = Altura

    def calcularAreaR(self):
        return self.Base * self.Altura

    def calcularPerimetroR(self):
        return 2 * (self.Base + self.Altura)


class Cuadrado:

    def __init__(self, Lado: int):
        self.Lado = Lado

    def calcularAreaCD(self):
        return pow(self.Lado,2)

    def calcularPerimetroCD(self):
        return 4 * self.Lado


class TrianguloRectangulo:

    def __init__(self, Base: int, Altura: int):
        self.Base = Base
        self.Altura = Altura

    def calcularAreaT(self):
        return (self.Base * self.Altura) / 2

    def calcularHipotenusa(self):
        return math.sqrt( pow(self.Base, 2) +  pow(self.Altura, 2))

    def calcularPerimetroT(self):
        return self.Base + self.Altura + self.calcularHipotenusa()

    def determinar_tipo_triangulo(self):
        
        Hipotenusa = self.calcularHipotenusa()
        
        if self.Base == self.Altura == Hipotenusa:
            print("Tipo: Es un triángulo de tipo equilátero.")
            
        elif self.Base != self.Altura and self.Base != Hipotenusa and self.Altura != Hipotenusa:
            print("Tipo: Es un triángulo de tipo escaleno.")
            
        else:
            print("Tipo: Es un triángulo de tipo isósceles.")


class PruebaFiguras:

    @staticmethod
    def main():
        figura1 = Circulo(2)
        figura2 = Rectangulo(1, 2)
        figura3 = Cuadrado(3)
        figura4 = TrianguloRectangulo(3, 5)

        print("\nFigura 1:")
        print(f"El área del círculo es = {figura1.calcularAreaC()}")
        print(f"El perímetro del círculo es = {figura1.calcularPerimetroC()}\n")

        print("\nFigura 2:")
        print(f"El área del rectángulo es = {figura2.calcularAreaR()}")
        print(f"El perímetro del rectángulo es = {figura2.calcularPerimetroR()}\n")

        print("\nFigura 3:")
        print(f"El área del cuadrado es = {figura3.calcularAreaCD()}")
        print(f"El perímetro del cuadrado es = {figura3.calcularPerimetroCD()}\n")

        print("\nFigura 4:")
        print(f"El área del triángulo es = {figura4.calcularAreaT()}")
        print(f"El perímetro del triángulo es = {figura4.calcularPerimetroT()}")
        figura4.determinar_tipo_triangulo()


if __name__ == "__main__":
    
    PruebaFiguras.main()
