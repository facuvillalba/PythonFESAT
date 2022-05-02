# PDF Module 1 Exercises
# First week: Strings - Operations - Arrays - Tuples
'''----------------------------------------------------------------------------------------------------------------------------          
1)  Generar nueva variable
    Dadas 4 variables con diferentes textos (de forma individual), generar una nueva
    variable con el siguiente contenido:
    Objetivo: "Python es un lenguaje de programación moderno"
    cadena_1 = "moderno"
    cadena_2 = "Python"
    cadena_3 = "es un lenguaje"
    cadena_4 = "de programación"
-------------------------------------------------------------------------------------------------------------------------------'''
# 1_Generate new variable
'''
cadena_1 = "moderno"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"
print(cadena_2, cadena_3, cadena_4, cadena_1)
print(cadena_2+" "+cadena_3+" "+cadena_4+" " + cadena_1)
'''
'''----------------------------------------------------------------------------------------------------------------------------          
2)  Calcular nota final
    Crear un programa para calcular la nota final del estudiante en base a 2 exámenes,
    los exámenes cuentan con un porcentaje distinto de la nota final
    nota_1 cuenta como el 40% de la nota final
    nota_2 cuenta como el 60% de la nota final
    Tener en cuenta: números, print, input, variables, operaciones matemáticas,
    cadena de texto.
    Los datos deben guardarse en variables y deben ser dinámicos por medio de input.
-------------------------------------------------------------------------------------------------------------------------------'''
# 2_Final note
'''
print("Ingresar notas del 0 al 10")
aux = False
while aux == False:
    nota_1 = int(input("Primera nota: "))
    nota_2 = int(input("Segunda nota: "))
    if nota_1 >= 0 and nota_1 <= 10 and nota_2 >= 0 and nota_2 <= 10:
        aux = True
    else:
        print("Ingresar notas válidas")
nota_final = (nota_1*0.4)+(nota_2*0.6)
print("Nota Final:", nota_final)
if nota_final >= 6:
    print('Aprobado')
else:
    print('Desaprobado')
'''   
'''----------------------------------------------------------------------------------------------------------------------------          
3)  Listas y Tuplas
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
    Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
    pantalla. Luego a la misma agregarle otra asignación mediante las funciones que
    tienen las listas y la muestre por pantalla la lista modificada. (hacerlo también en
    una tupla).
-------------------------------------------------------------------------------------------------------------------------------'''
# 3_Array and Tuple
'''
# With array
asignaturas_array = ['Matemáticas', 'Físcia', 'Química', 'Historia', 'Lengua']
print(asignaturas_array)
asignaturas_array.append('Dibujo')
print(asignaturas_array)
# With tuple
asignaturas_tuple = ('Matemáticas', 'Físcia', 'Química', 'Historia', 'Lengua')
print(asignaturas_tuple)
asignaturas_tuple = asignaturas_tuple + ('Dibujo',)
print(asignaturas_tuple)
'''
# Second week: Conditionals
'''----------------------------------------------------------------------------------------------------------------------------          
1)  Escribir un programa que le pregunte al usuario su edad y muestre por pantalla si
    es mayor de edad o no.
-------------------------------------------------------------------------------------------------------------------------------'''
# 1_Write a program to ask the age of a user and if he is an adult or not
'''
edad = int(input('Qué edad tenés? '))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
'''
'''----------------------------------------------------------------------------------------------------------------------------          
2)  Escriba un programa que pida dos números enteros y que calcule su división,
    escribiendo si la división es exacta o no.
-------------------------------------------------------------------------------------------------------------------------------'''
# 2_Write a program to calculate divisions exact or not
'''
num1 = int(input('Dividendo: '))
num2 = int(input('Divisor: '))
resto = num1 % num2
if resto == 0:
    print('División exacta')
else:
    print('División no exacta')
'''
'''----------------------------------------------------------------------------------------------------------------------------          
3)  Escriba un programa que pida tres números y que escriba si son los tres iguales, si
    hay dos iguales o si son los tres distintos.
-------------------------------------------------------------------------------------------------------------------------------'''
# 3_Write a program that asks for three numbers. How many are equal?
'''
num_a = int(input('Número a: '))
num_b = int(input('Número b: '))
num_c = int(input('Número c: '))
if num_a == num_b and num_c == num_a:
    print('Todos los números son iguales')
elif num_a == num_b or num_c == num_a or num_b == num_c:
    print('Dos números son iguales')
else:
    print('Todos son distintos')
'''
# Third week: Loops
'''----------------------------------------------------------------------------------------------------------------------------          
1)  While
    Escribir un programa que le pregunte al usuario números hasta que ingrese el 0,
    cuando lo haga mostrar por pantalla la suma de todos los números ingresados.
-------------------------------------------------------------------------------------------------------------------------------'''
# 1_While
'''
aux = False
sum = 0
while aux == False:
    num = int(input('Ingresar número: '))
    if num != 0:
        sum = sum + num
    else:
        aux = True
        print('Suma de numeros: ', sum)
'''
'''----------------------------------------------------------------------------------------------------------------------------          
2)  Escribí un programa que lea un número impar por teclado. Si el usuario no introduce
    un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
-------------------------------------------------------------------------------------------------------------------------------'''
# 2_Odd number
'''
aux = False
while aux == False:
    num = int(input('Ingresar número impar: '))
    if num % 2 == 0:
        print('Error el número es par')
    else:
        print('Correcto el número es impar')

        aux = True
'''
'''----------------------------------------------------------------------------------------------------------------------------          
3)  For
    Sumar los pares del 0 al 100.
-------------------------------------------------------------------------------------------------------------------------------'''
# 3_For pairs number from 0 to 100
'''
aux = 0
for num in range(0, 101, +2):
    aux = aux+num
    print(aux, end=', ')
'''
'''----------------------------------------------------------------------------------------------------------------------------   
4) Imprimir por pantalla los números del 1 al 10 al revés.
    Nota:
    Para imprimir por pantalla al revés se debe usar el mayor número, luego el menor,
    y el paso sería con -1 range(mayor, menor, -1)
-------------------------------------------------------------------------------------------------------------------------------'''
# 4_For numbers from 1 to 10 backwards
'''
for num in range(10, 0, -1):
    print(num)
'''
# Fourth week: Functions Exceptions
'''----------------------------------------------------------------------------------------------------------------------------   
1)  Realizar una función llamada par_o_impar:
    a. Recibirá un número por parámetro.
    b. Imprimirá Par si el número es par
    c. Imprimirá Impar si el número es impar
    d. Si se ingresa algo que no sea número debe indicar que se ingrese un número.
-------------------------------------------------------------------------------------------------------------------------------'''
# 1_Pair or odd
'''
def par_o_impar(num):
    if num % 2 == 0:
        print("Número par")
    else:
        print("Número impar")
try:
    num = int(input("Escribir número: "))
    par_o_impar(num)
except ValueError:
    print("Error! escribir número")
'''    
'''----------------------------------------------------------------------------------------------------------------------------   
2)  Realizar una función llamada año_bisiesto:
    a. Recibirá un año por parámetro
    b. Imprimirá “El año año es bisiesto” si el año es bisiesto
    c. Imprimirá “El año año no es bisiesto” si el año no es bisiesto
    d. Si se ingresa algo que no sea número debe indicar que se ingrese un número.
-------------------------------------------------------------------------------------------------------------------------------'''
# 2_Leap year
'''
def bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
try:
    anio = int(input("Escribir número: "))
    print("Año", anio, "Bisieto =", bisiesto(anio))
except ValueError:
    print("Error escribir número")
'''   
'''----------------------------------------------------------------------------------------------------------------------------
3)  Excepciones (extra)
    Localiza el error en el siguiente bloque de código. Crea una función con la excepción
    para evitar que el programa se bloquee y además explica en un mensaje al usuario
    la causa y/o solución:
-------------------------------------------------------------------------------------------------------------------------------'''
# 3_Exception
'''
def division(num_a, num_b):
    return num_a/num_b
try:
    num_a = int(input("Número dividiendo: "))
    num_b = int(input("Número divisor: "))
    print("Resultado", division(num_a, num_b))
except ZeroDivisionError:
    print("Error no es posible dividir por cero")
'''
# POWERPOINT CLASE 1
'''----------------------------------------------------------------------------------------------------------------------------
ACTIVIDAD SLICING --> FORMATEAR
    Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia.
    De forma individual, realiza lo siguiente:
    1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. 
    Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing cadena[::-1].
    2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
    3. Extraer la nota y almacenarla en una variable llamada nota.
    4. Extraer la materia y almacenarla en una variable llamada materia.
    5.  Mostrar por pantalla la siguiente estructura:
    NOMBRE APELLIDO tiene un NOTA en MATERIA
    Formateando las anteriores variables en una variable llamada cadena_formateada
    cadena = “acitametaM ,5.8 ,otipeP ordeP”
-------------------------------------------------------------------------------------------------------------------------------'''
# 3_Activity 2 Slicing
'''
cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_volteada = cadena[::-1]
print(cadena_volteada)

nombre_alumno = cadena_volteada[0:12:1]
print(nombre_alumno)

nota = cadena_volteada[14:17:1]
print(nota)

materia = cadena_volteada[19:29:1]
print(materia)

cadena_formateada = nombre_alumno+" tiene un "+nota+" en "+materia
print(cadena_formateada)
'''
#Activity_2 Initial practices
'''----------------------------------------------------------------------------------------------------------------------------
1) Identifica el tipo de dato (int, float, string, list o touple) de los siguientes valores literales:
Dato	                Tipo de datos
"Hola Mundo" 	        string
[1, 10, 100]	        list
-25	                    int
(8, 100, -12)	        touple
1.167	                float
["Hola", "Mundo"]	    list
''	                    string 
(1, -5, "Hola!")	    touple
-------------------------------------------------------------------------------------------------------------------------------'''
'''
a = "Hola Mundo"
b = [1, 10, 100]
c = -25
d = (8, 100, -12)
e = 1.167
f = ["Hola", "Mundo"]
g = ' '
h = (1, -5, "Hola!")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
'''
'''----------------------------------------------------------------------------------------------------------------------------
2) Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables: 
a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6) 
Ejecutar	            Resultado
print(a * 5)  	        50
print(a - b)    	    15
print(c + "Mundo")   	HolaMundo
print(c * 2)        	HolaHola
print(c[-1])        	a
print(c[1:])           	ola
print(d + d)       	    [1,2,3,1,2,3]
print(e[1])	            5
print(e+(7,8,9))	    (4,5,6,7,8,9)
-------------------------------------------------------------------------------------------------------------------------------'''
'''
a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e= (4,5,6)
print(a * 5)
print(a - b)  
print(c + "Mundo")  
print(c * 2) 
print(c[-1])
print(c[1:])
print(d + d) 
print(e[1])    
print(e+(7,8,9))   
'''
'''----------------------------------------------------------------------------------------------------------------------------
3) El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar 
el problema y solucionarlo?
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
La nota media es 14.0
-------------------------------------------------------------------------------------------------------------------------------'''
'''
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)
'''
'''----------------------------------------------------------------------------------------------------------------------------
4) A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada 
número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:
●	La primera nota vale un 15% del total
●	La segunda nota vale un 35% del total
●	La tercera nota vale un 50% del total
Ejemplos:
nota_1 = 10
nota_2 = 7
nota_3 = 4
-------------------------------------------------------------------------------------------------------------------------------'''
'''
nota_1 = 10
nota_2 = 7
nota_3 = 4
nota_final = (nota_1*0.15) + (nota_2*0.35) + (nota_3*0.50)
print(nota_final)
'''
'''----------------------------------------------------------------------------------------------------------------------------
5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe 
ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista
Partirás de: 
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
Debes llegar a: 
matriz = [ 
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
]
-------------------------------------------------------------------------------------------------------------------------------'''
'''
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))
print(matriz)
'''
'''
matriz = [[1, 5, 1], [2, 1, 2], [3, 0, 1], [1, 4, 4]]
matriz[0][len(matriz[0]):]= [sum(matriz[0])]
matriz[1][len(matriz[1]):]= [sum(matriz[1])]
matriz[2][len(matriz[2]):]= [sum(matriz[2])]
matriz[3][len(matriz[3]):]= [sum(matriz[3])]
print(matriz)                  
'''

