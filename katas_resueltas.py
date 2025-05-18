# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_letras(cadena):
    cadena = cadena.replace(" ", "")
    resultado = {}
    for letra in cadena:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    return resultado

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def doblar_lista(lista):
    return list(map(lambda x: x * 2, lista))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras(palabras, objetivo):
    resultado = []
    for palabra in palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    return list(map(lambda a, b: a - b, lista1, lista2))

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_nota(notas, nota_aprobado=5):
    if len(notas) == 0:
        return (0, "suspenso")
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: str(tupla), lista_tuplas))

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
def dividir_numeros():
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = a / b
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("La división fue exitosa. Resultado:", resultado)

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista_mascotas))

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía.")
    return sum(lista) / len(lista)

# Excepción personalizada:
try:
    print(promedio([10, 20, 30]))
except ListaVaciaError as e:
    print("Error:", e)


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            print("Edad fuera de rango.")
        else:
            print("Edad válida:", edad)
    except ValueError:
        print("Debes introducir un número válido.")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def letras_may_min(conjunto):
    letras = set(conjunto)  # elimina duplicados
    return list(map(lambda l: (l.upper(), l.lower()), letras))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
def palabras_con_letra(lista, letra):
    return list(filter(lambda p: p.startswith(letra), lista))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_3 = lambda lista: list(map(lambda x: x + 3, lista))

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()
def palabras_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda p: len(p) > n, palabras))

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
def filtrar_estudiantes(estudiantes):
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

# 19. Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
cubo = lambda x: x ** 3

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
def producto_lista(lista):
    return reduce(lambda x, y: x * y, lista)

# 23. Concatena una lista de palabras.Usa la función reduce() .
def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto = lambda a, b: a % b

# 27. Crea una función que calcule el promedio de una lista de números.
def promedio_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # si no hay duplicados

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarar(texto):
    texto = str(texto)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    try:
        entrada = input("Introduce una lista de nombres separados por comas: ")
        nombres = [nombre.strip() for nombre in entrada.split(',')]
        nombre_buscado = input("Introduce el nombre a buscar: ").strip()
        if nombre_buscado in nombres:
            print(f"{nombre_buscado} fue encontrado.")
        else:
            raise ValueError("Nombre no encontrado en la lista.")
    except ValueError as e:
        print("Error:", e)

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_empleado(nombre, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    return "Esa persona no trabaja aquí."

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda lista1, lista2: list(map(lambda a, b: a + b, lista1, lista2))

######################
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
### Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("Posición no válida para quitar rama.")

    def info_arbol(self):
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitudes de ramas": self.ramas
        }
    
### Caso de uso:
# 1. Crear un árbol.
mi_arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
info = mi_arbol.info_arbol()


######################
# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
### Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo restante: {self.saldo}")

    def transferir_dinero(self, desde_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser mayor que 0.")
        if cantidad > desde_usuario.saldo:
            raise ValueError(f"{desde_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        desde_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{desde_usuario.nombre} ha transferido {cantidad} a {self.nombre}.")

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que 0.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Nuevo saldo: {self.saldo}")

### Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)



# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
### Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = [p for p in palabras if p != palabra_a_eliminar]
    return ' '.join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se necesitan dos palabras para reemplazar.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se necesita una palabra para eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida.")

### Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto
texto = "hola mundo hola sol mundo"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "hola", "adiós"))
print(procesar_texto(texto, "eliminar", "mundo"))


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia(hora):
    if 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 20:
        return "Es la tarde"
    elif 0 <= hora < 6 or 20 <= hora <= 23:
        return "Es de noche"
    else:
        return "Hora no válida"

hora_usuario = int(input("Introduce la hora (0-23): "))
print(momento_del_dia(hora_usuario))

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
## Las reglas de calificación son:
#- 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Nota fuera de rango"

nota_usuario = int(input("Introduce la nota del alumno (0-100): "))
print(calificacion_texto(nota_usuario))

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    elif figura == "circulo":
        radio, = datos
        return math.pi * radio**2
    else:
        return "Figura no válida"

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
def calcular_descuento():
    try:
        precio = float(input("Introduce el precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Introduce el valor del cupón: "))
            if valor_cupon > 0:
                precio_final = precio - valor_cupon
            else:
                print("Cupón no válido. Se ignora el descuento.")
                precio_final = precio
        else:
            precio_final = precio

        print(f"El precio final de la compra es: {precio_final:.2f} €")

    except ValueError:
        print("Error: Entrada inválida.")