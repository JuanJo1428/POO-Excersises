import tkinter as tk
from tkinter import messagebox
import math


# ---------------- CLASE BASE ----------------
class FiguraGeometrica:
    
    def __init__(self, Volumen: float = 0, Superficie: float = 0):
        self.Volumen = Volumen
        self.Superficie = Superficie
        
    def setVolumen(self, volumen):
        self.Volumen = volumen
        
    def setSuperficie(self, superficie):
        self.Superficie = superficie

    def getVolumen(self):
        return self.Volumen
    
    def getSuperficie(self):
        return self.Superficie
    

# ---------------- CLASE CILINDRO ----------------
class Cilindro(FiguraGeometrica):
    
    def __init__(self, Entradas, Resultados):
        
        super().__init__()
        self.Entradas = Entradas
        self.Resultados = Resultados

    def CalcularVolumenC(self):
        
        RadioC = float(self.Entradas[0].get())
        AlturaC = float(self.Entradas[1].get())
        Volumen = math.pi * AlturaC * pow(RadioC, 2.0)
        return Volumen
    
    def CalcularSuperficieC(self):
        
        RadioC = float(self.Entradas[0].get())
        AlturaC = float(self.Entradas[1].get())
        AreaLadoA = 2.0 * math.pi * RadioC * AlturaC
        AreaLadoB = 2.0 * math.pi * pow(RadioC, 2.0)
        return AreaLadoA + AreaLadoB
    
    def Calcular(self):
        
        try:
            Superficie = self.CalcularSuperficieC()
            Volumen = self.CalcularVolumenC()
            self.Resultados.config(
                text="Resultados Buscados:\n\n"
                f"Superficie: {Superficie:.2f}\n"
                f"Volumen: {Volumen:.2f}\n"
            )
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            

# ---------------- CLASE ESFERA ----------------
class Esfera(FiguraGeometrica):
    
    def __init__(self, Entrada, Resultados):
        
        super().__init__()
        self.Entrada = Entrada
        self.Resultados = Resultados
        
    def CalcularVolumenE(self):
        
        RadioE = float(self.Entrada.get())
        Volumen = (4/3) * math.pi * pow(RadioE, 3.0)
        return Volumen
    
    def CalcularSuperficieE(self):
        
        RadioE = float(self.Entrada.get())
        Superficie = 4.0 * math.pi * pow(RadioE, 2.0)
        return Superficie
    
    def Calcular(self):
        
        try:
            Superficie = self.CalcularSuperficieE()
            Volumen = self.CalcularVolumenE()
            self.Resultados.config(
                text="Resultados Buscados:\n\n"
                f"Superficie: {Superficie:.2f}\n"
                f"Volumen: {Volumen:.2f}\n"
            )
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


# ---------------- CLASE PIRÁMIDE ----------------
class Piramide(FiguraGeometrica):
    
    def __init__(self, Entradas, Resultados):
        
        super().__init__()
        self.Entradas = Entradas
        self.Resultados = Resultados
        
    def CalcularVolumenP(self):
        
        BaseP = float(self.Entradas[0].get())
        AlturaP = float(self.Entradas[1].get())
        Volumen = (pow(BaseP, 2.0) * AlturaP) / 3.0
        return Volumen
    
    def CalcularSuperficieP(self):
        
        BaseP = float(self.Entradas[0].get())
        Apotema = float(self.Entradas[2].get())
        AreaBaseP = pow(BaseP, 2.0)
        AreaLadoP = 2.0 * BaseP * Apotema
        return AreaBaseP + AreaLadoP
    
    def Calcular(self):
        
        try:
            Superficie = self.CalcularSuperficieP()
            Volumen = self.CalcularVolumenP()
            self.Resultados.config(
                text="Resultados Buscados:\n\n"
                f"Superficie: {Superficie:.2f}\n"
                f"Volumen: {Volumen:.2f}\n"
            )
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


# ---------------- VENTANA CILINDRO ----------------
class VentanaCilindro:
    
    def __init__(self):
        
        self.InterfazCilindro = tk.Toplevel()
        self.InterfazCilindro.title("Opción Cilindro")
        self.InterfazCilindro.geometry("350x400")
        
        self.Entradas = []
        self.FrameEntradas = tk.Frame(self.InterfazCilindro)
        self.FrameEntradas.pack(pady=10)

        tk.Label(self.InterfazCilindro, text="Ingrese el Radio:", font=("Arial",11,"italic")).pack()
        Entrada = tk.Entry(self.InterfazCilindro)
        Entrada.pack(pady=5)
        self.Entradas.append(Entrada)

        tk.Label(self.InterfazCilindro, text="Ingrese la Altura:", font=("Arial",11,"italic")).pack()
        Entrada = tk.Entry(self.InterfazCilindro)
        Entrada.pack(pady=5)
        self.Entradas.append(Entrada)

        self.Resultados = tk.Label(self.InterfazCilindro, text="Resultados Buscados:", font=("Arial",11,"bold italic"))
        self.Resultados.pack(pady=10)
        
        self.FrameBotones = tk.Frame(self.InterfazCilindro)
        self.FrameBotones.pack(pady=70)

        tk.Button(self.FrameBotones, text="Calcular", bg="lightgreen", font=("Arial", 10, "italic"),
                  command=self.Calcular).pack(side="left", padx=5)
        
        tk.Button(self.FrameBotones, text="Limpiar", bg="lightcoral", font=("Arial", 10, "italic"),
                  command=self.Limpiar).pack(side="left", padx=5)

    def Calcular(self):
        
        Figura = Cilindro(self.Entradas, self.Resultados)
        Figura.Calcular()

    def Limpiar(self):
        
        for e in self.Entradas:
            e.delete(0, tk.END)
        self.Resultados.config(text="Resultados Buscados:")


