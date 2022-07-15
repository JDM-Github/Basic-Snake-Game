import os
import time
import msvcrt
import random

WIDTH = 30
HEIGHT = 15
MOVE = {
    "S": "STOP", "U": "UP", "D": "DOWN",
    "L": "LEFT", "R": "RIGHT"
}


class SnakeTail():
    """Snake tail"""

    def __init__(self, x=0, y=0, position=None) -> None:
        self.x = x
        self.y = y


class SnakeGame():
    """Snake Game"""

    def __init__(self) -> None:
        self.setup()

    def setup(self):
        """Setup the variable"""
        self.width = WIDTH
        self.height = HEIGHT
        self.gameOver = False
        self.snake_x = WIDTH//2
        self.snake_y = HEIGHT//2
        self.score = 0
        self.mover = MOVE["S"]
        self.fX = random.randint(1, WIDTH-2)
        self.fY = random.randint(1, HEIGHT-2)
        self.num_tail = list()
        self.tail_add(-1)

    def tail_add(self, x_a=0, y_a=0):
        """Tail Adder"""
        self.num_tail.append(SnakeTail(self.snake_x+x_a, self.snake_y+y_a))

    def run(self):
        """Run The Game"""
        os.system("cls")
        self.drawGame()
        self.checkInput()
        self.moveSnake()
        self.logic()

    def drawGame(self):
        """Draw the Game"""
        for h in range(self.height):
            for w in range(self.width):
                if self.snake_x == w and self.snake_y == h:
                    print("O", end="")
                    continue
                for tail in self.num_tail:
                    if tail.x == w and tail.y == h:
                        print("o", end="")
                        break
                else:
                    if self.fX == w and self.fY == h:
                        print("F", end="")
                    else:
                        print("#" if (h == 0 or h == (self.height-1))
                              else ("#" if (w == 0 or w == (self.width - 1))
                                    else " "), end="")
            print()
        print(f"Score: {self.score}")

    def checkInput(self):
        """Check Input"""
        if msvcrt.kbhit():
            if result := msvcrt.getch():
                if str(result).upper() == "B'W'":
                    if not (self.mover == MOVE["D"]):
                        self.mover = MOVE["U"]
                elif str(result).upper() == "B'S'":
                    if not (self.mover == MOVE["U"]):
                        self.mover = MOVE["D"]
                elif str(result).upper() == "B'A'":
                    if not (self.mover == MOVE["R"]):
                        self.mover = MOVE["L"]
                elif str(result).upper() == "B'D'":
                    if not (self.mover == MOVE["L"]):
                        self.mover = MOVE["R"]
                elif str(result).upper() == "B'Q'":
                    self.gameOver = True

    def moveSnake(self):
        """Move The Snake"""
        self.x_pos = self.snake_x
        self.y_pos = self.snake_y
        if self.mover == MOVE["U"]:
            self.snake_y -= 1
        elif self.mover == MOVE["D"]:
            self.snake_y += 1
        elif self.mover == MOVE["R"]:
            self.snake_x += 1
        elif self.mover == MOVE["L"]:
            self.snake_x -= 1
        self.prevx = self.num_tail[0].x
        self.prevy = self.num_tail[0].y
        self.num_tail[0].x = self.x_pos
        self.num_tail[0].y = self.y_pos
        for index in range(1, len(self.num_tail)):
            if self.snake_x == self.num_tail[index].x and self.snake_y == self.num_tail[index].y:
                self.gameOver = True
                break
            try:
                self.prevx2 = self.num_tail[index].x
                self.prevy2 = self.num_tail[index].y
                self.num_tail[index].x = self.prevx
                self.num_tail[index].y = self.prevy
                self.prevx = self.prevx2
                self.prevy = self.prevy2
            except IndexError:
                break

    def logic(self):
        """Logic of Game"""
        if self.snake_x == 0:
            self.snake_x = self.width-2
        elif self.snake_x == self.width-1:
            self.snake_x = 1
        elif self.snake_y == 0:
            self.snake_y = self.height-2
        elif self.snake_y == self.height-1:
            self.snake_y = 1
        if self.snake_x == self.fX and self.snake_y == self.fY:
            self.score += 10
            self.fX = random.randint(1, WIDTH-2)
            self.fY = random.randint(1, HEIGHT-2)
            if self.mover == MOVE["U"]:
                self.tail_add(0, 1)
            elif self.mover == MOVE["D"]:
                self.tail_add(0, -1)
            elif self.mover == MOVE["R"]:
                self.tail_add(-1)
            elif self.mover == MOVE["L"]:
                self.tail_add(1)


if __name__ == "__main__":
    game = SnakeGame()
    while not game.gameOver:
        game.run()
        time.sleep(0.1)
