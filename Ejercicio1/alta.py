# Juan para revisar el ejercicio con si no usas sqlite quita el # de mysql y ponsela a sqlite asi puedes ver el codigo

# import mysql.connector
import sqlite3
import re

# validacion & base datos

id = []

def val_reg(tit, des, Ent1, Ent2, tree):
    patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
    print(patron.match(tit.get()))
    if patron.match(tit.get()) is None:
        print('la has cagado macho, escribe bien')
    else:
        base = sqlite3.connect('baseprueba3.db')
        print("Base creada")
        cursor = base.cursor()
        # base = mysql.connector.connect(host="localhost", user="root", passwd="")
        # cursor = base.cursor()
        # cursor.execute("CREATE DATABASE baseprueba3")
        try:
            cursor.execute("CREATE TABLE producto(id integer PRIMARY KEY NOT NULL, titulo VARCHAR NOT NULL, descripcion VARCHAR NOT NULL)")
        except:
            pass

        sql = "INSERT INTO producto (titulo, descripcion) VALUES (?, ?)"
        # sql = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
        datos = (tit.get(), des.get())
        cursor.execute(sql, datos)
        base.commit()

        sql_id = "SELECT * FROM producto"
        cursor.execute(sql_id)
        ingresos = cursor.fetchall()
        print(ingresos)

        x = tree.get_children()
        for element in x:
            tree.delete(element)

        global id
        for i in ingresos:
            print(i)
            id = i
            tree.insert("", 0, text=str(id[0]), values=(id[1], id[2]))
        Ent1.delete(0, "end")
        Ent2.delete(0, "end")



def borrar_reg(tree):
    global id
    id = tree.focus()
    print(tree.item(id)["text"])  # Imprime el numero de entrada
    a = tree.item(id)["text"]   # Le asigno la entrada completa a variable a
    print(type(a))
    tree.delete(id)  # borro la entrada del tree pero no de la db
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    base = sqlite3.connect('baseprueba3.db')
    # base = mysql.connector.connect(host="localhost", user="root", passwd="", baseprueba3)
    cursor = base.cursor()
    cursor.execute("DELETE FROM producto WHERE ID=" + a)
    base.commit()
    base.close()
    print(cursor.rowcount, "registro ", id, " borrado")



def editar_reg(tree):
    global id
    x = tree.get_children()
    for element in x:  # Cambiando los children del root item
        tree.item(element, text=str(id[0]), values=(id[1], id[2]))

    base = sqlite3.connect('baseprueba3.db')
    # base = mysql.connector.connect(host="localhost", user="root", passwd="", baseprueba3)
    cursor = base.cursor()
    sql = 'UPDATE producto SET producto = ? where id = ?'
    datos = (id[1])
    cursor.execute(sql, datos)
    base.commit()
    base.close()
    print(cursor.rowcount, "Cantidad de registros afectados")
