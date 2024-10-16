# Reto2 Preguntas y respuestas

# --------- Me di la tarea de realizar la siguiente actividad
# de una forma dinamica, mediante un juego utilizando 
# la biblioteca de Tkinter de Python para crear la interfaz gráfica.
# El juego muestra 10 preguntas y cada una cuentas con 3 opciones en las que el usuario
# debe seleccionar una opción y posteriormente se dará una respuesta (correcto o incorrecto) ----------

#----El juego lleva un registro del puntaje actual del usuario y muestra el puntaje final al finalizar ---

import tkinter as tk
import random
# ---------------- Definiciones de preguntas y respuestas ----------------------

pregunta = [
    {
        'pregunta': '¿Cuál es nuestra Misión?',
        'opciones': ['Contribuir a la sostenibilidad','La Transformación Digital y e-Justicia','Ser lider ambiental'],
        'respuesta_correcta': 'La Transformación Digital y e-Justicia'
    },
    {
        'pregunta': '¿Cuál es nuestra Visión?',
        'opciones': ['Ser una área de vanguardia que transforma al Poder Judicial','Estar más conectados al mundo','Hacer uso eficiente de recursos naturales'],
        'respuesta_correcta': 'Ser una área de vanguardia que transforma al Poder Judicial'
    },
    {
        'pregunta': '¿A qué Dirección corresponde el Técnico de Analitica y Ciencia de Datos?',
        'opciones': ['Coordinación de gestión','Dirección de Gobernanza de Datos','Dirección de Analitica y Ciencia de Datos'],
        'respuesta_correcta': 'Dirección de Analitica y Ciencia de Datos'
    },
    {
        'pregunta': '¿Cuántas Jefaturas tiene la Coordinación de Gestión?',
        'opciones': ['2','1','Ninguna'],
        'respuesta_correcta': 'Ninguna'
    },
    {
        'pregunta': '¿Cuáles son las siglas de la Dirección General de Estrategia y Transformación Digital?',
        'opciones': ['DGETD','DITD','DGTDL'],
        'respuesta_correcta': 'DGETD'
    },
    {
        'pregunta': '¿Cuál Artículo conforma el Acuerdo General del Pleno del Consejo de la Judicatura Federal que reforma y adiciona diversas disposiciones en relación con la creación de la DGETD?',
        'opciones': ['Artículo 157','Artículo 158','Los 2 Artículos anteriores'],
        'respuesta_correcta': 'Los 2 Artículos anteriores'
    },
    {
        'pregunta': '¿Cuántas atribuciones menciona el Artículo 158?',
        'opciones': ['12','14','10'],
        'respuesta_correcta': '14'
    },
    {
        'pregunta': 'Ejecutar en coordinación con las áreas competentes, las estrategias para el aprovechamiento y gestión de la información en materia de gobierno de datos y gobernanza digital ¿A qué atribución corresponde?',
        'opciones': ['III','IV','IX'],
        'respuesta_correcta': 'IV'
    },
    {
        'pregunta': '¿Cuántos Pilares conforman nuestro trabajo?',
        'opciones': ['4','6','2'],
        'respuesta_correcta': '4'
    },
    {
        'pregunta': '¿La transpariencia y el acceso a la información es parte de los Sistemas y Mecanismos?',
        'opciones': ['Si','Tal vez','No'],
        'respuesta_correcta': 'Si'
    }

]

def mostrar_pregunta():
    #----- Función para mostrar una nueva pregunta y opciones de respuesta --------
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    resultado_texto.set('')
    if not preguntas_disponibles:
        #--------- Lo siguiente entrará en función cuando no haya más preguntas disponibles y mostrará un mensaje, posteriormente se finalizará el juego -------
        pregunta_texto.set('No hay más preguntas disponibles, gracias por participar.')
        siguiente_boton.config(state=tk.DISABLED)
        terminar_juego()
        return
    pregunta_actual = random.choice(preguntas_disponibles)
    pregunta_texto.set(pregunta_actual['pregunta'])
    for i, opcion in enumerate(pregunta_actual['opciones']):
        botones_opciones[i].config(text=opcion)
        siguiente_boton.config(state=tk.DISABLED)
        puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

