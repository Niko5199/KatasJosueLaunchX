

from traceback import print_tb


fact = 'The Moon has no atmosphere.'
two_facts = fact + 'No sound can be heard on the Moon.'

print(two_facts)

# * Métodos string en Python

# * Title
heading = 'temperatures and facts about the moon'
print(heading.title())

# * Dividir una cadena
temperatures = 'Daylight: 260 F Nighttime: -280 F'
print(temperatures .split())

# * Buscar una cadena
temperatures = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(temperatures.find('temperature'))

# * Count
# * Otra forma de buscar contenido es usar el método .count(), que devuelve el número total 
# * de apariciones de una determinada palabra en una cadena

print(temperatures.count('Celsius'))

# * Lower Minusculas 
print("The Moon And The Earth".lower())

# * Upper Mayusculas
print('The Moon And The Earth'.upper())

mars_temperature = 'The highest temperature on Mars is about 30 C'

for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

# * isnumeric 
# * Este metodo verifica si es un numero entero en la cadena que se le esta pasando
print('30'.isnumeric())


# * isdecimal
# * Este metodo verifica si el numero es decimal

print(u'30.1'.isdecimal())

# * startsWidth
# * Verifica si el parametro que le pasamos esta al inicio de la cadena a la cual
# * aplicamos el metodo
print('-60'.startswith('-'))

# * endsWidth
# * Verifica si el parametro que le pasamos esta al final de la cadena a la cual
# * aplicamos el metodo
if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# * replace
print('Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C'))

moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
print('\n'.join(moon_facts))

# * Formato con signo de porcentaje (%)

mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))

# * El metodo format
mass_percentage2 = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage2))

# * Multiples variables
print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage2))

# * Acerca de las cadenas con f
print(f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')