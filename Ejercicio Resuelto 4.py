# Ejercicio Número 4

class Calculos:

    @staticmethod
    def CalcularAlberto(EdadJuan):
        EdadAlberto = (2/3)*EdadJuan
        
        return EdadAlberto

    @staticmethod
    def CalcularAna(EdadJuan):
        EdadAna = (4/3)*EdadJuan
        
        return EdadAna

    def CalcularMadre(EdadJuan, EdadAlberto, EdadAna):
        EdadMadre = EdadJuan + EdadAlberto + EdadAna
    
        return EdadMadre

class Ejercicio_4:
    
    def Edades():

        EdadJuan = float(input("¿Cuál es la edad de Juan?: "))

        EdadAlberto = Calculos.CalcularAlberto(EdadJuan)
        EdadAna = Calculos.CalcularAna(EdadJuan)
        EdadMadre = Calculos.CalcularMadre(EdadJuan, EdadAlberto, EdadAna)

        print(f"La Madre tiene {EdadMadre} años y sus hijos tienen:")
        print(f"Juan: {EdadJuan} años, Alberto: {EdadAlberto} años y Ana: {EdadAna} años.")


Ejercicio_4.Edades()

