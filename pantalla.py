from tkinter import *
from tkinter import ttk
from modelo import Control, actualizar
from observador import * 
class Pantalla():
        def __init__(self,base):
                self._observers = []
                obs = ConcreteObserverA()
                self.registrar_observador(obs)
                self.my_base=base
                self.master=Tk()
                self.producto=StringVar()
                self.precio=DoubleVar()
                self.stock=DoubleVar() 
                self.tree=ttk.Treeview(self.master)
                self.abmc=Control()
                self.componente_pantalla()

        def registrar_observador(self,observador):
                self._observers.append(observador)

        def quitar_observador(self,observador):
                self._observers.remove(observador)

        def notificar_observador(self, mensaje):
                for observador in self._observers:
                        observador.update(mensaje)


#####################################################################################################################3
        def componente_pantalla(self,):
                self.master.geometry("500x400")
                self.master.title("CRUD")

        ###################################################################################################
                label_descripcion=Label(self.master,text="descripcion")
                label_descripcion.place(x=125)
                label_precio=Label(self.master,text="precio")
                label_precio.place(x=300)
                label_sotck=Label(self.master,text="stok")
                label_sotck.place(x=350)
                entry_descripcion=Entry(self.master, textvariable=self.producto)
                entry_descripcion.place(x=0,width=300,y=25)
                entry_precio=Entry(self.master,textvariable=self.precio)
                entry_precio.place(x=300,width=100,y=25)
                entry_stock=Entry(self.master,textvariable=self.stock)
                entry_stock.place(x=350,width=100,y=25)
        #######################################################################################################
                self.tree["column"]=("col1","col2","col3")
                self.tree.column("#0",width=15)
                self.tree.column("col1", width=50)
                self.tree.column("col2", width=15)
                self.tree.column("col3", width=15)
                self.tree.heading("#0", text="ID")
                self.tree.heading("col1", text="Producto")
                self.tree.heading("col2", text="precio")
                self.tree.heading("col3", text="stock")
                self.tree.place(x=0,width=450,y=95) 
        ###########################################################################################################
                
                boton_alta=Button(self.master, text="alta", command=lambda:self.abmc.alta(self.producto,self.precio,self.tree,self.stock,self.my_base, self))
                boton_alta.place(x=0,width=100,y=55)
                boton_borrar=Button(self.master, text="borrar",command=lambda:self.abmc.baja(self.tree,self.producto,self.precio,self.stock,boton_modificar,boton_alta,boton_borrar,self.my_base),state=DISABLED)
                boton_borrar.place(x=101,width=100,y=55)
                boton_modificar=Button(self.master, text="modificar", command=lambda:self.abmc.modificar(self.tree,self.producto,self.precio,self.stock,boton_modificar,boton_alta,boton_borrar,self.my_base),state=DISABLED)
                boton_modificar.place(x=201,width=100,y=55)
                boton_select=Button(self.master, text="seleccionar", command=lambda:self.abmc.muestra(self.tree,self.producto,self.precio,self.stock,boton_modificar,boton_alta,boton_borrar))
                boton_select.place(x=301,width=100,y=55)
                
        ##########################################################################################################
                actualizar.actualizar_treeview(self.tree,self.my_base)   
                self.menubar=Menu(self.master,tearoff=0)
                self.menubar.add_command(label="salir",command=self.master.quit)
                self.master.config(menu=self.menubar)
                self.master.mainloop()
        

