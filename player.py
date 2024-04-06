from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
         self.forward(MOVE_DISTANCE)  

    def go_to_start(self):
        self.goto(STARTING_POSITION)          

    # def game_over(self):
    #     self.write(f"Game Over", font=("Arial", 15, "normal")) 
    #     self.goto(0, 0)    

    def finish_game(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False