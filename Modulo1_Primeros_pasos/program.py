# program.py
# * Declarar Variables
sum1 = 1 + 2
print(sum1)

# * Funcion Print
print('Hola desde la consola')

# * Variables
sum2 = 1 + 2 # 3
product = sum2 * 2
print(product)

# * Tipos de Datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# * Funcion type para saber el tipado de la variable

typePlanets = type(planetas_en_el_sistema_solar)

print(typePlanets)

# * Operadores Aritmeticos

sumaArit = 2 + 3;
restaArit = 3 - 2;
divisionArit = 6 / 2;
multiplicacionArit = 5 * 10;

print("Suma Aritmetica",sumaArit);
print("Resta Aritmetica",restaArit);
print("Multiplicacion Aritmetica",multiplicacionArit);
print("Division Aritmetica",divisionArit);

# * Operadores de Asignación

x = 2; # * Asignamos el valor de 2 a x
x += 2; # * Asignamos un auto incremento de valor 2 a lo que tiene x actualmente 
x -= 2; # * Asignamos un auto decremento de valor 2 a lo que tiene x actualmente 
x /= 2; # * Dividimos con el valor 2 a lo que tiene x actualmente 
x *= 2; # * Dividimos con el valor 2 a lo que tiene x actualmente 


# * Fechas

# * Para trabajar con una fecha, debe importar el módulo: date

from datetime import date

print(date.today())

# * Conversion de tipos de datos

print("El dia de hoy es:" + str(date.today()))

# * Recompilar Información

print("Hola explorer, se bienvenido ¿En que puedo ayudarte?")
name = input("Por favor, Introduce tu nombre: ")
print("Saludos explorer: " + name +" =)")

print("=======Calculadora=======")
first_Number = int(input("Ingresa el primer Numero:"))
second_Number = int(input("Ingresa el segundo Numero:"))
print(first_Number+second_Number)
