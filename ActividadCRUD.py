import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os

# -------------------- LÓGICA (manejo de archivo y operaciones CRUD) -------------------- #
class CalculosPersonas:
    """
    Clase que encapsula la lógica de CRUD sobre un archivo CSV simple.
    Campos manejados: id, nombre, edad, ciudad
    """

    def __init__(self, TextArea, Resultados, Archivo="personas_db.csv"):
        self.TextArea = TextArea
        self.Resultados = Resultados
        self.Archivo = Archivo

        # Crear archivo si no existe
        if not os.path.exists(self.Archivo):
            try:
                with open(self.Archivo, mode="w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["id", "nombre", "edad", "ciudad"])
            except Exception as e:
                messagebox.showerror("Error al crear archivo", str(e))

    def _leer_todos(self):
        registros = []
        try:
            with open(self.Archivo, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    registros.append(row)
        except Exception as e:
            messagebox.showerror("Error lectura", str(e))
        return registros

    def _escribir_todos(self, registros):
        try:
            with open(self.Archivo, mode="w", newline="", encoding="utf-8") as f:
                fieldnames = ["id", "nombre", "edad", "ciudad"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for r in registros:
                    writer.writerow(r)
        except Exception as e:
            messagebox.showerror("Error escritura", str(e))

    def _siguiente_id(self, registros):
        max_id = 0
        for r in registros:
            try:
                val = int(r.get("id", 0))
                if val > max_id:
                    max_id = val
            except:
                continue
        return str(max_id + 1)

    def CrearRegistro(self, nombre, edad, ciudad):
        if not nombre.strip():
            messagebox.showwarning("Validación", "El nombre no puede estar vacío.")
            return

        registros = self._leer_todos()

        nuevo = {
            "id": self._siguiente_id(registros),
            "nombre": nombre.strip(),
            "edad": edad.strip(),
            "ciudad": ciudad.strip()
        }

        registros.append(nuevo)
        self._escribir_todos(registros)

        self.Resultados.config(text=f"Registro creado: id={nuevo['id']}")
        self.MostrarTodos()

    def LeerRegistro(self, id_buscar):
        registros = self._leer_todos()
        encontrado = None

        for r in registros:
            if r.get("id") == str(id_buscar).strip():
                encontrado = r
                break

        if encontrado:
            texto = (
                "Registro encontrado:\n"
                f"ID: {encontrado['id']}\n"
                f"Nombre: {encontrado['nombre']}\n"
                f"Edad: {encontrado['edad']}\n"
                f"Ciudad: {encontrado['ciudad']}"
            )
            self.TextArea.delete("1.0", tk.END)
            self.TextArea.insert(tk.END, texto)
            self.Resultados.config(text=f"Registro leído: id={encontrado['id']}")
        else:
            messagebox.showinfo("No encontrado", f"No existe registro con id {id_buscar}")

    def ActualizarRegistro(self, id_buscar, nombre, edad, ciudad):
        registros = self._leer_todos()
        actualizado = False

        for r in registros:
            if r.get("id") == str(id_buscar).strip():
                r["nombre"] = nombre.strip()
                r["edad"] = edad.strip()
                r["ciudad"] = ciudad.strip()
                actualizado = True
                break

        if actualizado:
            self._escribir_todos(registros)
            self.Resultados.config(text=f"Registro actualizado: id={id_buscar}")
            self.MostrarTodos()
        else:
            messagebox.showinfo("No encontrado", f"No existe registro con id {id_buscar}")

    def EliminarRegistro(self, id_buscar):
        registros = self._leer_todos()
        nuevos = []

        for r in registros:
            if r.get("id") != str(id_buscar).strip():
                nuevos.append(r)

        if len(nuevos) == len(registros):
            messagebox.showinfo("No encontrado", f"No existe registro con id {id_buscar}")
            return

        self._escribir_todos(nuevos)
        self.Resultados.config(text=f"Registro eliminado: id={id_buscar}")
        self.MostrarTodos()

    def MostrarTodos(self):
        registros = self._leer_todos()

        if not registros:
            contenido = "No hay registros."
        else:
            lineas = []
            for r in registros:
                if r.get("id") == "id":
                    continue

                linea = (
                    "ID: " + r.get("id", "") +
                    "\tNombre: " + r.get("nombre", "") +
                    "\tEdad: " + r.get("edad", "") +
                    "\tCiudad: " + r.get("ciudad", "")
                )
                lineas.append(linea)

            if len(lineas) == 0:
                contenido = "No hay registros."
            else:
                contenido = "\n".join(lineas)

        self.TextArea.delete("1.0", tk.END)
        self.TextArea.insert(tk.END, contenido)
        self.Resultados.config(text=f"Total registros: {len(registros)-1 if registros else 0}")

    def ExportarComo(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Texto", "*.txt")]
        )

        if not ruta:
            return

        try:
            with open(self.Archivo, mode="r", encoding="utf-8") as src:
                contenido = src.read()

            with open(ruta, mode="w", encoding="utf-8") as dst:
                dst.write(contenido)

            messagebox.showinfo("Exportado", f"Copia guardada en:\n{ruta}")
            self.Resultados.config(text=f"Copia guardada: {ruta}")

        except Exception as e:
            messagebox.showerror("Error exportar", str(e))


# -------------------- INTERFAZ (Tkinter) -------------------- #
class InterfazPersonas:
    def __init__(self):
        self.Ventana = tk.Tk()
        self.Ventana.title("Actividad 5 - CRUD (Archivos) - Python / Tkinter")
        self.Ventana.geometry("780x520")

        frm_top = tk.Frame(self.Ventana)
        frm_top.pack(pady=8)

        tk.Label(frm_top, text="ID:").grid(row=0, column=0, padx=6, sticky="e")
        self.EntryID = tk.Entry(frm_top, width=8)
        self.EntryID.grid(row=0, column=1, padx=6)

        tk.Label(frm_top, text="Nombre:").grid(row=0, column=2, padx=6, sticky="e")
        self.EntryNombre = tk.Entry(frm_top, width=28)
        self.EntryNombre.grid(row=0, column=3, padx=6)

        tk.Label(frm_top, text="Edad:").grid(row=1, column=0, padx=6, sticky="e")
        self.EntryEdad = tk.Entry(frm_top, width=8)
        self.EntryEdad.grid(row=1, column=1, padx=6)

        tk.Label(frm_top, text="Ciudad:").grid(row=1, column=2, padx=6, sticky="e")
        self.EntryCiudad = tk.Entry(frm_top, width=28)
        self.EntryCiudad.grid(row=1, column=3, padx=6)

        self.FrameBotones = tk.Frame(self.Ventana)
        self.FrameBotones.pack(pady=10)

        frm_text = tk.Frame(self.Ventana)
        frm_text.pack(padx=10, pady=6, fill="both", expand=True)

        self.TextArea = tk.Text(frm_text, width=90, height=18)
        self.TextArea.pack(side="left", fill="both", expand=True, padx=(0, 4))

        scrollbar = tk.Scrollbar(frm_text, command=self.TextArea.yview)
        scrollbar.pack(side="right", fill="y")
        self.TextArea.config(yscrollcommand=scrollbar.set)

        self.Resultados = tk.Label(self.Ventana, text="Resultados:", font=("Arial", 10, "bold"))
        self.Resultados.pack(pady=6)

        self.CalcularObj = CalculosPersonas(self.TextArea, self.Resultados)

        tk.Button(self.FrameBotones, text="Create", bg="lightgreen", width=10,
                  command=self._on_create, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        tk.Button(self.FrameBotones, text="Read (por ID)", bg="lightblue", width=12,
                  command=self._on_read, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        tk.Button(self.FrameBotones, text="Update", bg="khaki", width=10,
                  command=self._on_update, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        tk.Button(self.FrameBotones, text="Delete", bg="lightcoral", width=10,
                  command=self._on_delete, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        tk.Button(self.FrameBotones, text="List All", bg="lightgray", width=10,
                  command=self.CalcularObj.MostrarTodos, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        tk.Button(self.FrameBotones, text="Exportar copia", bg="lightyellow", width=12,
                  command=self.CalcularObj.ExportarComo, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        tk.Button(self.FrameBotones, text="Limpiar", bg="white", width=10,
                  command=self.Limpiar, font=("Arial", 10, "italic")).pack(side="left", padx=6)

        self.CalcularObj.MostrarTodos()

    def _on_create(self):
        nombre = self.EntryNombre.get()
        edad = self.EntryEdad.get()
        ciudad = self.EntryCiudad.get()

        self.CalcularObj.CrearRegistro(nombre, edad, ciudad)

        self.EntryID.delete(0, tk.END)
        self.EntryNombre.delete(0, tk.END)
        self.EntryEdad.delete(0, tk.END)
        self.EntryCiudad.delete(0, tk.END)

    def _on_read(self):
        id_buscar = self.EntryID.get().strip()
        if not id_buscar:
            messagebox.showwarning("Validación", "Ingresa el ID para leer.")
            return
        self.CalcularObj.LeerRegistro(id_buscar)

    def _on_update(self):
        id_buscar = self.EntryID.get().strip()
        if not id_buscar:
            messagebox.showwarning("Validación", "Ingresa el ID para actualizar.")
            return

        nombre = self.EntryNombre.get()
        edad = self.EntryEdad.get()
        ciudad = self.EntryCiudad.get()

        if messagebox.askyesno("Confirmar", f"¿Actualizar registro id={id_buscar}?"):
            self.CalcularObj.ActualizarRegistro(id_buscar, nombre, edad, ciudad)

            self.EntryID.delete(0, tk.END)
            self.EntryNombre.delete(0, tk.END)
            self.EntryEdad.delete(0, tk.END)
            self.EntryCiudad.delete(0, tk.END)

    def _on_delete(self):
        id_buscar = self.EntryID.get().strip()
        if not id_buscar:
            messagebox.showwarning("Validación", "Ingresa el ID para eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Eliminar registro id={id_buscar}?"):
            self.CalcularObj.EliminarRegistro(id_buscar)

            self.EntryID.delete(0, tk.END)
            self.EntryNombre.delete(0, tk.END)
            self.EntryEdad.delete(0, tk.END)
            self.EntryCiudad.delete(0, tk.END)

    def Limpiar(self):
        self.EntryID.delete(0, tk.END)
        self.EntryNombre.delete(0, tk.END)
        self.EntryEdad.delete(0, tk.END)
        self.EntryCiudad.delete(0, tk.END)
        self.TextArea.delete("1.0", tk.END)
        self.Resultados.config(text="Resultados:")

    def Ejecutar(self):
        self.Ventana.mainloop()


# -------------------- PUNTO DE ENTRADA -------------------- #
class Ejercicio5:
    def Principal():
        app = InterfazPersonas()
        app.Ejecutar()


if __name__ == "__main__":
    Ejercicio5.Principal()
