
# * Crear una lista

import math


planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'];

# * Para acceder a los elementos de una lista
print(planets[0])
print(planets[1])
print(planets[2])

# * Otra manera de acceder a los elementos es asi
acum = 0;
for planet in planets:
    acum += 1 
    print(f"Planet {acum}: {planet}")

# * Ver la longitud de mi arreglo
len_planets = len(planets);
print(f"El sistema solar donde se encuentra tiene {len_planets}")

# * Agregar valores a las listas
# * Append agrega el valor que le pasemos hasta ultimo
planets.append('Pluton');
print(planets)

# * Eliminar valores de una lista
# * El metodo pop elimina el ultimo elemento de la lista
planets.pop()
print(planets)

# * Indices Negativos
# * Los indices negativos comienzan al final de la lista y trabajan
# * hacia atras E/P: el indice -1 comienza desde el ultimo elemento y 
# * y asi sucesivamente 

print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

# * Buscar un valor en una lista
# * usamos el metodo index() este metodo recibe como parametro
# * un string que es el que se buscara en nuestra lista si existe
# * el metodo nos devolvera el indice actual de ese elemento, si no
# * nos devolvera un -1 apuntando a que el elemento que buscamos,
# * no existe

findIndexPlanet = planets.index('Earth')
print(f"El planeta tierra se encuentra en la posicion: {findIndexPlanet}")

# * Almacenar números en listas
print("---------- Trabajando con listas Numericas ----------")
gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]
print(gravity_on_planets)


bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

# * Metodos min() y max()
# * El metodo min() devuelve el numero mas pequeño de una lista

print(f"El numero mas pequeño de lista es:{min(gravity_on_planets)}")

# * El metodo max() devuelve el numero mas grande de una lista
print(f"El numero mas grande de la lista es:{max(gravity_on_planets)}")

# * Manipular datos de la lista
# * Para poder usar el slice y tomar una porcion o segmento de nuestra
# * lista usamos los corchetes[], y dentro de los corchetes poner
# * los indices(inicial y final), esto hara una seleccion de los 
# * elementos que estamos diciendo que queremos.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print(planets_before_earth)

# * Uniendo Listas 
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

friends = ['Juan','Sam','Jose'];
family = ['Sarah','Pedro','Kristine']

union = friends + family
print(union)

# * Ordenar Listas
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
