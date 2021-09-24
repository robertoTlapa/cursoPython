hora = int(input("Hora de inicio (horas): "))
minuto = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
horaMinutos=(hora*60)+minuto+dura
horas=horaMinutos//60
horasReal=horas%24
minutosReal=horaMinutos%60
print(str(horasReal)+':'+str(minutosReal))
true=54

# coloca tu código aqui
