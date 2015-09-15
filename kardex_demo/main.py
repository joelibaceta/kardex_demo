from tkinter import *  #tkinter es la ibrería usaba para crear el GUI
def agregar():
	genProducto = entradaNom.get() 
	espacio = "                                     "
	genProd = entradaCod.get() + espacio +"$ "+ entradaPre.get()
	lstProductos.insert(END,genProducto)
	lstProd.insert(END,genProd)

ventana = Tk()
ventana.geometry("650x400+300+150")
ventana.title("Registo de productos")
#Creacion de etiquetas (nombre de cada sección)
lbNombreP = Label(text="Nombre del producto",font=("Cambria",11)).place(x=35, y=15)
lbCodigo = Label(text="Código",font=("Cambria",11)).place(x=265, y=15)
lbPrecio = Label(text="Precio",font=("Cambria",11)).place(x=425, y=15)
lbMostrar = Label(text="Productos",font=("Cambria",11)).place(x=35,y=100)
#Lista
lstProductos = Listbox(ventana,width=50,height=14)
lstProductos.place(x=35,y=100)
lstProd = Listbox(ventana,width=60,height=14)
lstProd.place(x=265,y=100)
#Creando variable para guardar las entradas
entradaNom = StringVar()
entradaCod = StringVar()
entradaPre = StringVar()
#Creando Entradas
txtNombre = Entry(ventana,textvariable=entradaNom,width=34).place(x=35,y=40)
txtCodigo = Entry(ventana,textvariable=entradaCod,width=23).place(x=265,y=40)
txtPrecio = Entry(ventana,textvariable=entradaPre,width=23).place(x=425,y=40)
#Boton Agregar
btnAgregar = Button(ventana,text="Agregar",height=1,width=15,bg="#2E2E2E",
	fg="white",font=("Cambria",14),command=agregar).place(x=425,y=350)

ventana.mainloop()

