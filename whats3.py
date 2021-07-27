import pywhatkit as py

mensaje = input("Ingrese el mensaje: ")
rango = int(input("Ingrese el número de mensajes: "))
rango2 = 0

while rango2 < rango:
    py.sendwhatmsg("+51955002976",mensaje, 22,10)
