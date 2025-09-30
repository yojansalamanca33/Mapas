
import tkinter as tk
from tkinter import messagebox

class FrmEstudiantes(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Estudiantes")
        self.geometry("500x500")

        # Diccionario que simula Map<String, String>
        self.mapa_estudiantes = {}

        # Campos del formulario
        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Apellido:").pack()
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.pack()

        tk.Label(self, text="Edad:").pack()
        self.entry_edad = tk.Entry(self)
        self.entry_edad.pack()

        tk.Label(self, text="Teléfono:").pack()
        self.entry_telefono = tk.Entry(self)
        self.entry_telefono.pack()

        tk.Label(self, text="Correo:").pack()
        self.entry_correo = tk.Entry(self)
        self.entry_correo.pack()

        tk.Label(self, text="Asignatura:").pack()
        self.entry_asignatura = tk.Entry(self)
        self.entry_asignatura.pack()

        # Botones
        tk.Button(self, text="Guardar", command=self.guardar_estudiante).pack(pady=5)
        tk.Button(self, text="Listar", command=self.listar_estudiantes).pack(pady=5)

        # Área de texto para listar
        self.area_listado = tk.Text(self, height=12, width=50)
        self.area_listado.pack(pady=10)

    def guardar_estudiante(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        edad = self.entry_edad.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()
        asignatura = self.entry_asignatura.get()

        if not nombre or not correo:
            messagebox.showwarning("Advertencia", "Nombre y Correo son obligatorios.")
            return

        clave = f"{nombre} {apellido}"
        valor = f"Edad: {edad}, Tel: {telefono}, Correo: {correo}, Asignatura: {asignatura}"

        self.mapa_estudiantes[clave] = valor

        messagebox.showinfo("Éxito", "Estudiante guardado correctamente")

        # limpiar campos
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_asignatura.delete(0, tk.END)

    def listar_estudiantes(self):
        self.area_listado.delete("1.0", tk.END)
        for clave, valor in self.mapa_estudiantes.items():
            self.area_listado.insert(tk.END, f"{clave} -> {valor}\n")


if __name__ == "__main__":
    app = FrmEstudiantes()
    app.mainloop()

