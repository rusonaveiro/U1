from tkinter import *
from tkinter import ttk
from Ejercicio1.alta import *

root = Tk()
root.title("Tarea Poo")

f = Frame(root)
f.config(width=1020,height=1020)
f.grid(row=10, column=0, columnspan=4)

####################################################################################

# etiquetas
superior = Label(root, text="Ingrese sus datos", bg="orchid", fg="white", width=40)
titulo = Label(root, text="Titulo")
descripcion = Label(root, text="Descripcion")
registros = Label(root, text="Mostrar registros existentes", bg='grey', width=40)

####################################################################################

# entradas
def entradas(valor, ancho, fila, columna):
    entrada = Entry(root, textvariable=valor, width=ancho)
    entrada.grid(row=fila, column=columna)
    return entrada

tit = StringVar()
des = StringVar()

Ent1 = entradas(tit, 15, 1, 1)
Ent2 = entradas(des, 15, 2, 1)

####################################################################################

# crea db, tabla y registros
boton_alta = Button(root, text="Alta", command=lambda: val_reg(tit, des, Ent1, Ent2, tree))
boton_borrar = ttk.Button(root, text="Borrar", command=lambda: borrar_reg(tree))

####################################################################################

tree = ttk.Treeview(f)
tree["columns"] = ("col1", "col2")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=150, minwidth=80)
tree.column("col2", width=150, minwidth=80)

tree.heading("#0", text="ID")
tree.heading("col1", text="Título")
tree.heading("col2", text="Descripción")

# Scroll Vertical
scrolvert = Scrollbar(f, command=tree.yview, orient='vertical')
scrolvert.grid(row=10, column=4, sticky=N+S)
tree.configure(yscrollcommand=scrolvert.set)

# Scroll Horizontal (NO FUNCIONA)
scrolhoriz = Scrollbar(f, command=tree.xview, orient='horizontal')
scrolhoriz.grid(row=11, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
tree.configure(xscrollcommand=scrolhoriz.set)

####################################################################################

# posiciones en la tabla
superior.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
titulo.grid(row=1, column=0, sticky='w')
descripcion.grid(row=2, column=0, sticky='w')
registros.grid(row=3, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
boton_alta.grid(row=20, column=0)
boton_borrar.grid(row=20, column=2)
tree.grid(row=10, column=0, columnspan=4)

####################################################################################

root.mainloop()