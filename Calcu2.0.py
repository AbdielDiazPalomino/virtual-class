#Hay que hacer tipo calculadora
#De poner numero al lado poner la operacion y listo
#no estar dando enter para seguir

num1 = int(input("Ingresa el primer número: "))
opera = input("Que operación es: ")
num2 = input("Ingresa el segundo número número: ")
sua = int(num1) + int(num2)
re = int(num1) - int(num2)
mul = int(num1) * int(num2)
di = int(int(num1) / int(num2))
r = int(num1) % int(num2)

if opera == "+":
    print("La suma es", sua)

elif opera == "-":
    print("La resta es", re)

elif opera == "*":
    print("La multiplicación es", mul)

elif opera == "/":
    print("El conciente es", di)

elif opera == "/":
    print("El residuo es", r)

else:
    print("El operador no es valido\n""Utilice los siguientes: +, -, *, /")