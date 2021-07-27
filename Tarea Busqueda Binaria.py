"""
Una Busqueda Binaria divide una lista a la mitad para hallar un número o una palabra por medio 
de su índice, los indices son sus posiciones, la primera posición siempre es 0 
"""

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]

#La función sort hace que la lista se ordene en orden ascendente en los números
#y alfabeticamente con las palabras o letras
lista.sort()

def busqueda_binaria(valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        #Acá le decimos que el punto medio es inicio mas fin,
        #todo eso entre dos pero con doble barra // para q salga
        #un entero y no un foltante
        punto_medio = (inicio + fin) // 2

        if valor == lista[punto_medio]:
            return punto_medio
        elif valor > lista[punto_medio]:
            inicio = punto_medio + 1
        else:
            fin = punto_medio - 1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El valor {valor} no se encontró"
    else:
        return f"El valor {valor} se encuentra en la posición {res_busqueda + 1}"

print(lista)

while True:
    valor= int(input("Ingresa número a buscar: "))
    print(buscar_valor(valor))
    continuar = int(input("Quieres continuar?\n 1 para seguir\n Y 2 para salir\n Rpta: "))
    if continuar == 1:
        print(">>>>CONTINUEMOS!!!<<<<")
    else:
        print("The end")
        break

