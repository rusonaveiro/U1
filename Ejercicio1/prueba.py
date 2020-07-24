def editar_reg(tree):
    patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
    print(patron.match(tit.get()))
    if patron.match(tit.get()) is None:
        print('la has cagado macho, escribe bien')
    else:
        base = sqlite3.connect('baseprueba3.db')

def editar_reg(tree):
    base = sqlite3.connect('baseprueba3.db')
    # base = mysql.connector.connect(host="localhost", user="root", passwd="", baseprueba3)
    cursor = base.cursor()
    sql_id = "SELECT * FROM producto"
    cursor.execute(sql_id)
    ingresos = cursor.fetchall()
    print(ingresos)

    global id
    id = tree.focus()
    x = tree.get_children()
    for element in x:
        tree.delete(element)


    for i in ingresos:
        print(i)
        id = i
        tree.insert("", 0, text=str(id[0]), values=(id[1], id[2]))


def editar_reg(tree):
    global id
    id = tree.focus()
    a = tree.item(id)["text"]   # Le asigno ese registro completo a la variable a
    x = tree.get_children()
    for element in x:  # Cambiando los children del root item
        tree.delete(element)
        tree.insert("", 0, text=str(id[0]), values=(id[1], id[2]))

    base = sqlite3.connect('baseprueba3.db')
    # base = mysql.connector.connect(host="localhost", user="root", passwd="", baseprueba3)
    cursor = base.cursor()
    sql = 'UPDATE producto SET producto = ? where id = ?'
    datos = (id[1])
    cursor.execute(sql, datos)
    base.commit()
    base.close()
    print(cursor.rowcount, "Cantidad de registros afectados")