# ---------------- VENTANA ESFERA ----------------
class VentanaEsfera:
    
    def __init__(self):
        
        self.InterfazEsfera = tk.Toplevel()
        self.InterfazEsfera.title("Opción Esfera")
        self.InterfazEsfera.geometry("350x400")

        tk.Label(self.InterfazEsfera, text="Ingrese el Radio:", font=("Arial",11,"italic")).pack()
        self.Entrada = tk.Entry(self.InterfazEsfera)
        self.Entrada.pack(pady=10)

        self.Resultados = tk.Label(self.InterfazEsfera, text="Resultados Buscados:", font=("Arial",11,"bold italic"))
        self.Resultados.pack(pady=10)

        frame = tk.Frame(self.InterfazEsfera)
        frame.pack(pady=70)

        tk.Button(frame, text="Calcular", bg="lightgreen", font=("Arial", 10, "italic"),
                  command=self.Calcular).pack(side="left", padx=5)
        
        tk.Button(frame, text="Limpiar", bg="lightcoral", font=("Arial", 10, "italic"),
                  command=self.Limpiar).pack(side="left", padx=5)

    def Calcular(self):
        
        Figura = Esfera(self.Entrada, self.Resultados)
        Figura.Calcular()

    def Limpiar(self):
        
        self.Entrada.delete(0, tk.END)
        self.Resultados.config(text="Resultados Buscados:")


# ---------------- VENTANA PIRÁMIDE ----------------
class VentanaPiramide:
    
    def __init__(self):
        
        self.InterfazPiramide = tk.Toplevel()
        self.InterfazPiramide.title("Opción Pirámide")
        self.InterfazPiramide.geometry("350x400")

        self.Entradas = []
        self.FrameEntradas = tk.Frame(self.InterfazPiramide)
        self.FrameEntradas.pack(pady=10)

        for texto in ["Ingrese la Base:", "Ingrese la Altura:", "Ingrese el Apotema:"]:
            
            tk.Label(self.InterfazPiramide, text=texto, font=("Arial",11,"italic")).pack()
            Entrada = tk.Entry(self.InterfazPiramide)
            Entrada.pack(pady=5)
            self.Entradas.append(Entrada)

        self.Resultados = tk.Label(self.InterfazPiramide, text="Resultados Buscados:", font=("Arial",11,"bold italic"))
        self.Resultados.pack(pady=10)
        
        self.FrameBotones = tk.Frame(self.InterfazPiramide)
        self.FrameBotones.pack(pady=40)

        tk.Button(self.FrameBotones, text="Calcular", bg="lightgreen", font=("Arial", 10, "italic"),
                  command=self.Calcular).pack(side="left", padx=5)
        
        tk.Button(self.FrameBotones, text="Limpiar", bg="lightcoral", font=("Arial", 10, "italic"),
                  command=self.Limpiar).pack(side="left", padx=5)

    def Calcular(self):
        
        Figura = Piramide(self.Entradas, self.Resultados)
        Figura.Calcular()

    def Limpiar(self):
        
        for e in self.Entradas:
            e.delete(0, tk.END)
        self.Resultados.config(text="Resultados Buscados:")


# ---------------- VENTANA PRINCIPAL ----------------
class VentanaPrincipal:
    
    def __init__(self):
        
        self.VentanaPrincipal = tk.Tk()
        self.VentanaPrincipal.title("Figuras Geométricas")
        self.VentanaPrincipal.geometry("450x150")

        FrameBotones = tk.Frame(self.VentanaPrincipal)
        FrameBotones.pack(pady=52,padx=30)

        tk.Button(FrameBotones, text="Cilindro", bg="lightgreen", font=("Arial", 11, "bold italic"),
                  command=VentanaCilindro).pack(side="left", padx=10)
        
        tk.Button(FrameBotones, text="Esfera", bg="lightblue", font=("Arial", 11, "bold italic"),
                  command=VentanaEsfera).pack(side="left", padx=10)
        
        tk.Button(FrameBotones, text="Pirámide", bg="lightcoral", font=("Arial", 11, "bold italic"),
                  command=VentanaPiramide).pack(side="left", padx=10)

    def EjecutarApp(self):
        
        self.VentanaPrincipal.mainloop()


# ---------------- EJECUCIÓN PRINCIPAL ----------------
class Ejercicio83:
    
    @staticmethod
    def Principal():
        
        App = VentanaPrincipal()
        App.EjecutarApp()


if __name__ == "__main__":
    Ejercicio83.Principal()
