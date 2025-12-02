import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json

# ------------------------------
#   Clase Habitacion
# ------------------------------

class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True
        self.huesped = ""

    def reservar(self, nombre):
        if not self.disponible:
            return False
        self.disponible = False
        self.huesped = nombre
        return True

    def liberar(self):
        if self.disponible:
            return False
        self.disponible = True
        self.huesped = ""
        return True


# ------------------------------
#        Clase App
# ------------------------------

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 8.5 - Hotel")
        self.root.geometry("780x500")

        # Crear habitaciones como en el libro
        self.habitaciones = []
        for i in range(10):
            precio = 120000 if i < 5 else 160000
            self.habitaciones.append(Habitacion(i + 1, precio))

        # Frame principal
        frame_main = ttk.Frame(self.root, padding=10)
        frame_main.pack(fill="both", expand=True)

        # -----------------------------------------
        #    GRID DE HABITACIONES (5 x 2)
        # -----------------------------------------

        frame_grid = ttk.LabelFrame(frame_main, text="Habitaciones", padding=10)
        frame_grid.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.labels_estado = {}

        index = 0
        for fila in range(2):
            for col in range(5):
                hab = self.habitaciones[index]
                marco = ttk.Frame(frame_grid, borderwidth=1, relief="solid", padding=8)
                marco.grid(row=fila, column=col, padx=8, pady=8)

                ttk.Label(marco, text=f"Habitación {hab.numero}", font=("Arial", 11, "bold")).pack()

                lbl_estado = ttk.Label(marco, text="Disponible", foreground="green")
                lbl_estado.pack(pady=2)

                ttk.Label(marco, text=f"Precio: {hab.precio:,}").pack()

                ttk.Button(marco, text="Reservar",
                           command=lambda n=hab.numero: self.reservar(n)).pack(side="left", padx=3, pady=(5,0))
                ttk.Button(marco, text="Liberar",
                           command=lambda n=hab.numero: self.liberar(n)).pack(side="right", padx=3, pady=(5,0))

                self.labels_estado[hab.numero] = lbl_estado
                index += 1

        # -----------------------------------------
        #   PANEL DE ACCIONES
        # -----------------------------------------

        frame_right = ttk.Frame(frame_main, padding=5)
        frame_right.pack(side="right", fill="y")

        ttk.Label(frame_right, text="Acciones", font=("Arial", 12, "bold")).pack(pady=5)

        ttk.Button(frame_right, text="Mostrar resumen",
                   command=self.mostrar_resumen).pack(fill="x", pady=5)

        ttk.Button(frame_right, text="Guardar estado",
                   command=self.guardar).pack(fill="x", pady=5)

        ttk.Button(frame_right, text="Cargar estado",
                   command=self.cargar).pack(fill="x", pady=5)

        ttk.Button(frame_right, text="Salir",
                   command=self.root.quit).pack(fill="x", pady=25)

        # -----------------------------------------
        #   PANEL DE RESUMEN
        # -----------------------------------------

        frame_resumen = ttk.LabelFrame(frame_main, text="Resumen del hotel", padding=10)
        frame_resumen.pack(side="bottom", fill="both")

        self.text = tk.Text(frame_resumen, height=8)
        self.text.pack(fill="both", expand=True)

        self.actualizar_estados()

    # ------------------------------
    #     Función: Reservar
    # ------------------------------

    def reservar(self, numero):
        hab = self.habitaciones[numero - 1]

        if not hab.disponible:
            messagebox.showwarning("Error", "La habitación ya está ocupada.")
            return

        nombre = simpledialog.askstring("Reservar", "Nombre del huésped:")
        if not nombre:
            return

        hab.reservar(nombre)
        messagebox.showinfo("Reserva", f"Habitación {numero} reservada a {nombre}.")
        self.actualizar_estados()

    # ------------------------------
    #     Función: Liberar
    # ------------------------------

    def liberar(self, numero):
        hab = self.habitaciones[numero - 1]

        if hab.disponible:
            messagebox.showwarning("Error", "La habitación ya está libre.")
            return

        hab.liberar()
        messagebox.showinfo("Liberada", f"Habitación {numero} ha sido liberada.")
        self.actualizar_estados()

    # ------------------------------
    #     Actualizar UI
    # ------------------------------

    def actualizar_estados(self):
        for hab in self.habitaciones:
            lbl = self.labels_estado[hab.numero]
            if hab.disponible:
                lbl.config(text="Disponible", foreground="green")
            else:
                lbl.config(text=f"Ocupada por: {hab.huesped}", foreground="red")

    # ------------------------------
    #     Mostrar resumen
    # ------------------------------

    def mostrar_resumen(self):
        self.text.delete("1.0", "end")
        for h in self.habitaciones:
            if h.disponible:
                self.text.insert(
                    "end", f"Habitación {h.numero}: DISPONIBLE - Precio {h.precio:,}\n"
                )
            else:
                self.text.insert(
                    "end",
                    f"Habitación {h.numero}: OCUPADA por {h.huesped} - Precio {h.precio:,}\n"
                )

    # ------------------------------
    #     Guardar estado
    # ------------------------------

    def guardar(self):
        datos = []
        for h in self.habitaciones:
            datos.append({
                "numero": h.numero,
                "precio": h.precio,
                "disponible": h.disponible,
                "huesped": h.huesped
            })

        with open("hotel_guardado.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        messagebox.showinfo("Guardado", "Estado del hotel guardado correctamente.")

    # ------------------------------
    #     Cargar estado
    # ------------------------------

    def cargar(self):
        try:
            with open("hotel_guardado.json", "r", encoding="utf-8") as f:
                datos = json.load(f)

            for d in datos:
                hab = self.habitaciones[d["numero"] - 1]
                hab.precio = d["precio"]
                hab.disponible = d["disponible"]
                hab.huesped = d["huesped"]

            self.actualizar_estados()
            messagebox.showinfo("Cargado", "Estado restaurado correctamente.")

        except:
            messagebox.showerror("Error", "No se pudo cargar el archivo.")

# ------------------------------
#          Main
# ------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()