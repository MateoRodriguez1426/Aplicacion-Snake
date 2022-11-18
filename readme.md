# Todo
- Crear cuerpo de la culebra
- Mover el objeto
- Controlar el movimiento
- Detectar colision con la comida
- Puntaje
- Detectar colision con los muros
- Detectar cuando colisiona contra si misma
# Aplicacion-Snake
#SERPIENTE PYTHON
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

# FOOD.py
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
             
# SCOREBOARD
  from turtle import Turtle

  """
  Define la fuente y alineacion de la letra
  """
  ALIGNMENT = "center"
  FONT = ("Courier", 24, "normal")


  """
  Esta es la clase Scoreboard
  """
  class Scoreboard(Turtle):

      """
      Como toda clase esta tiene una funcion contructora que inicializa los valores predeterminados
      en este caso definira el color, el puntaje, la ubicacion y la inicializacion de la funcion de actualizacion
      de puntaje
      """

      def __init__(self):
          super().__init__()
          self.score = 0
          self.color("white")
          self.penup()
          self.goto(0, 270)
          self.hideturtle()
          self.update_scoreboard()


      """
      Este metodo se encarga de actualizar el scoreboard, asi tiene a dispocision los atributos de score
      """
      def update_scoreboard(self):
          self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

      def game_over(self):
          self.goto(0, 0)
          self.write("GAME OVER", align=ALIGNMENT, font=FONT)
      """
      Este metodo se encarga de actualizar el score aumentado uno y enlazado update_scoreboard
      """
      def increase_score(self):
          self.score += 1
          self.clear()
          self.update_scoreboard()

# SNAKE
    #Esta es la pagina de la serpiente y se encarga de darle los atributos y metodos a la serpiente
    from turtle import Turtle
    #Define las posiciones iniciales
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
    #Define la distancia que se mueven los bloques
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    """
    Esta es la clase snake
    """
    class Snake:

        """
        Esta es la clase constructora que inicializa las propiedades de la clase, en 
        este caso crea una tupla vacia que contendra los segmentos, inicia el metodo 
        create_snake y  define el atributo head
        """
        def __init__(self):
            """
            Defgine una tupla vacia que cumple la funcion de segmento de la serpiente
            """
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]
        """
        Esta es la funcion create_snake y al estar definida dentro del metodo __init__ siempre 
        iniciara automaticamente
        """
        def create_snake(self):
            """
            En el metodo tiene definido un for que recorre la tupla definida como STARTING_POSITIONS y 
            por cada recorrido que haga llamara al metodo add_segment que agregara un segmento
            """
            for position in STARTING_POSITIONS:
                self.add_segment(position)


        """
        Esta es la funcion add_segment y define los atributos y propiedades de los segmentos,
        en este caso el color, la propiedad penup y la posicion 
        """
        def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            """
            Aqui mediante el metodo append le agrega al segmento de la funcion __init__ un nuevo 
            segmento con las propiedades que se definieron anteriormente
            """
            self.segments.append(new_segment)

        """
        Metodo extend que define la ubicacion de los nuevos segmentos creados en el metodo add_segment 
        para esto le resta 1 al indice de los segmentos
        """
        def extend(self):
            self.add_segment(self.segments[-1].position())
        """
        metodo move 
        """
        def move(self):
            """
            Dentro de si contiene un for que realiza un recorrido dentro del rango de elementos que tiene segments 
            """
            for seg_num in range(len(self.segments)- 1, 0, -1):
                """
                Asi por cada recorrido le asignara una nueva coordenada x 
                """
                new_x = self.segments[seg_num - 1].xcor()
                """
                Asi por cada recorrido le asignara una nueva coordenada y
                """
                new_y = self.segments[seg_num - 1].ycor()

                self.segments[seg_num].goto(new_x, new_y)

            self.head.forward(MOVE_DISTANCE)
        """
        A continuacion se definen 4 metodos que se encargan del movimiento en cuatro direcciones
        """
        def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)
