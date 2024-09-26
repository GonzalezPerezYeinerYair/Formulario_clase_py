import re
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("500x700")
ventana.title("Formulario_vr1")
ventana.config(bg="lightblue")

# Crear la variable para el radiobutton
var_genero = tk.IntVar()

# Variables para controlar si se han mostrado los mensajes
bandera_edad = False
bandera_estatura = False

# Funcion para limpiar
def limpiar_campos():
    global mensaje_edad_mostrado, mensaje_estatura_mostrado
    tb_apellidos.delete(0, tk.END)
    tb_edad.delete(0, tk.END)
    tb_estatura.delete(0, tk.END)
    tb_nombre.delete(0, tk.END)
    tb_telefono.delete(0, tk.END)
    var_genero.set(0)
    bandera_edad = False  # Reiniciar cunado se limpia
    bandera_estatura = False

def entradas_validas():
    global bandera_edad, bandera_estatura #esto me ayuda a hacer mi chiste
    nombre = tb_nombre.get()
    apellidos = tb_apellidos.get()
    edad = tb_edad.get()
    telefono = tb_telefono.get()
    estatura = tb_estatura.get()
    
    # Validacion de los nombres
    if not nombre.strip(): 
        messagebox.showerror("Error", "'Nombre' no puede estar vacio")
        return False
    elif not re.match("^[a-zA-Z\s]+$", nombre):
        messagebox.showerror("Error", "'Nombre' solo puede tener caracteres alfabeticos")
        return False
    
    # Validacion de los apellidos
    if not apellidos.strip(): 
        messagebox.showerror("Error", "'Apellidos' no puede estar vacio")
        return False
    elif not re.match("^[a-zA-Z\s]+$", apellidos):
        messagebox.showerror("Error", "'Apellidos' solo puede tener caracteres alfabeticos")
        return False

    # Validacion de la edad
    if not edad.strip(): 
        messagebox.showerror("Error", "'Edad' no puede estar vacio")
        return False
    elif not edad.isdigit():
        messagebox.showerror("Error", "Ingrese una edad valida")
        return False 
    if int(edad) > 100 and not bandera_edad:
        messagebox.showwarning("ay cabron", "Usted esta viejisimo!")
        bandera_edad = True  # Marcar que ya semostro el mensaje

    # Validacion del telefono
    if not telefono.strip(): 
        messagebox.showerror("Error", "'Telefono' no puede estar vacio")
        return False
    elif not telefono.isdigit() or len(telefono) != 10:
        messagebox.showerror("Error", "Ingrese un numero telefonico de 10 digitos numericos")
        return False 
    
    # Validacion de la estatura
    if not estatura.strip(): 
        messagebox.showerror("Error", "'Estatura' no puede estar vacio")
        return False
    try:
        estatura = float(estatura)  
    except ValueError:
        messagebox.showerror("Error", "'Estatura' tiene que ser numerico")
        return False

    if int(estatura) > 2.00 and not bandera_estatura:
        messagebox.showwarning("ay cabron", "Estas bien alto!")
        bandera_estatura = True  # Marcar que ya se ha mostrado el mensaje
        
        #validacion del genero
    if var_genero.get() == 0:
        messagebox.showerror("Error", "Debe seleccionar un genero.")
        return False

    return True # si todo salio bien se envia un True

# Guardar
def guardar_campos():
    if not entradas_validas(): #llamamos la funcion
        return

    # Se obtiene la informacion de los campos y se guarda en variables
    nombre = tb_nombre.get()
    edad = tb_edad.get()
    apellidos = tb_apellidos.get()
    estatura = tb_estatura.get()
    telefono = tb_telefono.get()   

    genero = ""
    if var_genero.get() == 1:
        genero = "hombre"
    elif var_genero.get() == 2:
        genero = "mujer"

    # Generar la cadena de caracteres
    datos = f"\nnombre: {nombre}\napellidos: {apellidos}\nedad: {edad}\nestatura: {str(estatura)}\ntelefono: {telefono}\ngenero: {genero}"
    
    # Este metodo escribe la informacion en la ubicacion definida como tipo txt
    with open("C:\\Users\\User\\Desktop\\Programacion_avanzada_textos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
    
    # Creacion de los campos de entrada
    messagebox.showinfo("Informacion", "Datos guardados con exito\n\n" + datos)
    limpiar_campos()

# Nombre
lb_nombre = tk.Label(ventana, text="Nombre de la persona")
lb_nombre.pack(pady=5)
lb_nombre.config(fg="black", font=("Helvetica", 15), bg="lightblue")

tb_nombre = tk.Entry()
tb_nombre.pack(pady=5)

# Apellidos
lb_apellidos = tk.Label(ventana, text="Apellidos de la persona")
lb_apellidos.pack(pady=5)
lb_apellidos.config(fg="black", font=("Helvetica", 15), bg="lightblue")

tb_apellidos = tk.Entry()
tb_apellidos.pack(pady=5)

# Edad
lb_edad = tk.Label(ventana, text="Edad")
lb_edad.pack(pady=5)
lb_edad.config(fg="black", font=("Helvetica", 15), bg="lightblue")

tb_edad = tk.Entry()
tb_edad.pack(pady=5)

# Telefono
lb_telefono = tk.Label(ventana, text="Telefono")
lb_telefono.pack(pady=5)
lb_telefono.config(fg="black", font=("Helvetica", 15), bg="lightblue")

tb_telefono = tk.Entry()
tb_telefono.pack(pady=5)

# Estatura    
lb_estatura = tk.Label(ventana, text="Estatura en metros") 
lb_estatura.pack(pady=5)
lb_estatura.config(fg="black", font=("Helvetica", 15), bg="lightblue")

tb_estatura = tk.Entry()   
tb_estatura.pack(pady=5)

# Genero
lb_genero = tk.Label(ventana, text="Genero")
lb_genero.pack(pady=5)
lb_genero.config(fg="black", font=("Helvetica", 15), bg="lightblue")

rb_hombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rb_hombre.pack(pady=5)
rb_hombre.config(bg="lightblue", fg="blue", font=("Helvetica", 15))

rb_mujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rb_mujer.config(bg="lightblue", fg="blue", font=("Helvetica", 15))
rb_mujer.pack(pady=5)

# Guardar
btn_guardar = tk.Button(ventana, text="Guardar valores", command=guardar_campos)
btn_guardar.config(bg="blue", fg="white", font=("Helvetica", 15))
btn_guardar.pack(pady=5)

# Borrar
btn_borrar = tk.Button(ventana, text="Borrar valores", command=limpiar_campos, bd=5, relief="solid")
btn_borrar.config(bg="lightblue", fg="blue", font=("Helvetica", 15))
btn_borrar.pack(pady=5)

ventana.mainloop()