'''
print(False == True)
print(10>=2*4)
print(33/3==11)
print(True > False)
print(True*5==2.5*2)
'''
'''
print(not False)
print(not 3 == 5)
print(33/3 == 11 and 5>2)
print(True or False)
print(True*5==2.5*2 or 123 >=23)
print(12>7 and True < False)
'''
#CLASE Controladores de Flujo (Condicionales)
'''----------------------------------------------------------------------------------------------------------------------------
Actividad Mayoría de Edad
Escribir un programa que le pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
'''
edad = int(input('Qué edad tenés? '))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
'''
'''
Actividad Marvel vs CapCom 
Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una preferencia (Marvel o Capcom). 
El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y 
preferencia, y muestre por pantalla el grupo que le corresponde.
'''
'''
nombre = input("Cómo te llamás? ")
preferencia = input("Cuál es tu preferencia M o C? ")
if (nombre[0] < "M" and preferencia == "M") or (nombre[0] > "N" and preferencia == "C"):
    print("Bienvenido",nombre,", tu preferenica es:",preferencia,"pertenece al Grupo A")
else:
    print("Bienvenido",nombre,", tu preferenica es:",preferencia,"pertenece al Grupo B")
''' 
#Trabajo a entregar
'''---------------------------------------------------------------------------------------------------------------------------- 
Actividad N°3 Control de Flujo
1)  Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.
2)  Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los 
    tres distintos.
    Entregar adjuntando un archivo. py + link de Colab a través del campus.
