from tkinter import *
from tkinter import messagebox
from validaciones import Validar

class Principal:
    def __init__(self):
        self.val = Validar()  # Instancia del validador / Validator instance
        self.ventana = Tk()  # Crear ventana principal / Create main window
        self.lis=[]  # Lista auxiliar (no usada directamente) / Auxiliary list
        self.ventana.title('Practica 3')  # Título de la ventana / Window title

        # Configuración de tamaño y posición / Window size and position
        ancho = 350
        alto = 250
        pantalla_ancho = self.ventana.winfo_screenwidth()  # Ancho de pantalla / Screen width
        pantalla_alto = self.ventana.winfo_screenheight()  # Alto de pantalla / Screen height
        x = (pantalla_alto//2)- (ancho//2)
        y = (pantalla_ancho//2)- (alto//2)
        self.ventana.geometry(f"{ancho}x{alto}+{x+350}+{y-350}")

    # -------------------- MÉTODOS PARA QUITAR PLACEHOLDER / REMOVE PLACEHOLDER METHODS --------------------
    def quitar_placeholder1(self, event):
        if self.nombre.get() == self.placeholder1:  # Si el texto es el placeholder / If text equals placeholder
            self.nombre.delete(0, END)
            self.nombre.config(fg="black")  # Cambiar color del texto / Change text color

    def quitar_placeholder2(self, event):    
        if self.telefono.get() == self.placeholder2:
            self.telefono.delete(0, END)
            self.telefono.config(fg="black")

    def quitar_placeholder3(self, event):
        if self.domicilio.get() == self.placeholder3:
            self.domicilio.delete(0, END)
            self.domicilio.config(fg="black")

    # -------------------- MÉTODOS PARA PONER PLACEHOLDER / ADD PLACEHOLDER METHODS --------------------
    def poner_placeholder1(self, event):
        if self.nombre.get() == "":  # Si está vacío / If empty
            self.nombre.insert(0, self.placeholder1)
            self.nombre.config(fg="gray")

    def poner_placeholder2(self, event):
        if self.telefono.get() == "":
            self.telefono.insert(0, self.placeholder2)
            self.telefono.config(fg="gray")

    def poner_placeholder3(self, event):
        if self.domicilio.get() == "":
            self.domicilio.insert(0, self.placeholder3)
            self.domicilio.config(fg="gray")

    # -------------------- INICIO DE LA INTERFAZ / MAIN UI SETUP --------------------
    def inicio(self):
        # ----------- Caja de texto: nombre / Name input -----------
        self.placeholder1 = "Nombre"
        self.nombre = Entry(self.ventana, fg="gray")
        self.nombre.insert(0, self.placeholder1)
        self.nombre.bind("<FocusIn>", self.quitar_placeholder1)
        self.nombre.bind("<FocusOut>", self.poner_placeholder1)
        # self.nombre.bind("<Return>", self.validarCaja)  # Presionar Enter (opcional) / Optional Enter trigger
        self.nombre.place(x=10, y=10, width=100)

        # ----------- Caja de texto: teléfono / Phone input -----------
        self.placeholder2 = "Telefono"
        self.telefono = Entry(self.ventana, fg="gray")
        self.telefono.insert(0, self.placeholder2)
        self.telefono.bind("<FocusIn>", self.quitar_placeholder2)
        self.telefono.bind("<FocusOut>", self.poner_placeholder2)
        # self.telefono.bind("<Return>", self.validarCaja)
        self.telefono.place(x=120, y=10, width=100)

        # ----------- Caja de texto: domicilio / Address input -----------
        self.placeholder3 = "Domicilio"
        self.domicilio = Entry(self.ventana, fg="gray")
        self.domicilio.insert(0, self.placeholder3)
        self.domicilio.bind("<FocusIn>", self.quitar_placeholder3)
        self.domicilio.bind("<FocusOut>", self.poner_placeholder3)
        self.domicilio.bind("<Return>", self.validarCaja)  # Enter ejecuta validación / Enter triggers validation
        self.domicilio.place(x=230, y=10, width=100)

        # ----------- Etiquetas y botones de selección de sexo / Gender selection -----------
        Label(self.ventana,text="Sexo").place(x=10, y=30)
        self.modo = StringVar(value="F")  # Valor por defecto femenino / Default female
        Radiobutton(self.ventana,text="F",variable=self.modo,value="F").place(x=10,y=50)
        Radiobutton(self.ventana,text="M",variable=self.modo,value="M").place(x=10,y=70)

        # ----------- Lista para mostrar resultados / Listbox to display results -----------
        self.lista = Listbox(self.ventana, height=8, width=50, bg='grey',
                            activestyle="dotbox", fg="Black")
        self.lista.place(x=10, y=100)

        # ----------- Botón para agregar persona / Add person button -----------
        Button(self.ventana,text="Agregar",command=self.validarCaja).place(x=150,y=40,width=100,height=55)

        self.ventana.mainloop()  # Inicia la ventana / Start window

    def agregar(self):
        pass  # Método reservado (no implementado) / Placeholder method (not implemented)

    # -------------------- VALIDAR Y AGREGAR DATOS / VALIDATE AND ADD DATA --------------------
    def validarCaja(self,event=0):
        # Verifica si hay datos faltantes / Check for missing data
        if (self.nombre.get()==self.placeholder1) or (self.telefono.get()==self.placeholder2) or (self.domicilio.get()==self.placeholder3) or (self.domicilio.get()==""):
            messagebox.showerror('Error','Faltan datos')
        else:
            nombre = self.nombre.get()
            telefono = self.telefono.get()
            domicilio = self.domicilio.get()

            # Validar formato del número / Validate phone format
            if len(telefono)!=10:
                messagebox.showerror("Error","formato de numero incorrecto")
                self.telefono.delete(0,END)

            # Validar que sean solo números / Validate only numbers
            if not (self.val.ValidarNumeros(telefono)):
                messagebox.showerror("Error","solo se permiten numero")
                self.telefono.delete(0,END)

            # Validar que el nombre tenga solo letras / Validate name contains only letters
            if not self.val.ValidarNombre(nombre):
                messagebox.showerror("Error","solo se permiten letras")
                self.nombre.delete(0,END)
            else:
                # Asignar valor al sexo según selección / Assign gender
                if self.modo.get()=="F":
                    sexo = "Femenino"
                else:
                    sexo = "Masculino"

                # Crear clave con iniciales y parte del domicilio / Create key with initials and address part
                clave = nombre[0] + telefono[0] + domicilio[2:]
                # Concatenar todos los datos / Concatenate all data
                persona = clave + " - " + nombre + " - " + telefono + " - " + domicilio + " - " + sexo
                # Insertar en lista / Insert into listbox
                self.lista.insert(END, persona)
                persona = ""

                # Limpiar campos / Clear input fields
                self.nombre.delete(0,END)
                self.telefono.delete(0,END)
                self.domicilio.delete(0,END)


# -------------------- EJECUCIÓN PRINCIPAL / MAIN EXECUTION --------------------
if __name__=="__main__":
    app = Principal()  # Crear instancia / Create instance
    app.inicio()       # Ejecutar aplicación / Run application
