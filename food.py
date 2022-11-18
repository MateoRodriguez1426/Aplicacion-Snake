from turtle import Turtle
"""Se importa la función de random para que se den numeros   """
import random

""" Esta es la clase comida que tiene las funciones y propiedades de la comida. """
class Food(Turtle):
    """
    Este metodo constructor que se encarga de inicializar los metodos y atribustos de la clase food.
    """
    def __init__(self):
        """
        La funcion super() es usada para dar acceso a los metodos y propiedades de una clase principal o hermana.
        Ademas la funcion super() devuelve un objeto que representa la clase principal.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    """Este es un metodo que refresca la pantalla para que la comida salga aleatoriamente en otro punto dentro del rango de la pantalla. """
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
