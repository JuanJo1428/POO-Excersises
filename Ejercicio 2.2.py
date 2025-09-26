from enum import Enum

class TipoPlaneta(Enum):
    
    Gaseoso = 1
    Terrestre = 2
    Enano = 3


class Planeta():
    
    def __init__(self,Nombre = "",Satelites = 0, Masa = 0, Volumen = 0, Diametro = 0, DistanciaSol = 0, TipoPlaneta = TipoPlaneta, Observable = False):
        
        self.Nombre = Nombre
        self.Satelites = Satelites
        self.Masa = Masa
        self.Volumen = Volumen
        self.Diametro = Diametro
        self.DistanciaSol = DistanciaSol
        self.TipoPlaneta = TipoPlaneta
        self.Observable = Observable
        
    def CalcularDensidad(self):
            
        return (self.Masa / self.Volumen)
        
        
    def Imprimir(self):
        
        print(f"""
Nombres del Planeta: {self.Nombre}.
Número de Satelites a su alrededor: {self.Satelites}.
Masa del Planeta: {self.Masa}.
Volumen del Planeta: {self.Volumen}.
Diametro del Planeta: {self.Diametro}.
La distancia a la que esta el Planeta del Sol: {self.DistanciaSol}.
Tipo de  Planeta: {self.TipoPlaneta.name}.
¿Es observable el Planeta?: {self.Observable}
""")
        
    def PlanetaExterior(self):
        
        Limite = float(149597870 * 3.4)
        
        return self.DistanciaSol > Limite
             
             
class Ejercicio22():
    
    def main():
        
        P1 = Planeta("Jupiter", 4, 450, 7890,80,345678,TipoPlaneta.Gaseoso,True)
        P1.Imprimir()
        print(f"La densidad del Planeta es: {P1.CalcularDensidad()}")
        print(f"¿Es un Planeta Exterior: {P1.PlanetaExterior()}\n")
            
            
        P2 = Planeta("Marte",7,467,786,46,34567,TipoPlaneta.Enano,True)
        P2.Imprimir()
        print(f"La densidad del Planeta es: {P2.CalcularDensidad()}")
        print(f"¿Es un Planeta Exterior: {P2.PlanetaExterior()}\n")
        

if __name__ == "__main__":
    
    Ejercicio22.main()
    
            

