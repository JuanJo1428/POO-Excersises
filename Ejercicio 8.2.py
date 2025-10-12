import tkinter as tk #Librería con elementos para crear interfaces gráficas en python
from tkinter import messagebox
import math

#Clase que contiene las Funciones que se ejecuta al precionar el boton "Calcular"
class Calculos:
    
    def __init__(self, Entradas, Resultados):
        
        self.Entradas = Entradas
        self.Resultados = Resultados
        
    def getNotas(self):
        
        Notas = [float(Valores.get()) for Valores in self.Entradas]
        self.Notas = Notas
        
    def CalcularPromedio(self):
        
        Suma = 0
        for i in range(len(self.Notas)): 
            Suma += self.Notas[i]
            
        return Suma / (len(self.Notas))

    def CalcularDesviacion(self):
        
        Promedio = self.CalcularPromedio()
        Suma = 0
        for i in range(0, len(self.Notas)):
            Suma += math.pow(self.Notas[i] - Promedio, 2)
        return math.sqrt(Suma / (len(self.Notas)- 1))
    
    def NotaMaxima(self):
        
        return max(self.Notas)
        
    def NotaMinima(self):
        
        return min(self.Notas)
    
    def Calcular(self):
        
        try: 
            
            #Acceder a los valores númericos de las notas del estudiante ingresadas en los entry
            self.getNotas()
            
            #Valores que hay que calcular
            Promedio = self.CalcularPromedio()
            DesviacionEstandar = self.CalcularDesviacion() 
            NotaMaxima = self.NotaMaxima()
            NotaMinima = self.NotaMinima()
            
            #Para mostrar resultados de un label creado previamente en la extracción de entradas
            self.Resultados.config(
                text="Resultados Buscados:\n\n"
                f"Promedio: {Promedio:.2f}\n"
                    f"Desviación estándar: {DesviacionEstandar:.2f}\n"
                    f"Nota más alta: {NotaMaxima}\n"
                    f"Nota más baja: {NotaMinima}"
            )
            
        except ValueError:
            
            messagebox.showerror("Error en los valores ingresados", "Por favor, ingrese solo valores númericos.") 

            
class InterfazUsuario:            
    
    def __init__(self):
        
        self.VentanaPrincipal = tk.Tk()
        self.VentanaPrincipal.title("Notas del Estudiante")
        self.VentanaPrincipal.geometry("400x400")
        
        self.Entradas = []
        
        for i in range(5):
            
            tk.Label(self.VentanaPrincipal, text=f"Nota {i+1}:").pack()
            Entradas = tk.Entry(self.VentanaPrincipal)
            Entradas.pack()
            self.Entradas.append(Entradas)

        # Label de resultados (se pasa a BotonCalcular)
        self.Resultados = tk.Label(self.VentanaPrincipal, text="Resultados Buscados:", font=("Arial", 10, "bold italic"))
        self.Resultados.pack(pady=10)
        
        #Frame para organizar los botones
        self.FrameBotones = tk.Frame(self.VentanaPrincipal)
        self.FrameBotones.pack(pady=10)
        
        # Crear el objeto que realiza los cálculos
        self.BotonCalcular = Calculos(self.Entradas, self.Resultados)

        # Botón para ejecutar el cálculo
        BotonC = tk.Button(self.FrameBotones, text="Calcular" ,bg= "lightgreen", command=self.BotonCalcular.Calcular, font=("Arial", 10, "italic"))
        BotonC.pack(side= "left",pady=10, padx=8)

        BotonL = tk.Button(self.FrameBotones, text="Limpiar", bg="lightcoral", command=self.Limpiar, font=("Arial", 10, "italic"))
        BotonL.pack(side= "left", pady=10, padx=8)
    
    def Limpiar(self):
        
        for e in self.Entradas:
            
            e.delete(0, tk.END)
        
        self.Resultados.config(text="Resultados Buscados:")
    
    
    def Ejecutar(self):
        
        self.VentanaPrincipal.mainloop()


class Ejercicio82:
    
    # Programa principal
    def Principal():
            
            App = InterfazUsuario() #Instancia de la clase en una variable con la cual acceder a todos sus metodos y atributos
            App.Ejecutar()
        

if __name__ == "__main__":
    Ejercicio82.Principal()