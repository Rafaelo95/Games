import config
import snake

x = (random(config.WINDOW_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
y = (random(config.WINDOW_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
food_position = [x, y]


def show():
    fill(0, 255, 0)
    rect(food_position[0], food_position[1], config.SCALE, config.SCALE)
    

def reset_food_position():
    x = (random(config.WINDOW_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
    y = (random(config.WINDOW_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
    food_position[0] = x
    food_position[1] = y
    
    # TO CHECK IF NEXT FOOD POSITION CAN FALL ON THE SNAKE ITSELF