def verificar_respuesta(respuesta):
    #---- La siguiente función servirá para verificar la respuesta seleccionada por el usuario --------
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    if pregunta_actual['respuesta_correcta'] == respuesta:
        resultado_texto.set('¡Respuesta Correcta!')
        puntaje_actual += 10
    else:
        resultado_texto.set('Respuesta Incorrecta')
    siguiente_boton.config(state=tk.NORMAL)
    #----- Para eliminar la pregunta actual de la lista de preguntas disponibles utilizaré lo siguiente: -------------
    preguntas_disponibles.remove(pregunta_actual)

def terminar_juego():
    #----- Función que servirá para finalizar el juego y mostrar el puntaje final: --------------------
    global puntaje_actual
    pregunta_texto.set('Juego Terminado')
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
    resultado_texto.set(f'Puntaje Final:{puntaje_actual}')

# -------- Las funciones proximas serán para configurar la ventana principal --------------
ventana= tk.Tk()
ventana.title('Reto 2: Preguntas y Respuestas')
ventana.geometry('800x600')
ventana.resizable(0,0)
ventana.config (bg= 'white')

titulo_label = tk.Label(ventana, text = 'Dirección General de Estrategia y Transformación Digital', font=('Arial',20), bg= 'white', fg= '#0E1958')
titulo_label.pack(pady=50)

#--------------- Para insertar el logo ------------------------------------------
image = tk.PhotoImage(file= 'cjf.png')
lbl_img = tk.Label(ventana, image = image, bg= 'white')
lbl_img.place(x= '5', y= '5')

#------- Crearé una copia de la lista de preguntas disponibles que hice en el inicio --------
preguntas_disponibles = pregunta.copy()

#------- Variable para llevar un registro de la pregunta actual ------
pregunta_actual = None

#------ Variable para mostrar la pregunta actual -----------
pregunta_texto = tk.StringVar()
pregunta_label = tk.Label(ventana, textvariable=pregunta_texto, bg= 'white', wrap= '600', width= 80, height=5, font=('Arial',14))
pregunta_label.pack(pady=10)

#------- Botones para las opciones de las respuestas ------------------
botones_opciones = []
for i in range(3):
    boton = tk.Button(ventana, text='', wrap= '300', width= 50, height=2, font=('Arial',10), command=lambda i=i:verificar_respuesta(pregunta_actual['opciones'][i]))
    botones_opciones.append(boton)
    boton.pack(pady=5)

#--------- Variable que mostrará si la respuesta fue correcta o incorrecta ------------
resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto,font=('Arial',14), bg= 'white')
resultado_label.pack(pady=10)

#---------- Botón Siguiente -------------------------
siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial',12), width= '15', height= '1', command=mostrar_pregunta)
siguiente_boton.place(x='600', y= '530')
siguiente_boton.config(state=tk.DISABLED)

#----------- Para puntaje actual ------------------
puntaje_actual = 0
puntaje_label = tk.Label(ventana, text=f"Puntaje Actual: {pregunta_actual}",font=('Arial',14), bg= 'white')
puntaje_label.place(x= '50', y='530')

#----- Botón para terminar el juego ------------------
terminar_boton = tk.Button(ventana, text='Terminar Juego', font=('Arial',12),width= '15', height= '1', bg= 'red', fg= 'white', command=terminar_juego)
terminar_boton.place(x= '330', y='530')

#------------- Referencias Bibliográficas -----------

etiqueta1 = tk.Label(ventana, text="La información de este juego se obtuvo de la fuente: https://apps.cjf.gob.mx/dgetd/#/inicio",font=('Arial',8), bg= 'white')
etiqueta1.place(x= '50', y='565')

#--------- Para iniciar el juego ----------------------
mostrar_pregunta()

#------- Iniciar el bucle principal ------------------
ventana.mainloop()