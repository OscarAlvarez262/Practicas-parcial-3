# hacer un programa que lea nombre, apellido paterno y apellido materno
# en 3 cajas separadas ademas leer dia, mes y año de nacimiento de 3 cajas de 
# texto separadas. al presionar un boton se agregara a un listbox el rfc de la 
# persona, ademas contendra dos botones para eliminar mediante pilas o colas
# ------------------------------------------------------------
# Program to input name, paternal surname, and maternal surname
# from 3 separate boxes, and also read day, month, and year of birth
# from 3 separate text boxes. When pressing a button, it adds the person's RFC 
# to a Listbox. It also contains two buttons to delete items using stacks or queues.
# ------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
from validaciones import Validar

class RFC:
    def __init__(self):
        self.val = Validar()  # Instancia de la clase validaciones / Validator instance
        self.ventana = Tk()  # Ventana principal / Main window
        self.lis=[]  # Lista auxiliar (no usada directamente) / Auxiliary list
        ancho = 550  # Ancho de ventana / Window width
        alto = 250   # Alto de ventana / Window height
        pantalla_ancho = self.ventana.winfo_screenwidth()   # Ancho de pantalla / Screen width
        pantalla_alto = self.ventana.winfo_screenheight()   # Alto de pantalla / Screen height
        x = (pantalla_alto//2)- (ancho//2)  # Posición X centrada / Center X position
        y = (pantalla_ancho//2)- (alto//2)  # Posición Y centrada / Center Y position
        self.ventana.geometry(f"{ancho}x{alto}+{x+350}+{y-350}")  # Posicionar ventana / Position window

    def inicio(self):
        # -------------------- Cajas de texto / Input boxes --------------------
        self.nombre = Entry(self.ventana)  # Caja para nombre / Name entry
        self.nombre.place(x=20,y=60,width=100)
        self.paterno = Entry(self.ventana)  # Caja para apellido paterno / Paternal surname
        self.paterno.place(x=140,y=60,width=100)
        self.materno = Entry(self.ventana)  # Caja para apellido materno / Maternal surname
        self.materno.place(x=260,y=60,width=100)
        self.dia = Entry(self.ventana)  # Día / Day
        self.dia.place(x=20,y=130,width=100)
        self.mes = Entry(self.ventana)  # Mes / Month
        self.mes.place(x=140,y=130,width=100)
        self.año = Entry(self.ventana)  # Año / Year
        self.año.place(x=260,y=130,width=100)

        # -------------------- Etiquetas / Labels --------------------
        Label(self.ventana, text="DATOS PERSONALES").place(x=125,y=10)
        Label(self.ventana, text="Nombre").place(x=20,y=35)
        Label(self.ventana, text="Apellido paterno").place(x=140,y=35)
        Label(self.ventana, text="Apellido materno").place(x=260,y=35)
        Label(self.ventana, text="Dia").place(x=20,y=105)
        Label(self.ventana, text="Mes").place(x=140,y=105)
        Label(self.ventana, text="Año").place(x=260,y=105)

        # -------------------- Listbox / Lista visual --------------------
        self.lista = Listbox(self.ventana, height=10, width=15, bg='grey',
                                activestyle="dotbox", fg="Black")
        self.lista.place(x=380, y=20,width=150)

        # -------------------- Botones / Buttons --------------------
        Button(self.ventana,text="Agregar",command=self.agregar).place(x=40,y=170,width=55)  # Botón para agregar RFC / Add RFC button
        Button(self.ventana,text="Eliminar",command=self.Eliminar).place(x=270,y=170,width=55)  # Botón para eliminar / Delete button
        self.modo = StringVar(value="Pilas")  # Variable para el modo / Mode variable
        Radiobutton(self.ventana,text="pilas",variable=self.modo,value="Pilas").place(x=140,y=170)  # Opción pila / Stack option
        Radiobutton(self.ventana,text="colas",variable=self.modo,value="colas").place(x=190,y=170)  # Opción cola / Queue option
        self.ventana.mainloop()  # Iniciar bucle de ventana / Start mainloop

    def agregar(self):
        # Obtener los datos desde las cajas / Get data from entries
        nombre = self.nombre.get() 
        paterno = self.paterno.get()
        materno = self.materno.get()
        año = self.año.get()
        dia = self.dia.get()
        mes = self.mes.get()

        # -------------------- Validaciones / Validations --------------------
        if año=="" or mes=="" or dia=="" or nombre=="" or paterno==""or materno=="":
            messagebox.showerror("Error","Falta un dato")  # Campo vacío / Missing field
            self.nombre.delete(0,END)
            self.paterno.delete(0,END)
            self.materno.delete(0,END)
            self.año.delete(0,END)
            self.dia.delete(0,END)
            self.mes.delete(0,END)
        else:
            if len(dia)==1:
                dia = (f'0{dia}')  # Agrega cero si día tiene un dígito / Add leading zero if day has one digit
            if len(año)!=4 or len(mes)!=2 or len(dia)!=2:
                messagebox.showerror("Error","Formato de fecha erroneo")  # Formato incorrecto / Wrong date format
                self.año.delete(0,END)
                self.dia.delete(0,END)
                self.mes.delete(0,END)
            else:
                if len(dia)==1:
                    dia = (f'0{dia}')
                # Verifica que los campos de fecha sean numéricos / Check that date fields are numeric
                if (self.val.ValidarNumeros(año))==False or (self.val.ValidarNumeros(dia))==False or (self.val.ValidarNumeros(mes))==False:
                    messagebox.showerror("Error","No son numeros")  # No numéricos / Not numbers
                    self.año.delete(0,END)
                    self.dia.delete(0,END)
                    self.mes.delete(0,END)
                # Verifica que los nombres sean letras / Check that names are letters
                if (self.val.ValidarNombre(paterno))==False or (self.val.ValidarNombre(materno))==False or (self.val.ValidarNombre(nombre))==False:
                    self.nombre.delete(0,END)
                    self.paterno.delete(0,END)
                    self.materno.delete(0,END)

                else:
                    if int(mes)>12 or int(dia)>31:
                        messagebox.showerror("Error","Fecha erronea")  # Día o mes fuera de rango / Invalid day or month
                        self.dia.delete(0,END)
                        self.mes.delete(0,END)
                    else:   
                        if " " in paterno:
                            paterno = paterno.split(" ")[-1]  # Si hay doble apellido, toma el último / If double surname, take last
                        print(paterno)
                        bandera = False  # Bandera no utilizada / Unused flag
                        if bandera == True:
                            if not (paterno[1] in ("a,e,i,o,u")): 
                                paterno= paterno[0]+paterno[2]
                                bandera = False
                            else:
                                bandera = True
                        # Construcción del RFC / RFC construction
                        rfc = (f'{paterno[0:2]}{materno[0]}{nombre[0]}{año[2:]}{mes}{dia}')
                        rfc = rfc.upper()  # Convertir a mayúsculas / Convert to uppercase
                        self.lista.insert(END,rfc)  # Agregar RFC a la lista / Add RFC to list

                        # Limpiar las cajas / Clear all entry boxes
                        self.año.delete(0,END)
                        self.dia.delete(0,END)
                        self.mes.delete(0,END)
                        self.nombre.delete(0,END)
                        self.paterno.delete(0,END)
                        self.materno.delete(0,END)

    def Eliminar(self):
        # Eliminar elementos de la lista según el modo / Delete items based on mode
        if self.lista.size()<=0:
            messagebox.showerror("Error", "La lista esta vacia")  # Lista vacía / List is empty
            return
        if self.modo.get()=='Pilas':
            # último que entra, primero que sale / last in, first out (stack)
            self.lista.delete(self.lista.size()-1)
        else:
            # primero que entra, primero que sale / first in, first out (queue)
            self.lista.delete(0)

# Punto de entrada principal / Main entry point
if __name__=="__main__":
    app = RFC()  # Crear instancia / Create instance
    app.inicio()  # Ejecutar aplicación / Run application
