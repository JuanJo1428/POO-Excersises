import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime

class NominaApp:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 8.4 - Nomina")
        root.geometry("650x480")

        frm = ttk.Frame(root, padding=12)
        frm.pack(fill="both", expand=True)

        left = ttk.Frame(frm)
        left.pack(side="left", fill="y", padx=(0,12))

        ttk.Label(left, text="Empleado").grid(row=0, column=0, sticky="w")
        self.nombre_var = tk.StringVar()
        ttk.Entry(left, textvariable=self.nombre_var, width=30).grid(row=1, column=0)

        ttk.Label(left, text="ID empleado").grid(row=2, column=0, sticky="w", pady=(8,0))
        self.id_var = tk.StringVar()
        ttk.Entry(left, textvariable=self.id_var, width=20).grid(row=3, column=0)

        ttk.Label(left, text="Cargo").grid(row=4, column=0, sticky="w", pady=(8,0))
        self.cargo_var = tk.StringVar()
        ttk.Entry(left, textvariable=self.cargo_var, width=30).grid(row=5, column=0)

        right = ttk.Frame(frm)
        right.pack(side="left", fill="both", expand=True)

        ttk.Label(right, text="Horas trabajadas").grid(row=0, column=0, sticky="w")
        self.horas_var = tk.DoubleVar(value=40.0)
        ttk.Entry(right, textvariable=self.horas_var, width=10).grid(row=1, column=0)

        ttk.Label(right, text="Tarifa por hora").grid(row=2, column=0, sticky="w", pady=(8,0))
        self.tarifa_var = tk.DoubleVar(value=10000.0)
        ttk.Entry(right, textvariable=self.tarifa_var, width=10).grid(row=3, column=0)

        ttk.Label(right, text="Deducciones (%)").grid(row=4, column=0, sticky="w", pady=(8,0))
        self.ded_var = tk.DoubleVar(value=8.0)
        ttk.Entry(right, textvariable=self.ded_var, width=10).grid(row=5, column=0)

        botones = ttk.Frame(frm)
        botones.pack(side="bottom", fill="x", pady=(12,0))

        ttk.Button(botones, text="Calcular nomina", command=self.calcular).pack(side="left", padx=6)
        ttk.Button(botones, text="Exportar CSV", command=self.exportar_csv).pack(side="left", padx=6)
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=6)

        res_frame = ttk.LabelFrame(frm, text="Resumen", padding=10)
        res_frame.pack(side="right", fill="both", expand=True)

        self.text = tk.Text(res_frame, width=40, height=18, state="disabled", wrap="word")
        self.text.pack(fill="both", expand=True)

        self.ultimo = None

    def calcular(self):
        try:
            nombre = self.nombre_var.get().strip() or "Sin nombre"
            id_emp = self.id_var.get().strip() or "N/A"
            cargo = self.cargo_var.get().strip() or "N/A"
            horas = float(self.horas_var.get())
            tarifa = float(self.tarifa_var.get())
            ded_pct = float(self.ded_var.get())

            bruto = horas * tarifa
            deducciones = bruto * (ded_pct / 100.0)
            neto = bruto - deducciones

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            resumen = (
                f"Fecha: {fecha}\n"
                f"Empleado: {nombre}\n"
                f"ID: {id_emp}\n"
                f"Cargo: {cargo}\n\n"
                f"Horas trabajadas: {horas:.2f}\n"
                f"Tarifa por hora: {tarifa:,.2f}\n\n"
                f"Salario bruto: {bruto:,.2f}\n"
                f"Deducciones ({ded_pct:.2f}%): {deducciones:,.2f}\n"
                f"Salario neto: {neto:,.2f}\n"
            )

            self.text.config(state="normal")
            self.text.delete("1.0", "end")
            self.text.insert("end", resumen)
            self.text.config(state="disabled")

            self.ultimo = {
                "fecha": fecha,
                "nombre": nombre,
                "id": id_emp,
                "cargo": cargo,
                "horas": horas,
                "tarifa": tarifa,
                "bruto": bruto,
                "deducciones": deducciones,
                "neto": neto,
                "ded_pct": ded_pct
            }

        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular nomina:\n{e}")

    def exportar_csv(self):
        if not self.ultimo:
            messagebox.showwarning("Atencion", "Calcula la nomina antes de exportar.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV","*.csv")])
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["fecha","nombre","id","cargo","horas","tarifa","bruto","deducciones","ded_pct","neto"])
                u = self.ultimo
                writer.writerow([
                    u["fecha"], u["nombre"], u["id"], u["cargo"],
                    f"{u['horas']:.2f}", f"{u['tarifa']:.2f}",
                    f"{u['bruto']:.2f}", f"{u['deducciones']:.2f}",
                    f"{u['ded_pct']:.2f}", f"{u['neto']:.2f}"
                ])
            messagebox.showinfo("CSV", f"Exportado correctamente:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar CSV:\n{e}")

    def limpiar(self):
        self.nombre_var.set("")
        self.id_var.set("")
        self.cargo_var.set("")
        self.horas_var.set(40.0)
        self.tarifa_var.set(10000.0)
        self.ded_var.set(8.0)
        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.config(state="disabled")
        self.ultimo = None

if __name__ == "__main__":
    root = tk.Tk()
    NominaApp(root)
    root.mainloop()