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

GAME_WIDTH = 9
GAME_HEIGHT = 9

#### Put class definitions here ####
class Yellow_Star(GameElement):
    IMAGE="Star"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a yellow star! You have %d items!" %(len(player.inventory)))


class Best_Tree(GameElement):
    IMAGE="BestTree"
    SOLID=True

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

class Rainbow_Rock(GameElement):
    IMAGE = "RainbowRock"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a Rainbow Rock! Weird.  Do those even exists? You have %d items!" %(len(player.inventory)))



class Rainbow_Star(GameElement):
    IMAGE="RainbowStar"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a RAINBOW STAR! You have %d items!" %(len(player.inventory)))

class Rainbow_Star2(GameElement):
    IMAGE="RainbowStarGif"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("This is another Rainbow Star--it may be inferior...I'm not sure. You have %d items!" %(len(player.inventory)))


class Rainbok_Block(GameElement):
    IMAGE="RainbowBlock"
    SOLID=True

class West_Ramp(GameElement):
    IMAGE="WestRamp"
    SOLID=True

class North_Ramp(GameElement):
    IMAGE="NorthRamp"
    SOLID=True

class East_Ramp(GameElement):
    IMAGE="EastRamp"
    SOLID=True

class South_Ramp(GameElement):
    IMAGE="SouthRamp"
    SOLID=True

class Grass_Block(GameElement):
    IMAGE="GrassBlock"
    SOLID=True


class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        


class Character(GameElement):
    IMAGE="Horns"
    SOLID=True

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

class SadChild(GameElement):
    IMAGE="Boy"
    SOLID=True

    def interact(self, player):
        dialogue=[
        GAME_BOARD.draw_msg("Hello Traveler. If you were planning on having a nice time here, you came at the wrong time. *sniffle*"),
        GAME_BOARD.draw_msg("All of our plants are dead.  We have no food. Soon we will all be dead, too. *tear runs down cheek*"),
        GAME_BOARD.draw_msg("If only someone would bring us Best Tree seeds we could plant them in the lava to turn it to water and revive our crops."),
        GAME_BOARD.draw_msg("Alas! No one here has the strength to go. *can no longer control his desperate sobbing*"),
        GAME_BOARD.draw_msg("If you got some for us, we would be so happy.  We might even have a happy party, for once. My parents died at the last party. It was not happy.")
        ]
        i=0
        while i < len(dialogue)-1:
            if KEYBOARD[key.ENTER]:
                i+=1

        # GAME_BOARD.draw_msg("Hello Traveler. If you were planning on having a nice time here, you came at the wrong time. *sniffle*")
        # GAME_BOARD.draw_msg("All of our plants are dead.  We have no food. Soon we will all be dead, too. *tear runs down cheek*")
        # GAME_BOARD.draw_msg("If only someone would bring us Best Tree seeds we could plant them in the lava to turn it to water and revive our crops.")
        # GAME_BOARD.draw_msg("Alas! No one here has the strength to go. *can no longer control his desperate sobbing*")
        # GAME_BOARD.draw_msg("If you got some for us, we would be so happy.  We might even have a happy party, for once. My parents died at the last party. It was not happy.")

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    # Initialize and register rock 1
    # rock1=Rock()
    # GAME_BOARD.register(rock1)
    # GAME_BOARD.set_el(2, 1, rock1)

    #Initialize and register rock 2
    Star=Yellow_Star()
    GAME_BOARD.register(Star)
    GAME_BOARD.set_el(5,4, Star)

    rock2 = Blue_Rock()
    GAME_BOARD.register(rock2)
    GAME_BOARD.set_el(2, 2, rock2)


    # best_tree_positions=[
    #         (0,0),
    #         (0,8),
    #         (8,0),
    #         (8,8)
    #         ]
    # best_trees=[]
    
    # for pos in best_tree_positions:
    #     tree=Best_Tree()
    #     GAME_BOARD.register(tree)
    #     GAME_BOARD.set_el(pos[0], pos[1], tree)
    #     best_trees.append(tree)



    # rock_positions=[
    #     (2,1),
    #     (1,2),
    #     (3,2),
    #     (2,3)
    #     ]
    # rocks = []

    # for pos in rock_positions:
    #     rock=Rock()
    #     GAME_BOARD.register(rock)
    #     GAME_BOARD.set_el(pos[0], pos[1], rock)
    #     rocks.append(rock)
    # rocks[-1].SOLID = False

    # for rock in rocks:
    #     print rock

    heart = Heart()
    GAME_BOARD.register(heart)
    GAME_BOARD.set_el(6, 2, heart)

    # rainbow_star2=Rainbow_Star2()
    # GAME_BOARD.register(rainbow_star2)
    # GAME_BOARD.set_el(8,6,rainbow_star2)
    
    # rainbow_star=Rainbow_Star()
    # GAME_BOARD.register(rainbow_star)
    # GAME_BOARD.set_el(7,6,rainbow_star)

    # rainbow_rock=Rainbow_Rock()
    # GAME_BOARD.register(rainbow_rock)
    # GAME_BOARD.set_el(0,4, rainbow_rock)

    sad_child = SadChild()
    GAME_BOARD.register(sad_child)
    GAME_BOARD.set_el(4, 7, sad_child)

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)

    print PLAYER

    GAME_BOARD.draw_msg("This game, it is the saddest. :( :( :*( ")

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