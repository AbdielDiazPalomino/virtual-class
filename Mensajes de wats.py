# Este es un codigo para enviar un mensaje y tambien para programar
# a que hora se envia el mensaje
import pywhatkit 

mensaje = input("Ingrese el mensaje: ")
rango = int(input("Ingrese el número de mensajes: "))
rango2 = 0

while rango2 < rango:
    pywhatkit.sendwhatmsg("+51955002976",mensaje, 21,46)
    #pywhatkit.sendwhatmsg("+51955002976",mensaje, 15,34)
    rango2= rango2 + 1  
 
print("Mensaje Enviado")