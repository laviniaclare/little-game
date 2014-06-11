import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE="Rock"
    SOLID = True

class Blue_Rock(GameElement):
    IMAGE="Rock2"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a BLUE ROCK! You have %d items!" %(len(player.inventory)))

class Heart(GameElement):
    IMAGE = "Heart"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a heart! You have %d items!" %(len(player.inventory)))


class Character(GameElement):
    IMAGE="Horns"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None
####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    # Initialize and register rock 1
    # rock1=Rock()
    # GAME_BOARD.register(rock1)
    # GAME_BOARD.set_el(2, 1, rock1)

    #Initialize and register rock 2
    rock2 = Blue_Rock()
    GAME_BOARD.register(rock2)
    GAME_BOARD.set_el(2, 2, rock2)
   

    #iNITALIZE moar rocks
    rock_positions=[
        (2,1),
        (1,2),
        (3,2),
        (2,3)
        ]
    rocks = []

    for pos in rock_positions:
        rock=Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)
    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    heart = Heart()
    GAME_BOARD.register(heart)
    GAME_BOARD.set_el(0, 0, heart)


    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(4, 4, PLAYER)

    print PLAYER

    GAME_BOARD.draw_msg("BEST GAME EVER (doesn't do anything yet)!!!!111!!!11!")

def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)
            # player.inventory.append(heart)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)