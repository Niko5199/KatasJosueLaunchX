
# * Expresiones de Prueba
a = 97
b = 55

if(a < b):
    # * Instruccion de prueba
    print(b)
else:
    print("El elemento A:",a,"no es menor a b:",b)

# * Escribir declaraciones if
a2 = 93
b2 = 27
if a2 >= b2:
    print(a2)

# * Trabajando con else
msg = 'Hola';
if(msg.startswith('h')):
    print(msg)
else:
    print("El mensaje no tiene h")


# * Trabajando con elif
# * Estas instrucciones se ejecutan en el orden en que están escritas, 
# * por lo que el programa ingresará una instrucción elif solo si la primera 
# * instrucción if es FalseEstas instrucciones se ejecutan en el orden en que 
# * están escritas, por lo que el programa ingresará una instrucción elif solo 
# * si la primera instrucción if es False, recuerda que una instrucción elif 
# * sólo se ejecuta cuando la condición if es False


a3 = 27
b3 = 27

if a3 >= b3:
    print("a es mayor o igual que b")
elif a3 == b3:
    print("a es igual que b")


# * Trabajar con lógica condicional anidada

a4 = 16
b4 = 25
c4 = 27
if a4 > b4:
    if b4 > c4:
        print ("a es mayor que b y b es mayor que c")
    else: 
        print ("a es mayor que b y menor que c")
elif a4 == b4:
    print ("a es igual que b")
else:
    print ("a es menor que b")

# * El operador OR
# * Si una condicion es true automaticamente se ejecuta el if

a5 = 23
b5 = 34
if a5 == 34 or b5 == 34:
    print(a5 + b5)

# * El operador AND
# * Las condiciones deben ser verdaderas si no nos da un False

a6 = 23
b6 = 34
if a6 == 34 and b6 == 34:
    print (a6 + b6)