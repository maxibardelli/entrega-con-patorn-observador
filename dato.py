import sqlite3
from peewee import *
from tkinter.messagebox import *
""""
db=SqliteDatabase("base.sqlite3")
class BaseModelo(Model):
    class Meta:
        database=db
class Tabla(BaseModelo):
    descripcion=CharField(unique=True)
    precio=IntegerField()
    stock=IntegerField()
"""

class BaseDato():

    def __init__(self,base:str):
        self.my_base=sqlite3.connect(base)
        self.crear_tabal()


    def crear_tabal(self):
        try:
            cursor = self.my_base.cursor()
            sql = "CREATE TABLE producto(id integer PRIMARY KEY autoincrement, producto  text UNIQUE, precio integer, stock integer)"
            cursor.execute(sql)
            self.my_base.commit()
            showinfo(title="BASE DE DATO", message="Crear Base de Datos")
            return self.my_base
        except:
                showinfo(title="BASE DE DATO", message="Abrrir la base de dato")


