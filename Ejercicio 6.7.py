import tkinter as tk
from tkinter import messagebox

# -------------------- LÓGICA -------------------- #
class CalculosMultiCatch:
    def __init__(self, Entradas, Resultados):
        self.Entradas = Entradas
        self.Resultados = Resultados

    def getValores(self):
        try:
            self.a = int(self.Entradas[0].get())
            self.b = int(self.Entradas[1].get())
        except ValueError:
            raise ValueError("Debe ingresar números enteros.")

    def CalcularOperaciones(self):
        resultados = ""
        try:
            division = self.a / self.b
            resultados += f"División: {division:.2f}\n"
        except ZeroDivisionError:
            resultados += "División: Error (división por cero)\n"

        lista = [10, 20, 30]
        try:
            valor_lista = lista[self.b]
            resultados += f"Elemento lista[b]: {valor_lista}\n"
        except IndexError:
            resultados += "Elemento lista[b]: Error (índice fuera de rango)\n"

        resultados += f"Potencia a**b: {self.a ** self.b}\n"
        return resultados

    def Calcular(self):
        try:
            self.getValores()
            res = self.CalcularOperaciones()
            self.Resultados.config(text=f"Resultados:\n\n{res}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# -------------------- INTERFAZ -------------------- #
class InterfazMultiCatch:
    def __init__(self):
        self.Ventana = tk.Tk()
        self.Ventana.title("Ejercicio 6.7 – Múltiples excepciones")
        self.Ventana.geometry("400x300")

        self.Entradas = []
        for t in ["Valor A:", "Valor B:"]:
            tk.Label(self.Ventana, text=t).pack()
            e = tk.Entry(self.Ventana)
            e.pack()
            self.Entradas.append(e)

        self.Resultados = tk.Label(self.Ventana, text="Resultados:", font=("Arial", 10, "bold"), justify="left")
        self.Resultados.pack(pady=10)

        self.FrameBotones = tk.Frame(self.Ventana)
        self.FrameBotones.pack(pady=10)

        self.CalcularObj = CalculosMultiCatch(self.Entradas, self.Resultados)

        tk.Button(self.FrameBotones, text="Calcular", bg="lightgreen",
                  command=self.CalcularObj.Calcular, font=("Arial", 10, "italic")).pack(side="left", padx=8)
        tk.Button(self.FrameBotones, text="Limpiar", bg="lightcoral",
                  command=self.Limpiar, font=("Arial", 10, "italic")).pack(side="left", padx=8)

    def Limpiar(self):
        for e in self.Entradas:
            e.delete(0, tk.END)
        self.Resultados.config(text="Resultados:")

    def Ejecutar(self):
        self.Ventana.mainloop()


class Ejercicio4:
    def Principal():
        app = InterfazMultiCatch()
        app.Ejecutar()


if __name__ == "__main__":
    Ejercicio4.Principal()