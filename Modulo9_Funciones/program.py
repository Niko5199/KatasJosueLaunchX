
#  * Funciones sin argumentos
# * Para crear una función, utilizamos la palabra clave def, 
# * seguida de un nombre, paréntesis y, después, del cuerpo con 
# * el código de función:

def rocket_parts():
    print('payload, propellant, structure')

rocket_parts()

# * Argumentos opcionales y requerido
# * El metodo any(), toma un objeto iterable y devuelve True si 
# * algun elemento del objeto iterable es True, de lo contrario es False

print(any([False,True]))

# * Uso de argumentos en una función de Python

# * Exigencia de un argumento
def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'
        
print(distance_from_earth('Moon'))

# * Varios argumentos necesarios
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855,75))

# * Funciones como argumentos
total_days = days_to_complete(238855, 75)
print(round(total_days))

# * Uso de argumentos de palabra clave en Python
# * hacemos uso de argumentos opcionales

# * La función usa el módulo datetime para definir la hora actual. 
# * Usa timedelta para permitir la operación de suma que da como 
# * resultado un objeto de hora nuevo. Después de calcular ese resultado,
# * devuelve la estimación arrival con formato de cadena.
# * Intentando llamarla sin algún argumento:

from datetime import timedelta, datetime

def arrival_time(hours=0):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime('Arrival: %A %H:%M')


print(arrival_time())

# * Uso de argumentos de variable en Python
# * En este caso, *args indica a la función que acepta cualquier número de argumentos 
# * (incluido 0). En la función, args ahora está disponible como la variable que contiene 
# * todos los argumentos como una tupla. Pruebe la función pasando cualquier número o 
# * tipo de argumentos:
def variable_length(*args):
    print(args)
variable_length(1,2,3,4)
