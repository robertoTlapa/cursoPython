numeroSecreto = 777
numero = int(input(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
"""))
while numero != numeroSecreto:
    print('¡Ja, ja! ¡Estas atrapado en el ciclo!')
    numero = int(input('Intentalo de nuevo: '))
print('Bien hecho, muggle! Eres libre ahora!!!')
