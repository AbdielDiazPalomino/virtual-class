#Esto es mejor ejecutarlo y se explica solo
#pero igual te explicaré esto es una ventana que te permite
#poner tu nombre, tu apellido y lo que quieras y podría ser un inicio de seción
#pero hay q tenerlo con una base de datos >:v

#Y tkinter o Tk es una interfas gráfica donde puedes hacer figuras
#geometricas o ventanas en este caso

from tkinter import *


root = Tk()

Frame = Frame(root, width=1200, height=600)
Frame.pack()

Nombre = Entry(Frame)
Nombre.grid(row=0, column=1, padx= 10, pady=10)
Nombre.config(fg="Black", justify="left")

Apellido = Entry(Frame)
Apellido.grid(row=1, column=1, padx=10, pady=10)

Dirección = Entry(Frame)
Dirección.grid(row=2, column=1, padx=10, pady=10)

Contraseña = Entry(Frame)
Contraseña.grid(row=3, column=1, padx=10, pady=10)
Contraseña.config(show="*")

Nombre = Label(Frame, text="Nombre:")
Nombre.grid(row=0, column=0, padx=10, pady=10)

Apellido = Label(Frame, text="Apellido:")
Apellido.grid(row=1, column=0, padx=10, pady=10)

Dirección = Label(Frame, text="Dirección:")
Dirección.grid(row=2, column=0, padx=10, pady=10)

Contraseña = Label(Frame, text="Contraseña:")
Contraseña.grid(row=3, column=0, padx=10, pady=10)

Comentariop = Text(Frame, width=16, height=5)
Comentariop.grid(row=4, column=1, padx=10, pady=10)

Barra = Scrollbar(Frame, command = Comentariop.yview)
Barra.grid(row=4, column=2, sticky="nsew")

Comentariop.config(yscrollcommand=Barra.set)

Comentario = Label(Frame, text="Comentario:")
Comentario.grid(row=4, column=0, padx=10, pady=10)





root.mainloop()