import tkinter as tr
import random
import math


class Balls:

    def __init__(self, x, y, r, color, dx=0, dy=0, main=False, dangerous=False):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        self.oval = None
        self.main = main
        self.dangerous = dangerous

    def draw(self):
        if self.oval is None:
            self.oval = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color,
                outline=BG_COLOR,
            )

    def move(self):
        speed_factor = (WIDTH + HEIGHT) / 1000
        adjusted_dx = self.dx * speed_factor
        adjusted_dy = self.dy * speed_factor

        self.x += adjusted_dx
        self.y += adjusted_dy

        if self.main:
            if self.x + self.r > WIDTH:
                self.dx = -self.dx
                self.x = WIDTH - self.r
            elif self.x - self.r < 0:
                self.dx = -self.dx
                self.x = self.r

            if self.y + self.r > HEIGHT:
                self.dy = -self.dy
                self.y = HEIGHT - self.r
            elif self.y - self.r < 0:
                self.dy = -self.dy
                self.y = self.r

        canvas.coords(
            self.oval,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
        )

    def hide(self):
        if self.oval is not None:
            canvas.delete(self.oval)
            self.oval = None


def mouse_click(event):
    global main_ball
    INIT_DX = 3
    INIT_DY = 3

    if event.num == 1:
        if main_ball is not None and main_ball.oval is not None:
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
        else:
            main_ball = Balls(
                event.x,
                event.y,
                MAIN_BALL_RADIUS,
                MAIN_BALL_COLOR,
                INIT_DX,
                INIT_DY,
                main=True,
            )
            main_ball.draw()

    elif event.num == 2:
        if main_ball is not None and main_ball.oval is not None:
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dx = -main_ball.dx
            else:
                main_ball.dy = -main_ball.dy


def gen_colorballs():
    balls = []
    for _ in range(10):
        x = random.randint(COLORFUL_BALL_RADIUS, WIDTH - COLORFUL_BALL_RADIUS)
        y = random.randint(COLORFUL_BALL_RADIUS, HEIGHT - COLORFUL_BALL_RADIUS)
        color = "red" if _ == 0 else random.choice(BALL_COLORS)
        dangerous = color == "red"
        ball = Balls(x, y, COLORFUL_BALL_RADIUS, color, dangerous=dangerous)
        balls.append(ball)
        ball.draw()
    return balls


def colided(ball1, ball2):
    distance = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    return distance <= ball1.r + ball2.r


def main():
    global colorful_balls, main_ball

    if main_ball is not None and main_ball.oval is not None:
        main_ball.move()

        for ball in colorful_balls:
            if colided(main_ball, ball):
                if ball.dangerous:
                    exit()
                else:
                    ball.hide()
                    colorful_balls.remove(ball)

        for ball in colorful_balls:
            if ball.dx != 0 or ball.dy != 0:
                ball.move()

    window.after(10, main)


window = tr.Tk()
window.title("Ball Game")

WIDTH = random.randint(500, 1000)
HEIGHT = random.randint(500, 800)
MAIN_BALL_RADIUS = 20
MAIN_BALL_COLOR = "blue"
BG_COLOR = "#000408"

COLORFUL_BALL_RADIUS = 15
BALL_COLORS = ["green", "yellow", "purple", "orange", "pink", "cyan"]

window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tr.Canvas(window, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()

canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Button-2>", mouse_click)

main_ball = None
colorful_balls = gen_colorballs()

main()

window.mainloop()
