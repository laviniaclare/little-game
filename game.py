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

class Dead_Shrub(GameElement):
    IMAGE="DeadShrub"
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


class Grass_Block(GameElement):
    IMAGE="GrassBlock"
    SOLID=True

class Lava_Rock(GameElement):
    IMAGE="LavaRock"
    SOLID=True

class Black_Rock(GameElement):
    IMAGE="BlackRock"
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a BLACK ROCK! Maybe this will be useful later. You have %d items!" %(len(player.inventory)))

class SadChild(GameElement):
    IMAGE="SadBoy"
    SOLID=True
    def interact(self, player):
        GAME_BOARD.draw_msg("Hello Traveler. If you were planning on having a nice time here, you came at the wrong time. *sniffle* \\ All of our plants are dead.  We have no food. Soon we will all be dead, too. \\*tear runs down cheek*If only someone would bring us Best Tree seeds we could plant them in the lava to turn it to water and revive our crops.\\ Alas! No one here has the strength to go. *can no longer control his desperate sobbing*\\ If you got some for us, we would be so happy.  We might even have a happy party, for once.\\ My parents died at the last party. It was not happy.")

class Boy2(GameElement):
    IMAGE="Boy2"
    SOLID=True

class Cat(GameElement):
    IMAGE="Cat"
    SOLID=True

class Girl(GameElement):
    IMAGE="Girl"
    SOLID=True

class Girl2(GameElement):
    IMAGE="Girl2"
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


        
####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    # Initialize and register rock 1
    # rock1=Rock()
    # GAME_BOARD.register(rock1)
    # GAME_BOARD.set_el(2, 1, rock1)

    black_rock_positions=[
                        (5,4),
                        (2,3),
                        (6,6)
                        ]
    brocks=[]

    for pos in black_rock_positions:
        black_rock=Black_Rock()
        GAME_BOARD.register(black_rock)
        GAME_BOARD.set_el(pos[1], pos[0], black_rock)
        brocks.append(black_rock)

    for black_rock in brocks:
        print black_rock

    lava_rock = Lava_Rock()
    GAME_BOARD.register(lava_rock)
    GAME_BOARD.set_el(1, 7, lava_rock)

    lava_rock = Lava_Rock()
    GAME_BOARD.register(lava_rock)
    GAME_BOARD.set_el(1, 3, lava_rock)


    dead_shrub_positions=[
            (7,1),
            (7,2),
            (7,3),
            (7,4),
            (1,5)
            ]
    shrubs=[]
    
    for pos in dead_shrub_positions:
        shrub=Dead_Shrub()
        GAME_BOARD.register(shrub)
        GAME_BOARD.set_el(pos[0], pos[1], shrub)
        shrubs.append(shrub)

    for shrub in shrubs:
      print shrub

    cat_girl = Cat()
    GAME_BOARD.register(cat_girl)
    GAME_BOARD.set_el(7, 5, cat_girl)

    boy2 = Boy2()
    GAME_BOARD.register(boy2)
    GAME_BOARD.set_el(6, 3, boy2)

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
        print "key is up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"
    if KEYBOARD[key.ENTER]:
        print "enter key"

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