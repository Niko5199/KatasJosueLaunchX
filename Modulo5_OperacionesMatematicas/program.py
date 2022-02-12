
# * Adicion Suma
answer = 30 + 12
print(answer)

# * Sustraccion Resta
difference = 30 - 12
print(difference)

# * Multiplicación
product = 30 * 12
print(product)

# * División
quotient = 1042 / 60
print(quotient)

# * Trabajando con division
# * Nota: Para redondear hacia abajo un buen metodo es usar la division de piso //
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# * Operador %

seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)


# * Orden de funcionamiento (Jerarquía de Operaciones)
# * Python respeta el orden de operación para las matemáticas. El orden de operación dicta que las expresiones 
# * deben evaluarse en el siguiente orden:

# * 1.- Paréntesis
# * 2.- Exponentes
# * 3.- Multiplicación y división
# * 4.- Suma y resta

# * Convertir cadenas en numeros

# * int
demo_int = int('215')
print(demo_int)

# * float
demo_float = float('215.3')
print(demo_float)

# * Valores Absolutos
print(abs(39 - 16))
print(abs(16 - 39))

# * Redondeo
print(round(14.6))

# * Biblioteca Math
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)