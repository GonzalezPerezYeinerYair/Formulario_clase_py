import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title ("Formulario_vr1")

#Crear la variable para el radiobutton
var_genero = tk.IntVar()


#funcion para limpiar
def limpiar_campos ():
    tb_apellidos.delete(0, tk.END)
    tb_edad.delete(0, tk.END)
    tb_estatura.delete(0, tk.END)
    tb_nombre.delete(0, tk.END)
    tb_telefono.delete(0, tk.END)
    var_genero.set(0)
    
#guardar
def guardar_campos():
    #Se obtiene la informacion de los campos y se guarda en variables
    nombre= tb_nombre.get()
    edad = tb_edad.get()
    apellidos = tb_apellidos.get()
    estatura = tb_estatura.get()
    telefono = tb_telefono.get()   

    genero=""
    if var_genero.get() == 1:
          genero= "hombre"
    elif var_genero.get() == 2:
          genero= "mujer"

    ###generar la cadena de caracteres
    datos= "\nnombres: " +nombre + "\napellidos" + apellidos+ "\nedada:" + edad +"\nestatura:" +estatura+"\ntelefono:"+telefono+ "\ngenero:"+genero
    
    #este metodo escribe la informacion en la ubicacion definida como tipo txt
    with open("C:\\Users\\User\Desktop\\Programacion_avanzada_textos.txt","a") as archivo:
        archivo.write(datos+ "\n\n") # type: ignore
    
    ##Creacion de los campos de emtrada
    messagebox.showinfo("Informacion", "Datos guardados con exito\n\n"+ datos) # type: ignore
    tb_apellidos.delete(0, tk.END)
    tb_edad.delete(0, tk.END)
    tb_estatura.delete(0, tk.END)
    tb_nombre.delete(0, tk.END)
    tb_telefono.delete(0, tk.END)
    var_genero.set(0)



#nombre
lb_nombre=tk.Label(ventana, text="Nombre de la persona")
lb_nombre.pack()
lb_nombre.config(fg="blue" )

tb_nombre= tk.Entry()
tb_nombre.pack()

#apellidos
lb_apellidos=tk.Label(ventana, text="Apellidos de persona")
lb_apellidos.pack()
lb_apellidos.config(fg="blue" )


tb_apellidos= tk.Entry()
tb_apellidos.pack()

#edad
lb_edad=tk.Label(ventana, text="ingrese su Edad")
lb_edad.pack()
lb_edad.config(fg="blue" )

tb_edad= tk.Entry()
tb_edad.pack()

#telefono
lb_telefono=tk.Label(ventana,  text="Telefono")
lb_telefono.pack()
lb_telefono.config(fg="blue" )

tb_telefono= tk.Entry()
tb_telefono.pack()
 
#estatura    
lb_estatura = tk.Label (ventana,  text="Estatura") 
lb_estatura.pack()
lb_estatura.config(fg="blue" )
 
tb_estatura= tk.Entry()   
tb_estatura.pack()

#genero

lb_genero = tk.Label (ventana,  text="genero")
lb_genero.pack()
lb_genero.config(fg="blue" )

rb_hombre=tk.Radiobutton(ventana, text= "Hombre", variable=var_genero, value=1)
rb_hombre.pack()

rb_mujer=tk.Radiobutton(ventana, text= "mujer", variable=var_genero, value=2)
rb_mujer.pack()

#guardar
btn_guardar =tk.Button(ventana,  text="Guardar valores", command=guardar_campos)
btn_guardar.pack()

#borar
btn_borrar =tk.Button (ventana,  text="borar valores", command= limpiar_campos)
btn_borrar.pack()

ventana.mainloop()

