import tkinter as tk
from tkinter import messagebox, filedialog

# -------------------- LÓGICA -------------------- #
class CalculosArchivos:
    def __init__(self, TextArea, Resultados):
        self.TextArea = TextArea
        self.Resultados = Resultados

    def GuardarArchivo(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Archivos de texto", "*.txt")])
        if not ruta:
            return
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self.TextArea.get("1.0", tk.END))
            self.Resultados.config(text=f"Archivo guardado:\n{ruta}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def LeerArchivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if not ruta:
            return
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            self.TextArea.delete("1.0", tk.END)
            self.TextArea.insert(tk.END, contenido)
            self.Resultados.config(text=f"Archivo leído:\n{ruta}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# -------------------- INTERFAZ -------------------- #
class InterfazArchivos:
    def __init__(self):
        self.Ventana = tk.Tk()
        self.Ventana.title("Ejercicio 6.8 – Lectura y escritura de archivos")
        self.Ventana.geometry("600x400")

        tk.Label(self.Ventana, text="Contenido del archivo:").pack()
        self.TextArea = tk.Text(self.Ventana, width=70, height=15)
        self.TextArea.pack(pady=10)

        self.Resultados = tk.Label(self.Ventana, text="Resultados:", font=("Arial", 10, "bold"))
        self.Resultados.pack(pady=10)

        self.FrameBotones = tk.Frame(self.Ventana)
        self.FrameBotones.pack(pady=10)

        self.CalcularObj = CalculosArchivos(self.TextArea, self.Resultados)

        tk.Button(self.FrameBotones, text="Guardar", bg="lightgreen",
                  command=self.CalcularObj.GuardarArchivo, font=("Arial", 10, "italic")).pack(side="left", padx=8)
        tk.Button(self.FrameBotones, text="Leer", bg="lightblue",
                  command=self.CalcularObj.LeerArchivo, font=("Arial", 10, "italic")).pack(side="left", padx=8)
        tk.Button(self.FrameBotones, text="Limpiar", bg="lightcoral",
                  command=self.Limpiar, font=("Arial", 10, "italic")).pack(side="left", padx=8)

    def Limpiar(self):
        self.TextArea.delete("1.0", tk.END)
        self.Resultados.config(text="Resultados:")

    def Ejecutar(self):
        self.Ventana.mainloop()


class Ejercicio5:
    def Principal():
        app = InterfazArchivos()
        app.Ejecutar()


if __name__ == "__main__":
    Ejercicio5.Principal()