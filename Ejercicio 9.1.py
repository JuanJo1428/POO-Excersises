import tkinter as tk
from tkinter import ttk, messagebox


# ----------------------------------------------------
#   Clase Contacto (equivalente a la del libro)
# ----------------------------------------------------
class Contacto:
    def __init__(self, nombres, apellidos, fecha, direccion, telefono, correo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha = fecha
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def to_list(self):
        return [
            self.nombres,
            self.apellidos,
            self.fecha,
            self.direccion,
            self.telefono,
            self.correo
        ]


# ----------------------------------------------------
#   Clase Principal ContactosApp
# ----------------------------------------------------
class ContactosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 9.1 - Contacto")
        self.root.geometry("820x500")

        self.contactos = []  # lista de Contacto

        # --------------------------
        #   Formulario superior
        # --------------------------
        frm_form = ttk.LabelFrame(root, text="Nuevo contacto", padding=12)
        frm_form.pack(fill="x", padx=10, pady=10)

        # Nombres
        ttk.Label(frm_form, text="Nombres:").grid(row=0, column=0, sticky="w")
        self.var_nom = tk.StringVar()
        ttk.Entry(frm_form, textvariable=self.var_nom, width=30).grid(row=0, column=1, padx=8)

        # Apellidos
        ttk.Label(frm_form, text="Apellidos:").grid(row=0, column=2, sticky="w")
        self.var_ape = tk.StringVar()
        ttk.Entry(frm_form, textvariable=self.var_ape, width=30).grid(row=0, column=3, padx=8)

        # Fecha nacimiento
        ttk.Label(frm_form, text="Fecha nacimiento:").grid(row=1, column=0, sticky="w", pady=6)
        self.var_fecha = tk.StringVar()
        ttk.Entry(frm_form, textvariable=self.var_fecha, width=30).grid(row=1, column=1, padx=8)

        # Dirección
        ttk.Label(frm_form, text="Dirección:").grid(row=1, column=2, sticky="w")
        self.var_dir = tk.StringVar()
        ttk.Entry(frm_form, textvariable=self.var_dir, width=30).grid(row=1, column=3, padx=8)

        # Teléfono
        ttk.Label(frm_form, text="Teléfono:").grid(row=2, column=0, sticky="w", pady=6)
        self.var_tel = tk.StringVar()
        ttk.Entry(frm_form, textvariable=self.var_tel, width=30).grid(row=2, column=1, padx=8)

        # Correo
        ttk.Label(frm_form, text="Correo:").grid(row=2, column=2, sticky="w")
        self.var_cor = tk.StringVar()
        ttk.Entry(frm_form, textvariable=self.var_cor, width=30).grid(row=2, column=3, padx=8)

        # Botón agregar
        ttk.Button(frm_form, text="Agregar contacto", command=self.agregar_contacto)\
            .grid(row=3, column=0, columnspan=4, pady=10)

        # --------------------------
        #   Tabla inferior
        # --------------------------
        frm_tabla = ttk.LabelFrame(root, text="Lista de contactos", padding=10)
        frm_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        columnas = ("nombres", "apellidos", "fecha", "direccion", "telefono", "correo")

        self.tabla = ttk.Treeview(frm_tabla, columns=columnas, show="headings", height=12)

        self.tabla.heading("nombres", text="Nombres")
        self.tabla.heading("apellidos", text="Apellidos")
        self.tabla.heading("fecha", text="F. Nacimiento")
        self.tabla.heading("direccion", text="Dirección")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("correo", text="Correo")

        # Anchos de columnas
        self.tabla.column("nombres", width=120)
        self.tabla.column("apellidos", width=120)
        self.tabla.column("fecha", width=100)
        self.tabla.column("direccion", width=170)
        self.tabla.column("telefono", width=100)
        self.tabla.column("correo", width=150)

        self.tabla.pack(fill="both", expand=True)

    # ----------------------------------------------------
    #   Agregar contacto
    # ----------------------------------------------------
    def agregar_contacto(self):
        nombres = self.var_nom.get().strip()
        apellidos = self.var_ape.get().strip()
        fecha = self.var_fecha.get().strip()
        direccion = self.var_dir.get().strip()
        telefono = self.var_tel.get().strip()
        correo = self.var_cor.get().strip()

        # Validación simple
        if not nombres or not apellidos:
            messagebox.showwarning("Datos incompletos", "Nombres y apellidos son obligatorios.")
            return

        nuevo = Contacto(nombres, apellidos, fecha, direccion, telefono, correo)
        self.contactos.append(nuevo)

        # Insertar en la tabla
        self.tabla.insert("", "end", values=nuevo.to_list())

        # Limpiar entradas
        self.var_nom.set("")
        self.var_ape.set("")
        self.var_fecha.set("")
        self.var_dir.set("")
        self.var_tel.set("")
        self.var_cor.set("")

        messagebox.showinfo("Contacto agregado", "El contacto fue añadido correctamente.")


# ------------------------------
#   Inicio del programa
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    ContactosApp(root)
    root.mainloop()
