import sqlite3

class sqlite3_base():
    base = sqlite3
    cursor = None

    def __init__(self):
        self.base = sqlite3.connect('baseprueba3.db')
            print("Base creada")
        self.cursor = self.base.cursor()
            try:
                self.cursor.execute("CREATE TABLE producto(id integer PRIMARY KEY NOT NULL, titulo VARCHAR NOT NULL, descripcion VARCHAR NOT NULL)")
            except:
                pass

    def insertar_db(self, tit, des):
        sql = "INSERT INTO producto (titulo, descripcion) VALUES (?, ?)"
        datos = (tit.get(), des.get())
        self.cursor.execute(sql, datos)
        self.base.commit()
        print(self.cursor.rowcount, "Cantidad de registros insertados")
        self.tree_insertar()

    def atrapar_db(self):
        sql_id = "SELECT * FROM producto"
        self.cursor.execute(sql_id)
        ingresos = self.cursor.fetchall()
        print(ingresos)
        self.tree_atrapar()

    def update_db(self, tit, des, a):
        sql = "UPDATE producto SET titulo=?, descripcion=? WHERE id = " + a
        datos = (tit.get(), des.get())
        self.cursor.execute(sql, datos)
        self.base.commit()
        print(self.cursor.rowcount, "Cantidad de registros afectados")

    def borrar_db(self, a):
        sql = "DELETE FROM producto WHERE ID=" + a
        self.cursor.execute(sql)
        self.base.commit()
        print(self.cursor.rowcount, "registro ", id, " borrado")