'''
#1
'''
num1 = int(input('Dividendo: '))
num2 = int(input('Divisor: '))
if num1 % num2 == 0:
    print('División exacta')
else:
    print('División no exacta')

#2
num_a = int(input('Número a: '))
num_b = int(input('Número b: '))
num_c = int(input('Número c: '))
if num_a == num_b and num_c == num_a:
    print('Todos los números son iguales')
elif num_a == num_b or num_c == num_a or num_b == num_c:
    print('Dos números son iguales')
else:
    print('Todos son distintos')
'''

#CLASE Bucles 
'''----------------------------------------------------------------------------------------------------------------------------
Escribir un programa que le pregunte al usuario número hasta que ingrese el o, cuando lo haga mostrar por pantalla la suma de 
todos los números.
'''
'''
num = int(input("Igresar un número: "))
suma_total=0
while num != 0:
    num = int(input("Igresar un número: "))
    suma_total += num
else:
    print("Suma total: ", suma_total)
''' 
#Ejemplos de clase
#FOR, cuando se las veces que se va a repetir.
#1
'''
listas=[1,2,3,4,5]
for lista in listas:
    print("Soy un ítem de la lista y valgo: ", lista)
'''
#2
'''
for valor in listas:
    valor *= 5
    print("Soy un ítem de la lista y valgo: ", valor)
