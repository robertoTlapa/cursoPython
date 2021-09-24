#uso de if-else clasico
numero1=int(input('Dame el primer numero:'))
numero2=int(input('Dame el segundo numero:'))
if numero1>numero2:
    numeroMayor= numero1
else:
    numeroMayor=numero2
print('El numero mayor es: ', numeroMayor)

#uso de una manera más corta de representar el if else o elif, solo
#se usa de esta manera cuando el if, else o elif tiene una unica
#rama...

if numero1>numero2: numeroMayor=numero1
else: numeroMayor=numero2
print('EJECUCION MODO 2')
print('El nuemro mayor es: ', numeroMayor)

#ejemplo 3
numero1 = int(input('Dame el numero 1: '))
numero2 = int(input('Dame el numero 2: '))
numero3 = int(input('Dame el numero 3: '))
numeroMayor = numero1

if numero2>numero1:
    numeroMayor = numero2

if numero3 > numero2:
    numeroMayor = numero3

print('El numero mayor es: ' , numeroMayor)
