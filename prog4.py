from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
from validaciones import Validar

class Principal:
    def __init__(self):
        self.val =  Validar()  # instancia del validador
        self.ventana = Tk()
        self.lis=[]
        self.ventana.title('Practica 4')

        # Tamaño y posición de la ventana
        ancho = 500
        alto = 300
        pantalla_ancho = self.ventana.winfo_screenwidth()
        pantalla_alto = self.ventana.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        # Variables de control
        self.con = 0           # Contador para generar claves
        self.bandera = False   # Bandera para modo edición
        self.renglon = None    # Guarda la fila seleccionada
        self.index = ""        # Guarda la clave del registro

    def inicio(self):
        # ---------------- Campos de texto ----------------
        Label(self.ventana, text="Nombre").place(x=10, y=10)
        self.nombre = Entry(self.ventana)
        self.nombre.place(x=10, y=30, width=100)

        Label(self.ventana, text="Edad").place(x=130, y=10)
        self.edad = Entry(self.ventana)
        self.edad.place(x=130, y=30, width=100)

        Label(self.ventana, text="Correo").place(x=250, y=10)
        self.correo = Entry(self.ventana)
        self.correo.place(x=250, y=30, width=100)

        # ---------------- Botones ----------------
        Button(self.ventana, text="Agregar", command=self.AgregarElimentos).place(x=380, y=20, width=100, height=30)
        Button(self.ventana, text="Eliminar", command=self.eliminar).place(x=380, y=60, width=100, height=30)
        Button(self.ventana, text="Seleccionar", command=self.validarCaja).place(x=380, y=100, width=100, height=30)

        # ---------------- Tabla ----------------
        columnas = ("Clave", "Nombre", "Correo", "Edad")
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        self.tabla.place(x=10, y=90, width=350, height=190)

        # Encabezados y alineación
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=80)

        # Scrollbars
        scrolly = ttk.Scrollbar(self.ventana, orient="vertical", command=self.tabla.yview)
        scrollx = ttk.Scrollbar(self.ventana, orient="horizontal", command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.place(x=360, y=90, height=190)
        scrollx.place(x=10, y=280, width=350)

        self.ventana.mainloop()

    # ---------------- Seleccionar fila (modo edición) ----------------
    def validarCaja(self):
        seleccion = self.tabla.selection()  # obtiene fila seleccionada
        if not seleccion:
            messagebox.showerror("Error", "Elige una fila")
        else:
            self.renglon = seleccion[0]
            valores = self.tabla.item(self.renglon, "values")

            # Guardamos los valores para edición
            self.index = valores[0]  # clave
            self.nombre.delete(0, END)
            self.edad.delete(0, END)
            self.correo.delete(0, END)
            self.nombre.insert(0, valores[1])
            self.correo.insert(0, valores[2])
            self.edad.insert(0, valores[3])
            self.bandera = True  # activamos modo edición

    # ---------------- Agregar o actualizar elementos ----------------
    def AgregarElimentos(self):
        if len(self.nombre.get()) == 0 or len(self.edad.get()) == 0 or len(self.correo.get()) == 0:
            messagebox.showerror("Error", "Faltan datos")
            return

        nombre = self.nombre.get()
        edad = self.edad.get()
        correo = self.correo.get()

        # Validaciones básicas
        if not edad.isdigit():
            messagebox.showerror("Error", "Edad debe ser numérica")
            return
        if not self.val.ValidarNombre(nombre):
            messagebox.showerror("Error", "El nombre solo debe contener letras")
            return

        # Si no estamos editando, agregamos nuevo registro
        if not self.bandera:
            clave = str(self.con) + str(random.randint(1, 100)) + nombre[0:2].upper()
            self.con += 1
            self.tabla.insert("", "end", values=(clave, nombre, correo, edad))
            messagebox.showinfo("Correcto", "Registro agregado correctamente")
        else:
            # Modo edición activado
            print("Modo edición activado")
            clave = self.index  # mantener la misma clave
            self.tabla.item(self.renglon, values=(clave, nombre, correo, edad))
            self.bandera = False
            self.renglon = None
            messagebox.showinfo("Correcto", "Datos actualizados")

        # Limpiar entradas después de agregar o editar
        self.nombre.delete(0, END)
        self.edad.delete(0, END)
        self.correo.delete(0, END)

    # ---------------- Eliminar elemento ----------------
    def eliminar(self):
        renglon = self.tabla.selection()
        if not renglon:
            messagebox.showerror("Error", "Elige una fila")
        else:
            self.tabla.delete(renglon)
            messagebox.showinfo("Correcto", "Fila eliminada")

# ---------------- Ejecutar programa ----------------
if __name__ == "__main__":
    app = Principal()
    app.inicio()
