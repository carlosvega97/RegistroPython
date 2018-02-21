'''
Created on 20 feb. 2018

@author: Pablo Vega
'''

from tkinter import *
from msilib.schema import ComboBox
from tkinter import ttk

ventana = Tk()

imagen1 = PhotoImage(file="paisaje.gif")
display = Label(ventana, image=imagen1).place(x = 0, y = 0)
    
ventana.geometry("600x600+400+100")
ventana.title("Agencia de vajes")
etiqueta = Label(ventana, text = 'Viajes de senderismo', font = ("Agency FB",30))
etiqueta.pack()

etiqueta2 = Label(ventana, text = 'Seleccione la excursion que desea realizar: ', bd = 8).place(x = 40, y = 70)
select = IntVar()
RdB = Radiobutton(ventana, text="Monte Abantos", variable = select, value=1).place(x = 40, y = 100)
RdB2 = Radiobutton(ventana, text="La Pedriza", variable = select, value=2).place(x = 40, y = 120)
RdB3 = Radiobutton(ventana, text="Las dehesas de Cercedilla", variable = select, value=3).place(x = 40, y = 140)
RdB4 = Radiobutton(ventana, text="La Cabrera-Pico de la Miel", variable = select, value=4).place(x = 40, y = 160)


etiqueta3 = Label(ventana, text = 'Seleccione los objetos que desea llevar: ', bd = 8).place(x = 350, y = 70)


select1 = StringVar()
select2 = StringVar()
select3 = StringVar()
select4 = StringVar()
select5 = StringVar()
select6 = StringVar()
select7 = StringVar()
select8 = StringVar()
chb = Checkbutton (ventana, text = "Mochila", variable = select1, onvalue = "Mochila", offvalue = "").place(x = 350, y = 100)
chb2 = Checkbutton (ventana, text = "Linterna", variable = select2, onvalue ="Linterna", offvalue = "").place(x = 350, y = 120)
chb3= Checkbutton (ventana, text = "GPS", variable = select3, onvalue = "GPS", offvalue = "").place(x = 350, y = 140)
chb4 = Checkbutton (ventana, text = "Mapa", variable = select4, onvalue = "Mapa", offvalue = "").place(x = 350, y = 160)
chb5 = Checkbutton (ventana, text = "Prismáticos", variable = select5, onvalue ="Prismáticos", offvalue = "").place(x = 350, y = 180)
chb6 = Checkbutton (ventana, text = "Cantimplora", variable = select6, onvalue ="Cantimplora", offvalue = "").place(x = 350, y = 200)
chb7 = Checkbutton (ventana, text = "Botiquín", variable = select7, onvalue ="Botiquín", offvalue = "").place(x = 350, y = 220)
chb8 = Checkbutton (ventana, text = "Crema_Solar", variable = select8, onvalue ="Crema_Solar", offvalue = "").place(x = 350, y = 240)

etiqueta = Label(ventana, text = 'Informacion personal', font = ("Agency FB",20)).place(x = 40, y = 200)

nombre = StringVar()
txtNombre = Entry(ventana, textvariable = nombre).place(x = 100, y = 280)
lblnombre = Label(text = "Nombre:").place(x = 40, y = 280)

apellidos = StringVar()
txtApellido = Entry(ventana, textvariable = apellidos).place(x = 355, y = 280)
lblnombre = Label(text = "Apellido:").place(x = 295, y = 280)

direccion = StringVar()
txtDireccion = Entry(ventana, textvariable = direccion).place(x = 100, y = 310)
lblnombre = Label(text = "Direccion:").place(x = 40, y = 310)

telefono = StringVar()
txtTelefono = Entry(ventana, textvariable = telefono).place(x = 355, y = 310)
lblnombre = Label(text = "Telefono:").place(x = 295, y = 310)


cbx = ttk.Combobox(values=("Madrid", "Alcobendas", " San Sebastián de los Reyes", " Algete", "Pozuelo", " Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón"))
cbx.set("Madrid")
cbx.place(x = 85, y = 345)


from tkinter import messagebox

def mensaje():
    messagebox.showinfo("Titulo: Enhorabuena", "Sus datos no se van a poder guardar")


lista = Listbox(ventana,width=75)
lista.place(x =100,y = 400)
     
     
def Guardado():
    lista.insert(END,("Nombre:",nombre.get(),apellidos.get()))
    lista.insert(END,("Excursion:",select.get()))
    lista.insert(END,("Direccion:",direccion.get()))
    lista.insert(END,("Municipio:",cbx.get()))
    lista.insert(END,("Telefono:",telefono.get()))
    lista.insert(END,("Accesorios:",select1.get(),select2.get(),select3.get(),select4.get(),select5.get(),select6.get(),select7.get(),select8.get()))
    lista.insert(END,())
     
     
boton1 = Button(ventana, text = 'Guardar datos', command = Guardado).place(x = 365, y = 345)






ventana.mainloop()