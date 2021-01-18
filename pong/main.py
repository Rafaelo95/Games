import turtle
import game
import time
from ctypes import windll

timeBeginPeriod = windll.winmm.timeBeginPeriod
timeBeginPeriod(1)

SCALE = 20

game = game.Game()

screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor('black')
screen.setup(game.width, game.height)
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

ball = turtle.Turtle()
ball.color('red')
ball.shape('circle')
ball.penup()

paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('yellow')
paddle_a.shapesize(game.paddle_height / SCALE, game.paddle_width / SCALE)
paddle_a.penup()

paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('green')
paddle_b.shapesize(game.paddle_height / SCALE, game.paddle_width / SCALE)
paddle_b.penup()

# TEXT
text = turtle.Turtle()
text.color('white')
text.penup()
text.goto(0, game.height / 2 - 40)
text.hideturtle()


def player_a_up():
    game.paddle_a_up()


def player_a_down():
    game.paddle_a_down()


def player_b_up():
    game.paddle_b_up()


def player_b_down():
    game.paddle_b_down()


screen.listen()
screen.onkeypress(player_a_up, 'w')
screen.onkeypress(player_a_down, 's')
screen.onkeypress(player_b_up, 'Up')
screen.onkeypress(player_b_down, 'Down')


prev_points_a = None
prev_points_b = None
DEFAULT_SLEEP = 0.005
sleep_time = DEFAULT_SLEEP
index = 0

finished = turtle.Turtle()
finished.color('white')
finished.hideturtle()
already_finished = False

while True:
    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    paddle_b.goto(game.paddle_b_pos)

    if prev_points_a != game.points_a or prev_points_b != game.points_b:
        text.clear()
        text.write(f'Player A: {game.points_a}, Player B: {game.points_b}',
                   align='center',
                   font=('Courier', 20, 'bold'))
        prev_points_a = game.points_a
        prev_points_b = game.points_b

        # PUT SPEED BACK TO ITS ORIGINAL
        sleep_time = DEFAULT_SLEEP

    if game.game_over and not already_finished:
        finished.clear()
        finished.write('Game Over!', align='center', font=('Courier', 35, 'bold'))
        already_finished = True

    screen.update()
    time.sleep(sleep_time)

    # INCREASING SPEED GRADUALLY
    if sleep_time > 0.0005 and index % 20 == 0:
        sleep_time -= 0.00005
    index += 1