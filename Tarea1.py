nombre = input("ingrese su nombre: ")
apellido = input("ingrse su apellido: ")
tam = int(len(nombre))
tam2 = int(len(apellido))
tam3= int(tam + tam2)

print("Tu nombre completo es: ", nombre, apellido)
print("Tu nombre tiene", tam3, "letras")