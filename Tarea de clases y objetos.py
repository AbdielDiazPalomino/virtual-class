#Abdiel, al llamarme en tercera persona significa que es algo serio
#concentrate al entender este codigo

"""
En este codigo estamos haciendo una clase osea class
para  poder importarla otro trabajo

ya aquí vemos que la clase se llama Estudiande y le
damos una deficion que va a init cializar self siempre va
luego ponemos el nombre, curso lo que querramos
"""
class Estudiante:
    def __init__(self, nombre, edad, curso_inicial):
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.nombre = nombre
        self.esta_activo = True
        self.cursos = [curso_inicial]
    def desactivar (self):
        self.esta_activo = False
    def añade_curso (self, curso):
        self.curso = curso
        self.cursos.append(curso)
    def quitar (self, curso):
        self.cursos.remove(curso)

#Luego ponemos los Datos de los estudiantes como su nombre
#y lo que le hemos dado en el def __init__
estudiante1 = Estudiante("Santiago", 26, "Python")

estudiante2 = Estudiante("Belen", 24, "Java Script")

#creamos variables para añadir y quitar cursos aunque podemos
#quitar y poner nombre también
curso1 = input("añade curso: ")
curso2 = input("añade curso: ")
curso3 = input("añade curso: ")
curso4 = input("quitar curso: ")

#acá es donde la lo operamos 
#Le decimos que al estudiante1 le añanada un curso
# que será la variable curso1 y de igual forma con las siguientes
estudiante1.añade_curso(curso1)

estudiante1.añade_curso(curso2)

estudiante1.añade_curso(curso3)

#acá imprimimos el estudiante1 con todos lo cursos que le añadimos
print(estudiante1.cursos)

#acá le quitamos un curso en este caso
estudiante1.quitar(curso4)

#y lo imprimimos con el curso que le quitamos
print(estudiante1.cursos)

"""
Por siacaso no estamos trabajando con el estudiante2
Solo con el 1 añadiendoles y quitandole cursos
Pero trabajar con el estudiante2 no es dificil es lo mismo
solo que lo reemplazar por el nombre de estudiante2
"""
