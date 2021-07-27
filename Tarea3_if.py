num1 = int(input("Inserte el primer número: "))
num2 = int(input("Inserte el segundo número: "))
num3 = int(input("Inserte el tercer número: "))

if num1 > num2 and num1 > num3:
    print(int(num1), "Es el mayor")

elif num2 > num1 and num2 > num3:
    print(int(num2), "Es el mayor")
    
elif num3 > num2 and num3 > num1:
    print(int(num3), "Es el mayor")

else:
    print("son iguales")