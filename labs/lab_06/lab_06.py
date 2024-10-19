import tkinter as tr
import random
import math


class Balls:

    def __init__(self,
                 x,
                 y,
                 r,
                 color,
                 dx=0,
                 dy=0,
                 is_main=False,
                 is_dangerous=False):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        self.oval = None
        self.is_main = is_main
        self.is_dangerous = is_dangerous

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

        if self.is_main:
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
    INIT_DX = random.randrange(-5, 5, 2)
    INIT_DY = random.randrange(-5, 5, 2)

    if event.num == 1:
        if main_ball is not None and main_ball.oval is not None:
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
        else:
            main_ball = Balls(event.x,
                              event.y,
                              MAIN_BALL_RADIUS,
                              MAIN_BALL_COLOR,
                              INIT_DX,
                              INIT_DY,
                              is_main=True)
            main_ball.draw()

    elif event.num == 2:
        if main_ball is not None and main_ball.oval is not None:
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dx = -main_ball.dx
            else:
                main_ball.dy = -main_ball.dy


def resize_canvas(event):
    global WIDTH, HEIGHT
    WIDTH = event.width
    HEIGHT = event.height
    canvas.config(width=WIDTH, height=HEIGHT)

    if "main_ball" in globals(
    ) and main_ball is not None and main_ball.oval is not None:
        if main_ball.x + main_ball.r > WIDTH:
            main_ball.x = WIDTH - main_ball.r
        elif main_ball.x - main_ball.r < 0:
            main_ball.x = main_ball.r

        if main_ball.y + main_ball.r > HEIGHT:
            main_ball.y = HEIGHT - main_ball.r
        elif main_ball.y - main_ball.r < 0:
            main_ball.y = main_ball.r

        canvas.coords(
            main_ball.oval,
            main_ball.x - main_ball.r,
            main_ball.y - main_ball.r,
            main_ball.x + main_ball.r,
            main_ball.y + main_ball.r,
        )


def generate_non_intersecting_balls(num_balls, num_dangerous):
    balls = []
    attempts = 0
    max_attempts = 1000  # Prevents infinite loops

    while len(balls) < num_balls and attempts < max_attempts:
        x = random.randint(COLORFUL_BALL_RADIUS, WIDTH - COLORFUL_BALL_RADIUS)
        y = random.randint(COLORFUL_BALL_RADIUS, HEIGHT - COLORFUL_BALL_RADIUS)

        intersects = False
        for ball in balls:
            distance = math.sqrt((x - ball.x)**2 + (y - ball.y)**2)
            if distance < ball.r + COLORFUL_BALL_RADIUS:
                intersects = True
                break

        if not intersects:
            is_dangerous = len([b for b in balls if b.is_dangerous
                               ]) < num_dangerous
            color = "red" if is_dangerous else random.choice(BALL_COLORS)
            new_ball = Balls(x,
                             y,
                             COLORFUL_BALL_RADIUS,
                             color,
                             is_main=False,
                             is_dangerous=is_dangerous)
            balls.append(new_ball)

        attempts += 1

    return balls


def check_collision(ball1, ball2):
    distance = math.sqrt((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)
    return distance <= ball1.r + ball2.r


def handle_collision(main_ball, colorful_ball):
    # Calculate normal vector
    nx = colorful_ball.x - main_ball.x
    ny = colorful_ball.y - main_ball.y
    dist = math.sqrt(nx**2 + ny**2)
    nx /= dist
    ny /= dist
    # Calculate speed
    speed = math.sqrt(main_ball.dx**2 + main_ball.dy**2)
    # main_ball direction is reversed
    main_ball.dx = -speed * nx
    main_ball.dy = -speed * ny
    # colorful_ball continues to travel in the same direction
    colorful_ball.dx = speed * nx
    colorful_ball.dy = speed * ny


def game_over():
    global game_running
    game_running = False  # Stop the main loop
    canvas.delete("all")
    canvas.create_text(WIDTH / 2,
                       HEIGHT / 2 - 50,
                       text="Game Over",
                       font=("Arial", 36),
                       fill="white")

    if "restart_button" in globals():
        canvas.delete(restart_button_window)

    restart_button = tr.Button(window, text="Restart", command=restart_game)
    restart_button_window = canvas.create_window(WIDTH / 2,
                                                 HEIGHT / 2 + 50,
                                                 window=restart_button)


def restart_game():
    global main_ball, colorful_balls, NUM_COLORFUL_BALLS, NUM_DANGEROUS_BALLS, WIDTH, HEIGHT, game_running
    WIDTH = SAVED_WIDTH
    HEIGHT = SAVED_HEIGHT
    window.geometry(f"{WIDTH}x{HEIGHT}")
    # Clear the canvas
    canvas.delete("all")
    main_ball = None

    # Re-generate colorful balls
    colorful_balls = generate_non_intersecting_balls(NUM_COLORFUL_BALLS,
                                                     NUM_DANGEROUS_BALLS)

    # Draw new balls
    for ball in colorful_balls:
        ball.draw()

    game_running = True  # Set the game to running state
    main()  # Restart the main loop


def main():
    global colorful_balls, main_ball, game_running

    if not game_running:  # Only run if the game is in running state
        return

    if main_ball is not None and main_ball.oval is not None:
        main_ball.move()

        for ball in colorful_balls:
            if check_collision(main_ball, ball):
                if ball.is_dangerous:
                    game_over()
                    return
                handle_collision(main_ball, ball)

        for ball in colorful_balls:
            if ball.dx != 0 or ball.dy != 0:
                ball.move()

        new_colorful_balls = []
        for ball in colorful_balls:
            if (-ball.r * 2 <= ball.x <= WIDTH + ball.r * 2 and
                    -ball.r * 2 <= ball.y <= HEIGHT + ball.r * 2):
                new_colorful_balls.append(ball)
            else:
                ball.hide()

        num_new_balls = NUM_COLORFUL_BALLS - len(new_colorful_balls)
        num_new_dangerous = NUM_DANGEROUS_BALLS - len(
            [b for b in new_colorful_balls if b.is_dangerous])
        new_balls = generate_non_intersecting_balls(num_new_balls,
                                                    num_new_dangerous)
        for ball in new_balls:
            ball.draw()

        colorful_balls = new_colorful_balls + new_balls

    window.after(10, main)


window = tr.Tk()
window.title("Dangerous Ball Game")

WIDTH = random.randint(500, 1000)
HEIGHT = random.randint(500, 800)
SAVED_WIDTH = WIDTH
SAVED_HEIGHT = HEIGHT
MAIN_BALL_RADIUS = 20
MAIN_BALL_COLOR = "blue"
BG_COLOR = "#000408"

NUM_COLORFUL_BALLS = random.randint(10, 20)
NUM_DANGEROUS_BALLS = 3  # Fixed number of dangerous red balls
COLORFUL_BALL_RADIUS = 15
BALL_COLORS = ["green", "yellow", "purple", "orange", "pink", "cyan"]

window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tr.Canvas(window, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Button-2>", mouse_click)

window.bind("<Configure>", resize_canvas)

main_ball = None
colorful_balls = generate_non_intersecting_balls(NUM_COLORFUL_BALLS,
                                                 NUM_DANGEROUS_BALLS)
for ball in colorful_balls:
    ball.draw()

game_running = True

main()

window.mainloop()
