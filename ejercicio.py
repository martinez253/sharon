from tkinter import*

root = TkVersion()
root.geometry("600x450")
root.config(bg="blue")
frame = Frame(root, width=500, height=400, bg="yellow")
frame.pack()

hora_inicio = 9
hora_final = 10
hora_ingreso = 9.5
numero_estudiantes = 0
en_clase = False

encabezado = Label(frame, text="sala virtual", font=("Arial Bold", 20), fg="blue")
encabezado.place(x=150, y=10) 

for fila in range(100,300,100):
    for columna in range(100,400,100):
        numero_estudiantes = numero_estudiantes +1
        if hora_ingreso >= hora_inicio and hora_ingreso < hora_final and en_clase == False:
            asistente = Label(frame, text='estudiante'+str(numero_estudiante))
            asistente.place(x=columna, y=fila)

nombre = Label(frame, text="nombre: ")
nombre.place(x=100, y=300)
#nombre.pack(side="LEFT")
nuevo_estudiante = Entry(frame, bd=2)
nuevo_estudiante.place(x=180, y=300)
#nuevo_estudiante.pack(side="RIGHT")

def agregar_asistente():
    nuevo_asistente = Label(frame, text="asistente agregado")
    nuevo_asistente.place(x=190, y=300)

root.mailoop()