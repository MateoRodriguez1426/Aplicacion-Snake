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