'''
#3
'''
indice=0
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numero[indice]*=5
    indice +=1
    print(numeros, numero,indice)
'''  
#4
'''
paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']
for pais in enumerate(paises):
  #print (f"Pais:{pais[1]}, Indice:{pais[0]}") 
  print("pais", pais[1], "índice:", pais[0])
'''
#Trabajo a entregar
'''---------------------------------------------------------------------------------------------------------------------------- 
1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
1.	Mostrar una suma de los dos números
2.	Mostrar una resta de los dos números (el primero menos el segundo)
3.	Mostrar una multiplicación de los dos números
4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
5.	En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''
'''
num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))
opcion = 0
while opcion != 4:
    opcion = int(input('Elegir opción: 1 sumar, 2 restar, 3 multiplicar, 4 Salir: '))
    if(opcion == 1):
        result = num1 + num2
        print('Resultado:',result)
    elif(opcion == 2):
        result = num1 - num2
        print('Resultado:',result)
    elif(opcion == 3):
        result = num1 * num2
        print('Resultado:',result)
    elif(opcion == 4):
        print('Fin')
    else:
        print('Opción no válida, elegir nuevamente')
'''        
'''---------------------------------------------------------------------------------------------------------------------------- 
2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el 
proceso hasta que lo introduzca correctamente.     
'''     
'''
while True:
    num_a = int(input('Ingresar número impar: '))
    par = num_a % 2
    if (par == 0):     
        print('El número es par, ingresar nuevamente')
    else:        
        print('Correcto número impar')
        break
'''
'''----------------------------------------------------------------------------------------------------------------------------     
3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:   
'''
''' 
aux = 0
for num in range(1, 101, +2):
    aux = aux+num
    print(aux, end=', ')   
print('\nLa suma total de los primeros 100 números impares es:', aux)    
'''
'''----------------------------------------------------------------------------------------------------------------------------     
4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza 
una media aritmética:  
'''
'''
opcion = int(input('Cuántos números que igresar? '))
sum = 0
for numero in range(opcion):
    aux = int(input('Ingrese número: '))
    sum = sum + aux
print('Media aristmética es:', sum/opcion)
'''
'''----------------------------------------------------------------------------------------------------------------------------     
5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se 
repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
'''
'''
numeros=[1,3,6,9]
num = 0
while True:
    num = int(input('Ingresar números del 0 al 9: '))
    if (num >= 0 and num <= 9):
        if (num in numeros):
            print('El número si se encuentra en la lista')
            break
        else:
            print('No se encuentra en la lista')
            break    
    else:
        print('Error ingresar nuevamente')
'''        
'''----------------------------------------------------------------------------------------------------------------------------     
6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
    Todos los números del 0 al 10 [0, 1, 2, ..., 10]
    Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
    Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
    Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
    Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
'''
'''
list_1 = list(range(0,11,1))
print('Todos los números del 0 al 10 =',list_1) 
list_1 = list(range(-10,1,1))
print('Todos los números del -10 al 0 =',list_1)
list_1 = list(range(0,21,2))
print('Todos los pares del 0 al 20 =',list_1)   
list_1 = list(range(-19,0,2))
print('Todos los impares del -20 al 0 =',list_1)       
list_1 = list(range(0,51,5))
print('Todos los múltiplos de 5 del 0 al 50 =',list_1)  
'''
'''----------------------------------------------------------------------------------------------------------------------------     
7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe 
repetirse ningún elemento en la nueva lista:
'''
'''
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
for aux_1 in lista_1:
    for aux_2 in lista_2:
        if aux_1 == aux_2 and aux_1 not in lista_3:
            lista_3.append(aux_1)
print(lista_3)            
'''     
'''
#CLASE 23-03-22 SET and DECCIONARY (PowerPoint)

https://j2logo.com/python/tutorial/tipo-set-python/#set-clase

'''
'''
grupo={"Miguel","Blanca","Mario","Andrés"}
grupo.update(["Ana","Ramón","Marta","Eric","David"])
print(grupo)
'''

