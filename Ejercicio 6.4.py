import tkinter as tk
from tkinter import messagebox

# -------------------- LÓGICA -------------------- #
class CalculosPromedio:
    def __init__(self, Entradas, Resultados):
        self.Entradas = Entradas
        self.Resultados = Resultados

    def getValores(self):
        try:
            self.Valores = [float(e.get()) for e in self.Entradas]
        except ValueError:
            raise ValueError("Debe ingresar solo valores numéricos.")

    def CalcularPromedio(self):
        return sum(self.Valores) / len(self.Valores)

    def Calcular(self):
        try:
            self.getValores()
            promedio = self.CalcularPromedio()
            self.Resultados.config(text=f"Resultado:\n\nPromedio: {promedio:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# -------------------- INTERFAZ -------------------- #
class InterfazPromedio:
    def __init__(self):
        self.Ventana = tk.Tk()
        self.Ventana.title("Ejercicio 6.4 – Promedio de tres números")
        self.Ventana.geometry("350x300")

        self.Entradas = []
        for i in range(3):
            tk.Label(self.Ventana, text=f"Número {i+1}:").pack()
            entrada = tk.Entry(self.Ventana)
            entrada.pack()
            self.Entradas.append(entrada)

        self.Resultados = tk.Label(self.Ventana, text="Resultado:", font=("Arial", 10, "bold italic"))
        self.Resultados.pack(pady=10)

        self.FrameBotones = tk.Frame(self.Ventana)
        self.FrameBotones.pack(pady=10)

        self.CalcularObj = CalculosPromedio(self.Entradas, self.Resultados)

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


class Ejercicio1:
    def Principal():
        app = InterfazPromedio()
        app.Ejecutar()


if __name__ == "__main__":
    Ejercicio1.Principal()