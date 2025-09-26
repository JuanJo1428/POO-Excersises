class Persona():
    
    def __init__(self,Nombre: str,Apellidos: str,NumerodeIdentificación: str,AñoNacimiento: int):
        
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.NumerodeIdentificación = NumerodeIdentificación
        self.AñoNacimiento = AñoNacimiento
    
    def Imprimir(self):
        
        print(f"""
Nombres de la Persona: {self.Nombre}.
Apellidos de la Persona: {self.Apellidos}.
Número de Identificación de la Persona: {self.NumerodeIdentificación}.
Año de Nacimiento de la Persona: {self.AñoNacimiento}
""")
    
class Ejercicio21:

    def main():
        
        Persona1 = Persona("Juan","Vasquez","1015189591",2008)
        Persona2 = Persona("Walter","Arboleda","43201665",1990)
    
        Persona1.Imprimir()
        Persona2.Imprimir()
        
if __name__ == "__main__":
    
    Ejercicio21.main()
