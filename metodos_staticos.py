from re import *
# metos para usar en el modulo modelo, pero que no pertenecen al modulo en si
class validar():
    @staticmethod
    def validar_producto(producto):
        patron="^[A-Za-záéíóú1-9Ññ0.,\s\*]*$"
        if match(patron,producto):
            return True
        
        else:
            return False

class Vaciar():
    @staticmethod
    def vaciar(producto,precio,stock):
        producto.set("")
        precio.set(0)
        stock.set(0)

class actualizar():
    @staticmethod
    def actualizar_treeview(tree,my_base):
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        sql = "SELECT * FROM producto ORDER BY id ASC"
        cursor=my_base.cursor()
        datos=cursor.execute(sql)
        resultado = datos.fetchall()
        for fila in resultado:
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2],fila[3]))