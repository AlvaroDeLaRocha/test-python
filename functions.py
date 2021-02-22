# print()
# #Nos da info del dato
# dir(1)
# #Nos dice de que tipo es el dato
# type(12)

def hello(name = "persona"):
    print("Hello " + name)

hello("joe")
hello("ryan")
hello()

# Funcion para sumar dos numeros
def add(n1, n2):
    return n1 + n2

print(add(10, 20))

# Lo mismo pero con una funcion de py por defecto
suma = lambda n1, n2: n1 + n2
print(suma(20, 5))