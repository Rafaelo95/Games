import config
import food
from copy import deepcopy

snake_position = [[0, 0], [config.SCALE, 0], [config.SCALE * 2, 0]]

def show():
    for segment in snake_position:
        fill(255)
        rect(segment[0], segment[1], config.SCALE, config.SCALE)


def check_edges():
    snake_head = snake_position[-1]
    if snake_head[1] < 0:
        snake_head[1] = config.WINDOW_HEIGHT
    elif snake_head[1] >= config.WINDOW_HEIGHT:
        snake_head[1] = 0
    elif snake_head [0] < 0:
        snake_head[0] = config.WINDOW_WIDTH
    elif snake_head[0] >= config.WINDOW_WIDTH:
        snake_head[0] = 0
        
    
def move():
    current_changes = config.DIRECTIONS[config.current_direction]
    
    snake_copy = deepcopy(snake_position)
    snake_position[-1][0] += current_changes[0]
    snake_position[-1][1] += current_changes[1]
    
    for i in range(len(snake_position) - 2, -1, -1):
        snake_position[i] = snake_copy[i + 1]
    
    check_edges()

def touch_food():
    return snake_position[-1] == food.food_position


def eat_food():
    snake_position.insert(0, snake_position[1])
    

def eats_self():
    head = snake_position[-1]
    return any(seg == head for seg in snake_position[:-1])
