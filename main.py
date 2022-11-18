# SERPIENTE PYTHON
# Mateo Rodriguez, David Sanchez Ficha: 2502640
"""En el siguiente grupo de codigo se realiza la importación de la libreria Turtle que sirve para trabajos graficos y las otras paginas de las diferentes funciones del juego. """

from turtle import Screen, Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time


"""En esta sección de codigo se instancia el objeto screen de la clase Turtle para darle las propiedades y atributos deseados, el largo, el ancho, el color y el titulo, asi screen servirá como la pantalla del juego."""
screen = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""
Aqui se hace un llamado a las demas clases que se han definido importando asi sus metodos y atributos
"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""
Aqui screen hace un llamado al metodo listen que sirve para recibir las entradas de pantalla
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""
Aqui se define que mientras  el juego este en ejecucion el objeto pantalla se actualice y tenga una pausa de 
0.1 milisegundo
"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detecta la colision con la comida
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        """
        llama al metodo increase_score para que aumente un punto
        """
        scoreboard.increase_score()
    #Detecta la colision con el muro
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head. ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        #Aqui llama a la funcion de scoreboard game_over para finalizar el juego al colisionar con  el muro 
        scoreboard.game_over()
    #Detecta la colision con sigo mismo.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

"""
El comando screen.exitonclick es uno de los mas importantes y define que mientras todo el anterior codigo en ejecucion se cierre siempre y cuando se le de un click a la pantalla del juego
"""
screen.exitonclick()

