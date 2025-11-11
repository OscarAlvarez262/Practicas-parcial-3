from tkinter import *
from tkinter import messagebox
from validaciones import Validar
import numpy as np  

class Principal():
    def __init__(self):
        self.val = Validar()  # Instancia del validador / Validator instance
        self.ven = Tk()  # Crear ventana principal / Create main window
        self.lis=[]  # Lista auxiliar / Auxiliary list
        ancho = 300  # Ancho de la ventana / Window width
        alto = 210   # Alto de la ventana / Window height
        pantalla_ancho = self.ven.winfo_screenwidth()  # Ancho de pantalla / Screen width
        pantalla_alto = self.ven.winfo_screenheight()  # Alto de pantalla / Screen height
        x = (pantalla_alto//2)- (ancho//2)  # Calcular posición X / Calculate X position
        y = (pantalla_ancho//2)- (alto//2)  # Calcular posición Y / Calculate Y position
        self.ven.geometry(f"{ancho}x{alto}+{x+350}+{y-350}")  # Definir tamaño y posición / Set window size and position

    def validarcaja(self):
        valor = self.dato.get()  # Obtener el valor del campo de entrada / Get entry value
        if (self.val.ValidarNumeros(valor)):  # Verifica si es un número / Check if it’s a number
            if (self.val.ValidarEntradas(valor)):  # Verifica si tiene dos dígitos / Check if it has two digits
                self.lista.insert(self.lista.size() + 1, valor)  # Insertar valor en la lista / Insert value into list
                self.dato.delete(0,END)  # Limpiar caja de texto / Clear input box
                self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')  # Actualizar contador / Update counter
            else:
                messagebox.showerror("Incorrecto", "Solo se permite dos digitos")  # Error si supera 2 dígitos / Error if over 2 digits
                self.dato.delete(0,END)
        else:
            messagebox.showerror("Incorrecto", "No es un numero")  # Error si no es número / Error if not a number
            self.dato.delete(0,END)

    def inicio(self):
        self.dato = Entry(self.ven)  # Campo de texto / Text entry field
        self.dato.place(x=50,y=20)
        self.modo = StringVar(value="Pilas")  # Modo inicial: pilas / Default mode: stack
        self.orden = StringVar(value="Mayor")  # Orden inicial: mayor / Default order: descending
        Radiobutton(self.ven,text="pilas",variable=self.modo,value="Pilas").place(x=50,y=50)  # Radio para pilas / Stack option
        Radiobutton(self.ven,text="colas",variable=self.modo,value="colas").place(x=100,y=50)  # Radio para colas / Queue option
        Radiobutton(self.ven,text="Mayor",variable=self.orden,value="Mayor").place(x=50,y=135)  # Orden descendente / Descending order
        Radiobutton(self.ven,text="Menor",variable=self.orden,value="Menor").place(x=110,y=135)  # Orden ascendente / Ascending order
        Button(self.ven,text="Validar",command=self.validarcaja).place(x=90,y=80,width=55)  # Botón para validar / Validate button
        Button(self.ven,text="Eliminar",command=self.eliminardato).place(x=90,y=110,width=55)  # Botón eliminar / Delete button
        Button(self.ven,text="Ordenar",command=self.ordenar).place(x=90,y=160,width=55)  # Botón ordenar / Sort button
        self.lista = Listbox(self.ven, height=10, width=15, bg='grey',
                                activestyle="dotbox", fg="Black")  # Lista visual / Display list
        self.lista.place(x=195, y=20)
        self.label= Label(self.ven, text="Elementos en la lista: 0")  # Etiqueta contador / Counter label
        self.label.place(x=10,y=190)
        self.ven.mainloop()  # Iniciar bucle principal / Start main loop

    def eliminardato(self):
        if self.lista.size()<=0:
            messagebox.showerror("Error", "La lista esta vacia")  # Mensaje si está vacía / Error if list is empty
            return
        if self.modo.get()=='Pilas':
            # último que entra, primero que sale / last in, first out (stack)
            self.lista.delete(self.lista.size()-1)
        else:
            # primero que entra, primero que sale / first in, first out (queue)
            self.lista.delete(0)
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')  # Actualizar etiqueta / Update label

    def ordenar(self):
        self.lis = list(self.lista.get(0,END))  # Obtener lista actual / Get current list
        if len(self.lis)<=0:
            messagebox.showerror("Error", "La lista esta vacia")  # Error si lista vacía / Error if list empty
        if self.orden.get()=='Mayor':
            # método de selección (orden descendente) / selection sort (descending)
            p = 0
            for i in range(0,len(self.lis)):
                aux = int(self.lis[i])
                p=i
                for x in range(i,len(self.lis)):
                    if aux < int(self.lis[x]):  # Buscar el mayor / Find the largest
                        aux = int(self.lis[x])
                        p = x
                self.lis[p] = self.lis[i]
                self.lis[i] = str(aux)
            self.lista.delete(0,END) 
            for i in self.lis:
                self.lista.insert(self.lista.size()+1,i)  # Insertar ordenada / Insert sorted list
        else:   
            # método burbuja (orden ascendente) / bubble sort (ascending)
            for i in range(0,len(self.lis)):
                for x in range(0,len(self.lis)-1):
                    if self.lis[x]>self.lis[x+1]:  # Comparar e intercambiar / Compare and swap
                        aux = self.lis[x]
                        self.lis[x]= self.lis[x+1]
                        self.lis[x+1]= aux
            self.lista.delete(0,END) 
            for i in self.lis:
                self.lista.insert(self.lista.size()+1,i)  # Insertar ordenada / Insert sorted list       


if __name__=='__main__':
    app = Principal()  # Crear instancia / Create instance
    app.inicio()  # Ejecutar aplicación / Run app
