from tkinter import *
from tkinter import ttk
from alta_poo import sqlite3_base
import re

######################################################################################################################
##################### HE ADAPTADO UNA PARTE DE MI EJERCICIO 1 A LA CONSIGNA DE REALIZAR 2 CLASES   ###################

# Creo una clase y pongo todas las variables
class ventanita():
    root = Tk()
    f = Frame(root)
    tree = ttk.Treeview(f)
    tit = StringVar()
    des = StringVar()
    db = False
    id = []

    # Inicio los metodos
    def __init__(self):
        self.db = sqlite3_base()
        self.forma_tk()
        self.etiquetas()
        self.input()
        self.botones()
        self.arbol()

    # Moldeo el frame
    def forma_tk(self):
        self.root.title("Tarea Poo")
        self.f.config(width=1020, height=1020)
        self.f.grid(row=10, column=0, columnspan=4)

    # Creo los Label
    def etiquetas(self):
        self.superior = Label(self.root, text="Ingrese sus datos", bg="orchid", fg="white", width=40)
        self.titulo = Label(self.root, text="Titulo")
        self.descripcion = Label(self.root, text="Descripcion")
        self.registros = Label(self.root, text="Mostrar registros existentes", bg='grey', width=40)

        self.superior.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W + E)
        self.titulo.grid(row=1, column=0, sticky='w')
        self.descripcion.grid(row=2, column=0, sticky='w')
        self.registros.grid(row=3, column=0, columnspan=4, padx=1, pady=1, sticky=W + E)

    # Creo las entradas
    def entradas(self, valor, ancho, fila, columna):
        self.entrada = Entry(self.root, textvariable=valor, width=ancho)
        self.entrada.grid(row=fila, column=columna)
        return entrada

    # Creo los input que activan metodo entradas
    def input(self):
        Ent1 = self.entradas(self.tit, 15, 1, 1)
        Ent2 = self.entradas(self.des, 15, 2, 1)

    # Defino los botones de ABM de tree
    def botones(self):
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.activar_db)
        self.boton_editar = ttk.Button(self.root, text="Actualizar", command=lambda: self.tree_modific)
        self.boton_borrar = ttk.Button(self.root, text="Borrar", command=lambda: self.tree_borrar)

        self.boton_alta.grid(row=20, column=0)
        self.boton_editar.grid(row=20, column=1)
        self.boton_borrar.grid(row=20, column=2)

    # Defino la ventana del tree
    def arbol(self):
        self.tree["columns"] = ("col1", "col2")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=150, minwidth=80)
        self.tree.column("col2", width=150, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Título")
        self.tree.heading("col2", text="Descripción")
        self.tree.grid(row=10, column=0, columnspan=4)
        self.scrolvert = Scrollbar(f, command=tree.yview, orient='vertical')
        self.scrolvert.grid(row=10, column=4, sticky=N+S)
        self.tree.configure(yscrollcommand=scrolvert.set)

######################################################################################################################
############# DESDE AQUI HACIA ABAJO NO LOGRO ADAPTAR LOS METODOS (ANTES ESTABAN DENTRO DEL MODULO ALTA ##############

    # Activo la DB validando regex
    def activar_db(self):
        if(self.db == False):
            self.db = True
            patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
            print(patron.match(self.tit.get()))
            if patron.match(self.tit.get()) is None:
                print('la has cagado macho, escribe bien')
        else:
            self.db = False

    # Entrada del tree llamando a atrapar registro db (cursor.fetchall)
    def tree_insertar(self):
        x = self.tree.get_children()
        for element in x:
            self.tree.delete(element)
        self.atrapar_db()

    # Capturo registro del tree llamandolo desde atrapar_db (cursor.fetchall)
    def tree_atrapar(self):
        global id
        for i in ingresos:
            print(i)
        id = i
        self.tree.insert("", 0, text=str(id[0]), values=(id[1], id[2]))
        Ent1.delete(0, "end")
        Ent2.delete(0, "end")

    # Borro registro del tree y llamo a la db para que tambien borre
    def tree_borrar(self):
        global id
        id = self.tree.focus()
        print(self.tree.item(id)["text"])
        a = self.tree.item(id)["text"]
        self.tree.delete(id)
        self.borrar_db(a)

    # Selecciono item y lo borro del tree, lo modifico en db llamando a update y atrapando el cursor.fetchall
    def tree_modific(self):
        global id
        id = self.tree.focus()
        a = self.tree.item(id)["text"]
        self.tree.delete(id)
        self.update_db(self.tit, self.des, a)
        self.tree_atrapar()


    root.mainloop()
