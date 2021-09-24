año = int(input("Introduzca un año: "))
if año>=1582:
    if año%4!=0:
        print('Año comun1..')
    elif (año%100) !=0:
        print('Es un año bisiesto2...')
    elif (año%400)!=0:
        print('Año comun3...')
    else:
        print('Año bisesto4..')
else:
    print('No dentro del perido del calendiario Greogoriano')
