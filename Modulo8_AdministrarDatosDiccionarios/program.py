
# * Creacion de un diccionario
planet = {
    'name': 'Earth',
    'moons': 1
}

# * Para leer datos de un diccionario
print(planet.get('name'))
print(planet['moons'])

# * Aunque el comportamiento de get y los corchetes ([ ]) 
# * suele ser el mismo para recuperar elementos, hay una 
# * diferencia principal. Si una clave no está disponible, 
# * get devuelve None y [ ] genera un error KeyError.

# * Modificación de valores de un diccionario

planet.update({'name':'Mars'})
print(planet)

planet['name'] = 'Earth'
print(planet)


# * La principal ventaja de usar update es la capacidad de modificar 
# * varios valores en una operación. Los dos ejemplos siguientes son 
# * lógicamente los mismos, pero la sintaxis es diferente. Puedes usar 
# * la sintaxis que creas más adecuada. Para actualizar valores 
# * individuales, la mayoría de los desarrolladores eligen corchetes.

# * Adición y eliminación de claves

planet['orbital period'] = 4333
print(planet)
# * Para quitar una clave, usa pop. pop devuelve el valor y quita la 
# * clave del diccionario. Para eliminar orbital period, puedes usar el 
# * código siguiente:

planet.pop('orbital period');
print(planet)

# * Tipos de data complejos

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet)

#  * Recuperación de todas las claves y valores

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# * Determinar si existe una clave en un diccionario
# * La palabra clave in nos ayuda a comprobar si existe una 
# * clave en el diccionario de datos con ese nombre

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# * Recuper todos los valores de un diccionario

total_rainfall = 0
for value in rainfall.values():
    total_rainfall += value
print(f'Total: {total_rainfall}cm')