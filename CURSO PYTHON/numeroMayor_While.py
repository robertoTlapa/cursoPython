#Almacenare el numero más grande actual aqui numeor
numeroMayor =-99999999
#lee el primer varlor
numero = int(input('Introduzca un numero o escriba -1 para detener la ejecucion:'))
# Si el numero no es igual a -1 continuaremos con la ejecucion de bucle
while numero != -1:
    #¿Es el mumero leido mas grande que mi numeroMayor?
    if numero>=numeroMayor:
        #si si, actualizar el numeroMayor = numero leido
        numeroMayor=numero
        print(numeroMayor)
        #leer el siguiente numero
    numero= int(input('Introduce un númro o escribe -1 para finalizar la ejecucion:'))
    #imprimer el numero mas grande
print('El numero mas grande es: ', numeroMayor)
    
