import tkinter as tk
from tkinter import messagebox

# -------------------- LÓGICA -------------------- #
class CalculosDivision:
    def __init__(self, Entradas, Resultados):
        self.Entradas = Entradas
        self.Resultados = Resultados

    def getValores(self):
        try:
            self.num = float(self.Entradas[0].get())
            self.den = float(self.Entradas[1].get())
        except ValueError:
            raise ValueError("Debe ingresar valores numéricos.")

    def Dividir(self):
        if self.den == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return self.num / self.den

    def Calcular(self):
        try:
            self.getValores()
            resultado = self.Dividir()
            self.Resultados.config(text=f"Resultado:\n\nDivisión: {resultado:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except ZeroDivisionError as e:
            messagebox.showerror("Error Matemático", str(e))


# -------------------- INTERFAZ -------------------- #
class InterfazDivision:
    def __init__(self):
        self.Ventana = tk.Tk()
        self.Ventana.title("Ejercicio 6.5 – División entre cero")
        self.Ventana.geometry("350x250")

        self.Entradas = []
        for i, label in enumerate(["Numerador:", "Denominador:"]):
            tk.Label(self.Ventana, text=label).pack()
            entrada = tk.Entry(self.Ventana)
            entrada.pack()
            self.Entradas.append(entrada)

        self.Resultados = tk.Label(self.Ventana, text="Resultado:", font=("Arial", 10, "bold"))
        self.Resultados.pack(pady=10)

        self.FrameBotones = tk.Frame(self.Ventana)
        self.FrameBotones.pack(pady=10)

        self.CalcularObj = CalculosDivision(self.Entradas, self.Resultados)

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


class Ejercicio2:
    def Principal():
        app = InterfazDivision()
        app.Ejecutar()


if __name__ == "__main__":
    Ejercicio2.Principal()