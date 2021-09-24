#Programa que lee una secuencia de numero y cuenta ciantos numero son pares y
#Cuantos son impares, el progrma termina cuando  se ingrese un cero
numerosImpares = 0
numerosPares = 0
#Leer el primer numero
numero = int(input('Introduce el numero o escribe 0 para terminar la ejecucion: '))
while numero != 0:
    #Verificar si en numero leido es impar
    if numero % 2 == 1:
        #Incrementar el conteno de numero Impares
        numerosImpares +=1
    else:
        #Incrementar el conteo de numero pares
        numerosPares += 1
    #Leer el siguiente numero o detener el ciclo si se introduce 0
    numero = int(input('Introduce un umero o escribe 0 para terminar la ejecucion: '))
#Imprimir los resultados
print('Numero pares: ', numerosPares)
print('Numero impares: ', numerosImpares)
