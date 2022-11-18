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