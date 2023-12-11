import turtle

def dibujar_estrella(num_puntas, longitud_lados):
    # Crear una instancia de Turtle
    t = turtle.Turtle()

    # Calcular el ángulo entre las puntas de la estrella
    angulo = 180 - 180 / num_puntas

    # Dibujar la estrella
    for _ in range(num_puntas):
        t.forward(longitud_lados)
        t.right(angulo)
       

    # Ocultar la Turtle
    t.hideturtle()

# Longitud de los lados de la estrella (fija)
longitud_fija = 100

# Solicitar al usuario el número de vértices
num_puntas = int(input("Ingrese el número de vértices para la estrella: "))

# Llamar a la función para dibujar la estrella con longitud fija
dibujar_estrella(num_puntas, longitud_fija)

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.mainloop()
