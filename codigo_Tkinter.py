#importamos la libreria tkinter que se usa para crear intefaces gráficas 
import tkinter as tk
#usaremos messagebox para mostrar mensajes de advertencias 
from tkinter import messagebox
#definimos la funcion que se realizará cuando presiones el boton
def validar_y_convertir():
    temp = entry_temp.get() #obtenemos los datos que se ingresaron de la temperatura
    humedad = entry_humedad.get() #obtenemos los datos de la humedad
#definimos lo que pasara si los capos se estan vacios 
    if not temp or not humedad:
        messagebox.showwarning("Campos vacíos", "Por favor ingresa la temperatura y la humedad.")
        return #si estan vacios se detiene la funcion
    #convertimos los datos obtenidos a float paa determinar si son valores numericos y no una cadena de texto (string)
    try:
        temp = float(temp)
        humedad = float(humedad)
    except ValueError:
        #Eliminamos la opcion de ingresar letras. De lo contrario se moestrara el siguiente texto
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")
        return
    #creamos una cadena de texto con los valores que ingresaron
    resultado = f"Temperatura: {temp} °C\nHumedad: {humedad} %"
    #si el checkbox esta activado convertimos la temperatura
    if convertir_var.get():
        temp_f = (temp * 9/5) + 32
        resultado += f"\nTemperatura convertida: {temp_f:.2f} °F"
    #mostramos el resultado en la etiqueta de salida
    label_resultado.config(text=resultado)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Temperatura y Humedad")#titulo de la ventana

# Etiquetas y campos de entrada
#creamos una etiqueta para la temperatura y la ponemos en la primera fila, columna 0
tk.Label(ventana, text="Temperatura (°C):").grid(row=0, column=0, padx=5, pady=5)
# Creamos el campo de entrada para la temperatura y lo colocamos en la primera fila, columna 1
entry_temp = tk.Entry(ventana)
entry_temp.grid(row=0, column=1, padx=5, pady=5)
# Creamos una etiqueta para la humedad y la colocamos en la segunda fila, columna 0
tk.Label(ventana, text="Humedad (%):").grid(row=1, column=0, padx=5, pady=5)
# Creamos el campo de entrada para la temperatura y lo colocamos en la primera fila, columna 1
entry_humedad = tk.Entry(ventana)
entry_humedad.grid(row=1, column=1, padx=5, pady=5)

# Checkbox para convertir
# Creamos una variable booleana que se usará para saber si se desea convertir la temperatura
convertir_var = tk.BooleanVar()
# Creamos el checkbox para elegir si se quiere convertir la temperatura a Fahrenheit
check_convertir = tk.Checkbutton(ventana, text="Convertir a Fahrenheit", variable=convertir_var)
check_convertir.grid(row=2, columnspan=2, pady=5)

# Botón
# Creamos el botón que ejecutará la función validar_y_convertir cuando se presione
boton_validar = tk.Button(ventana, text="Validar y Mostrar", command=validar_y_convertir)
boton_validar.grid(row=3, columnspan=2, pady=10)

# Resultado
# Creamos una etiqueta vacía que luego mostrará el resultado
label_resultado = tk.Label(ventana, text="", fg="blue")
label_resultado.grid(row=4, columnspan=2, pady=5)

ventana.mainloop()
