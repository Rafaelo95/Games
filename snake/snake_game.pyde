import config
import snake
import food
import score


def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)    
    frameRate(10)


def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    score.show()
    
    if snake.touch_food():
        snake.eat_food()
        food.reset_food_position()
        score.scr += 1
    
    if snake.eats_self():
        print("GAME OVER!")
        noLoop()

def keyPressed():
    if keyCode == UP and config.current_direction != "down":
        config.current_direction = "up"
    elif keyCode == LEFT and config.current_direction != "right":
        config.current_direction = "left"
    elif keyCode == RIGHT and config.current_direction != "left":
        config.current_direction = "right"
    elif keyCode == DOWN and config.current_direction != "up":
        config.current_direction = "down"
