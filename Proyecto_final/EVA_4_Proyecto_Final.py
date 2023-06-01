import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def agregar_objeto_perdido(nombre, categoria, descripcion):
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Isai1622?",
        database="ñññ"
    )
    cursor = conexion.cursor()

    # Insertar los valores en la base de datos
    consulta = "INSERT INTO objetos_perdidos (nombre, categoria, descripcion) VALUES (%s, %s, %s)"
    valores = (nombre, categoria, descripcion)
    cursor.execute(consulta, valores)
    conexion.commit()

    # Cerrar la conexión
    cursor.close()
    conexion.close()


def eliminar_objeto_perdido(id_objeto):
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Isai1622?",
        database="ñññ"
    )
    cursor = conexion.cursor()

    # Eliminar el objeto de la base de datos
    consulta = "DELETE FROM objetos_perdidos WHERE id = %s"
    valor = (id_objeto,)
    cursor.execute(consulta, valor)
    conexion.commit()

    # Cerrar la conexión
    cursor.close()
    conexion.close()

def consultar_objetos_perdidos():
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Isai1622?",
        database="ñññ"
    )
    cursor = conexion.cursor()

    # Realizar la consulta SELECT
    consulta = "SELECT * FROM objetos_perdidos"
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    # Crear una nueva ventana para mostrar los resultados
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados de la consulta")
    ventana_resultados.configure(bg="#F0F0F0")
    ventana_resultados.geometry("600x400")
    ventana_resultados.resizable(False, False)

    # Centrar la ventana de resultados
    center_window(ventana_resultados)

    # Crear el widget Treeview para mostrar los resultados en una tabla
    treeview = ttk.Treeview(ventana_resultados)
    treeview["columns"] = ("id", "nombre", "categoria", "descripcion")

    # Establecer los encabezados de la tabla
    treeview.heading("id", text="ID", anchor=tk.W)
    treeview.heading("nombre", text="Nombre", anchor=tk.W)
    treeview.heading("categoria", text="Categoría", anchor=tk.W)
    treeview.heading("descripcion", text="Descripción", anchor=tk.W)

    # Configurar el tamaño de las columnas
    treeview.column("id", width=50, anchor=tk.W)
    treeview.column("nombre", width=100, anchor=tk.W)
    treeview.column("categoria", width=100, anchor=tk.W)
    treeview.column("descripcion", width=350, anchor=tk.W)

    # Alinear todas las columnas a la izquierda
    for column in treeview["columns"]:
        treeview.column(column, anchor=tk.W)

    # Agregar los resultados a la tabla
    for resultado in resultados:
        treeview.insert("", "end", values=resultado)

    # Mostrar la tabla en la ventana
    treeview.pack(fill="both", expand=True)

    def eliminar_objeto():
        # Obtener el ID del objeto seleccionado
        seleccion = treeview.focus()
        if seleccion:
            id_objeto = treeview.item(seleccion)["values"][0]

            # Mostrar un mensaje de confirmación antes de eliminar el objeto
            confirmacion = tk.messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar este objeto?")
            if confirmacion:
                # Eliminar el objeto de la base de datos
                eliminar_objeto_perdido(id_objeto)
                # Eliminar el objeto de la tabla
                treeview.delete(seleccion)

    # Botón para eliminar un objeto
    eliminar_btn = ttk.Button(ventana_resultados, text="Eliminar", command=eliminar_objeto)
    eliminar_btn.pack(pady=10)

    # Cerrar la conexión
    cursor.close()
    conexion.close()

def abrir_ventana_objetos_perdidos():
    global ventana_objetos_perdidos  # Declarar la variable como global
    # Cerrar la ventana del menú principal
    root.withdraw()

    # Crear una nueva ventana para "Objetos perdidos"
    ventana_objetos_perdidos = tk.Toplevel()
    ventana_objetos_perdidos.title("Objetos perdidos")
    ventana_objetos_perdidos.configure(bg="#F0F0F0")
    ventana_objetos_perdidos.geometry("400x400")
    ventana_objetos_perdidos.resizable(False, False)

    # Centrar la ventana de "Objetos perdidos"
    center_window(ventana_objetos_perdidos)

    # Etiqueta centrada con el título "Objetos perdidos"
    titulo_label = tk.Label(ventana_objetos_perdidos, text="Objetos perdidos", font=("Arial", 16))
    titulo_label.pack(pady=10)

    # Campos para agregar objetos perdidos
    nombre_label = ttk.Label(ventana_objetos_perdidos, text="Nombre:")
    nombre_label.pack()
    nombre_entry = ttk.Entry(ventana_objetos_perdidos)
    nombre_entry.pack()

    categoria_label = ttk.Label(ventana_objetos_perdidos, text="Categoría:")
    categoria_label.pack()
    categoria_entry = ttk.Entry(ventana_objetos_perdidos)
    categoria_entry.pack()

    descripcion_label = ttk.Label(ventana_objetos_perdidos, text="Descripción:")
    descripcion_label.pack()
    descripcion_entry = ttk.Entry(ventana_objetos_perdidos)
    descripcion_entry.pack()

    # Botón para agregar objetos perdidos
    agregar_btn = ttk.Button(ventana_objetos_perdidos, text="Agregar",
                             command=lambda: agregar_objeto_perdido(nombre_entry.get(), categoria_entry.get(), descripcion_entry.get()))
    agregar_btn.pack(pady=10)

    # Botón para regresar al menú principal
    regresar_btn = ttk.Button(ventana_objetos_perdidos, text="Regresar al Menú Principal", command=regresar_al_menu)
    regresar_btn.pack(pady=10)

def regresar_al_menu():
    # Cerrar la ventana de "Objetos perdidos"
    ventana_objetos_perdidos.destroy()

    # Mostrar la ventana del menú principal
    root.deiconify()

def main_menu():
    global root
    root = tk.Tk()
    root.title("Menú principal")
    root.configure(bg="#F0F0F0")
    root.geometry("400x400")
    root.resizable(False, False)

    # Centrar la ventana principal
    center_window(root)

    # Etiqueta centrada con el título "Menú principal"
    titulo_label = tk.Label(root, text="Menú principal", font=("Arial", 16))
    titulo_label.pack(pady=10)

    # Botón para abrir la ventana de "Objetos perdidos"
    abrir_ventana_btn = ttk.Button(root, text="Ir a Objetos perdidos", command=abrir_ventana_objetos_perdidos)
    abrir_ventana_btn.pack(pady=10)

    # Botón para consultar objetos perdidos
    consultar_btn = ttk.Button(root, text="Consultar", command=consultar_objetos_perdidos)
    consultar_btn.pack(pady=10)

    root.mainloop()

# Ejecutar el menú principal
main_menu()