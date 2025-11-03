import tkinter as tk
from tkinter import messagebox
import math

# -------------------- LÓGICA -------------------- #
class CalculosRaiz:
    def __init__(self, Entradas, Resultados):
        self.Entradas = Entradas
        self.Resultados = Resultados

    def getValor(self):
        try:
            self.num = float(self.Entradas[0].get())
        except ValueError:
            raise ValueError("Debe ingresar un número válido.")

    def CalcularRaiz(self):
        if self.num < 0:
            raise ValueError("No se puede calcular la raíz de un número negativo.")
        return math.sqrt(self.num)

    def Calcular(self):
        try:
            self.getValor()
            resultado = self.CalcularRaiz()
            self.Resultados.config(text=f"Resultado:\n\nRaíz cuadrada: {resultado:.4f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# -------------------- INTERFAZ -------------------- #
class InterfazRaiz:
    def __init__(self):
        self.Ventana = tk.Tk()
        self.Ventana.title("Ejercicio 6.6 – Raíz cuadrada")
        self.Ventana.geometry("350x220")

        self.Entradas = []
        tk.Label(self.Ventana, text="Número:").pack()
        entrada = tk.Entry(self.Ventana)
        entrada.pack()
        self.Entradas.append(entrada)

        self.Resultados = tk.Label(self.Ventana, text="Resultado:", font=("Arial", 10, "bold"))
        self.Resultados.pack(pady=10)

        self.FrameBotones = tk.Frame(self.Ventana)
        self.FrameBotones.pack(pady=10)

        self.CalcularObj = CalculosRaiz(self.Entradas, self.Resultados)

        tk.Button(self.FrameBotones, text="Calcular", bg="lightgreen",
                  command=self.CalcularObj.Calcular, font=("Arial", 10, "italic")).pack(side="left", padx=8)
        tk.Button(self.FrameBotones, text="Limpiar", bg="lightcoral",
                  command=self.Limpiar, font=("Arial", 10, "italic")).pack(side="left", padx=8)

    def Limpiar(self):
        for e in self.Entradas:
            e.delete(0, tk.END)
        self.Resultados.config(text="Resultado:")

    def Ejecutar(self):
        self.Ventana.mainloop()


class Ejercicio3:
    def Principal():
        app = InterfazRaiz()
        app.Ejecutar()


if __name__ == "__main__":
    Ejercicio3.Principal()