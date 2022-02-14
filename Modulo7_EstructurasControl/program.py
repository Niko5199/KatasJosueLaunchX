
# * Ciclo while
# * Se lee de la siguiente manera: Mientras la condición se cumpla: ejecuta el código

user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')

# * Ciclo for
# * Podemos usar el metodo sleep() y recibe como parametro
# * un valor int que de el tiempo que va a hacer esperar a 
# * todo el codigo.

from time import sleep
countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)

print("Blast off!! 🚀")