'''----------------------------------------------------------------------------------------------------------------------------     
Actividad N° 5 (Clase 9 y 10)
1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base y 10 de altura
'''
'''
def area_rectangulo(base, altura):
    return base*altura
print("Área del rectángulo:",area_rectangulo(base=15, altura=10))
'''
'''
2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
Calcula el área de un círculo de 5 de radio.
'''
'''
import math
def area_circulo(radio):
    return round(radio*math.pi, 2)
print("Área del círculo", area_circulo(radio=5))
'''
'''
3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
1.	Si el primer número es mayor que el segundo, debe devolver 1.
2.	Si el primer número es menor que el segundo, debe devolver -1.
3.	Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
'''
'''
def relacion(num_one,num_two):
    if num_one > num_two:
        return 1
    elif num_one < num_two:
        return -1
    else:
        return 0
print("La relación es:", relacion(num_one=5, num_two=10))
print("La relación es:", relacion(num_one=10, num_two=5))    
print("La relación es:", relacion(num_one=5, num_two=5))  
'''
'''
4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
Comprueba el punto intermedio entre -12 y 24
'''
'''
def intermedio(num_a, num_b):
    return (num_a + num_b)/2
print("El número intermedio es:", intermedio(num_a= -12, num_b= 24))
'''
'''
5) Realizá una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el 
segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
1.	Devolver el límite inferior si el número es menor que éste
2.	Devolver el límite superior si el número es mayor que éste.
3.	Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10
'''
'''
def recortar(num_recortar,num_inferior,num_superior):
    if num_recortar<num_inferior:
        return num_inferior
    elif num_recortar>num_superior:
        return num_superior
    else:
        return num_recortar
print("Resultado:", recortar(num_recortar=15,num_inferior=0,num_superior=10))
'''
'''
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:
''' 
'''
lista = [6,5,2,1,7]
def separar(lista):
    pares=[]
    impares=[]
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
            pares.sort()
        else:
            impares.append(n) 
            impares.sort()          
    return pares, impares
pares, impares = separar(lista)
print("Lista pares ordenada:", pares) 
print("Lista impares ordenada:", impares)    
'''    
'''---------------------------------------------------------------------------------------------------------------------------- 
Actividad N°6 Cuenta
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener 
decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase: 
Un constructor.
mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos
'''
'''
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad      
    
    def mostrar(self):
        print(f"Datos de Cuenta\nTitular: {titular.apellido} {titular.nombre} Saldo ${cuenta.cantidad}")
       
    def ingresar(self, cantidad):
        if (cantidad > 0):
            self.cantidad = cuenta.cantidad + cantidad
        print(f"Ingreso: {cantidad} Saldo ${cuenta.cantidad}")    
    
    def retirar(self, cantidad):
        if (cantidad < 0):
            self.cantidad = cuenta.cantidad + cantidad
        print(f"Retiro: {cantidad} Saldo ${cuenta.cantidad}")  

class Titular:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido 
      
titular = Titular("Facundo", "Villalba")  
cuenta = Cuenta(titular, 15000)

cuenta.mostrar()
cuenta.ingresar(5000)
cuenta.ingresar(-500)
cuenta.retirar(-2000)
cuenta.retirar(2000)
cuenta.retirar(-20000)
'''
'''---------------------------------------------------------------------------------------------------------------------------- 
Actividad Cetáceo
Crear una herencia múltiple, trabajando con Mamífero, Cetáceo, AnimalMarino. Realizar la herencia múltiple 
respetando este diagrama de clases.
'''

