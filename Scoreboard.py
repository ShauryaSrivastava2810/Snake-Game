from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.hideturtle()
        self.penup()
        self.goto(-50, 265)
        self.write(f"Score: {self.Score}",move=False, align="left", font=("Arial", 24, "normal"))

    def update(self):
        self.write(f"Score: {self.Score}", move=False, align="left", font=("Arial", 24, "normal"))

    def increment(self):
        self.Score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(-150, 0)
        self.write("GAME OVER", move=False, align="left", font=("Arial", 48, "normal"))