class Mamifero:  
    def __init__(self, cantMamas, esperazaDeVida):
        self.cantMamas = cantMamas
        self.esperanzaDeVida = esperazaDeVida
    
    def nacer(self):
        return "Mamifero nadan"
       
    def mamar(self):
        return "Mamifero maman"
        
class AnimalMarino:   
    def __init__(self, tieneBranqueas, especie):
        self.tieneBranqueas = tieneBranqueas
        self.especie = especie 
    
    def nadar(self):
        return "Animal marino nadan"    
    
class Cetaceo(Mamifero, AnimalMarino):  
    def __init__(self, notas, vivenEn, peso, cantMamas, esperanzaDeVida, tieneBranqueas, especie):
        Mamifero.__init__(self, cantMamas, esperanzaDeVida)
        AnimalMarino.__init__(self, tieneBranqueas, especie)
        self.notas = notas
        self.vivenEn = vivenEn
        self.peso = peso
        
    def nacer(self):
        return"Cetaceo nacen"
    
    def nadar(self):
        return "Cetaceo nadan"

cetaceo = Cetaceo("nota Cetaceo", "ocenaos","7 tn","1","70 años", "sin branqueas", "ballena")

print(f"Clase hija Cetaceo:\nNota: {cetaceo.notas} Viven en: {cetaceo.vivenEn} Peso: {cetaceo.peso} Esperanza de vida: {cetaceo.esperanzaDeVida} Tienen branqueas: {cetaceo.tieneBranqueas} Especie: {cetaceo.especie}")
print(f"Metodos: {cetaceo.nacer()} {cetaceo.nadar()}") 
print("Herencia de Cetaceo:", Cetaceo.__mro__)