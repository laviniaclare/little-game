#!/usr/bin/env python

import pyglet
from pyglet.window import key
from core import GameElement

SCREEN_X = 1100
SCREEN_Y = 1000

game_window = pyglet.window.Window(SCREEN_X, SCREEN_Y)


pyglet.resource.path = ["images/"]
pyglet.resource.reindex()

# Custom student changes
import game

IMAGES = {}
TILE_WIDTH = 0
TILE_HEIGHT = 0

def setup_images():
    filenames = {
            "Wall": "Wall Block.png",
            "Block": "Plain Block.png",
            "GrassBlock": "Grass Block.png",
            "StoneBlock": "Stone Block.png",
            "RainbowBlock": "Rainbow_block.png",
            "DarkDirt": "Dark_Dirt_Block.png",
            "ShortTree": "Tree Short.png",
            "TallTree": "Tree Tall.png",
            "BestTree": "Tree Cute.png",
            "DeadShrub": "Dead_Shrub.png",
            "RainbowTree": "RainbowTree.png",
            "MCTree": "Monochrome_Tree.png",
            "Lava": "Lava_block.png",
            "Water": "Water Block.png",
            "Rock": "Rock.png",
            "Rock2": "Rock2.png",
            "BlackRock": "Black_rock.png",
            "LavaRock": "Lava_Rock.png",
            "RainbowRock": "RainbowRock.png",
            "MCRock": "Monochrome_Rock.png",
            "Chest": "Chest Closed.png",
            "DoorClosed": "Door Tall Closed.png",
            "DoorOpen": "Door Tall Open.png",
            "BlueGem": "Gem Blue.png",
            "GreenGem": "Gem Green.png",
            "OrangeGem": "Gem Orange.png",
            "Star": "Star.png",
            "RainbowStar": "RainbowStar.png",
            "Selector": "Selector.png",
            "Heart": "Heart.png",
            "Key": "Key.png",
            "Boy": "Character Boy.png",
            "Boy2": "boy2.png",
            "RainbowBoy2": "RainbowBoy2.png",
            "MCBoy": "Monochrome Boy.png",
            "MCBoy2": "Monochrome_Boy.png",
            "Cat" : "Character Cat Girl.png",
            "RainbowCat": "RainbowCatGirl.png",
            "Horns": "Character Horn Girl.png",
            "Girl": "Character Pink Girl.png",
            "RainbowGirl1": "RainbowGirl1.png",
            "Girl2": "Character Purple Girl.png",
            "RainbowGirl2": "RainbowGirl2.png",
            "MCGirl": "Monochrome Girl.png",
            "Princess": "Character Princess Girl.png",
            "SadBoy": "SadChild.png",
            "SouthRamp": "Ramp South.png",
            "NorthRamp": "Ramp South.png",
            "WestRamp": "Ramp West.png",
            "EastRamp": "Ramp East.png"
            }

    for k,v in filenames.items():
        i = pyglet.resource.image(v)
#        i.anchor_x = i.width/2
        i.anchor_y = i.height
        IMAGES[k] = i

    global TILE_WIDTH, TILE_HEIGHT
    TILE_WIDTH = i.width
    TILE_HEIGHT = i.height

class Board(object):
    def __init__(self, width = 3, height = 3):
        self.width = width
        self.height = height

        # Screen center - half of board width
        board_width_px = width * TILE_WIDTH
        # Board height is half what we think because we stack tiles
        board_height_px = height * TILE_HEIGHT/2
        self.offset_x = ((SCREEN_X-board_width_px)/2.0)
        self.offset_y = ((SCREEN_Y-board_height_px)/2.0)
        self.offset_y = -SCREEN_Y/2 + board_height_px/2 + TILE_HEIGHT/4


        # Make a map with a stoneblock border and filled with grass
        game_map = []
        inner_width = width-2

        # for i in range(height):
            
        #     if i == 0 or i == height-1:
        #         for i in range(width):
        #             if i == 0 or i == width - 1:
        #         # On the boundaries
        #                 game_map.append(["Lava"] * width)
        #     else:
        #         row = ["Water"] + (["RainbowBlock"] * inner_width) + ["Water"]
        #         game_map.append(row)
        self.status = "Playing"



        def level1_map():
            for i in range(height):

                if i == 0 or i == height-1:
                    # On the boundaries
                    game_map.append(["Lava"] * width)
                else:
                    row = ["Lava"] + (["DarkDirt"] * inner_width) + ["Lava"]
                    game_map.append(row)
      
        def level2_map():
            for i in range(height):
                for j in range(width):
                    game_map.append(["RainbowBlock"]* width)

        def level3_map():
            for i in range(height):
                for j in range(width):
                    game_map.append(["Block"]* width)   
        
        level_maps=[level1_map(),level2_map(),level3_map()]

        # for i in Portal.interact:
        #     level_maps[i]

        self.base_board = game_map
        self.content_layer = []
        row = [ None ] * width
        for y in range(height):
            self.content_layer.append(list(row))

        self.message = pyglet.text.Label(text = "", width = 1000, x=10, y=SCREEN_Y-30, multiline=True)
        self.bg_sprites = []

        for y in range(height):
            for x in range(width):
                img_idx = game_map[y][x]
                image = IMAGES[img_idx]

                sprite = pyglet.sprite.Sprite(image)
                self.draw_bg(sprite, x, y)
                self.bg_sprites.append(sprite)

    def draw_msg(self, message):
        self.message.text = message
        pass

    def erase_msg(self):
        self.message.text = ""
        pass

    def draw_bg(self, sprite, x_pos, y_pos):
        # x_pos and y_pos in board coordinates
        x_px = x_pos * sprite.width
        y_px = SCREEN_Y - (y_pos * sprite.height / 2)
        sprite.set_position(
                x_px + self.offset_x,
                y_px + self.offset_y)

    def draw_active(self, sprite, x_pos, y_pos):
        # x_pos and y_pos in board coordinates
        # Active layer is 1/4 sprite width above bg layer
        x_px = x_pos * sprite.width
        y_px = SCREEN_Y - (y_pos * sprite.height /2) + (sprite.height/4)

        sprite.set_position(
                x_px + self.offset_x,
                y_px + self.offset_y)
        sprite.draw()

    def check_bounds(self, x, y):
        # if x == 0:
        if not (0 <= x < self.width):
            raise IndexError("%r is out of bounds of the board width: %d"%(x, self.width))
        if not (0 <= y < self.height):
            raise IndexError("%r is out of bounds of the board height: %d"%(y, self.width))

    def get_el(self, x, y):
        self.check_bounds(x, y)
        return self.content_layer[y][x]

    def set_el(self, x, y, el):
        self.check_bounds(x, y)
        el.x = x
        el.y = y
        self.content_layer[y][x] = el

    def del_el(self, x, y):
        self.check_bounds(x, y)
        self.content_layer[y][x] = None

    def register(self, el):
        image_file = IMAGES[el.IMAGE]
        el.board = self
        el.sprite = pyglet.sprite.Sprite(image_file)
        update_list.append(el)

    def draw(self):
        # Y is inverted
        # Draw the background
        for sprite in self.bg_sprites:
            sprite.draw()

        # Draw the label if it exists:
        if self.message:
            self.message.draw()

        # Draw the content layer
        for y in range(self.height):
            for x in range(self.width):
                el = self.content_layer[y][x]
                if el:
                    self.draw_active(el.sprite, x, y)


    def check_status(self, status):
        self.status = status
        return status





class Obstacle(GameElement):
    pass

def update(dt):
    for el in update_list:
        el.update(dt)

draw_list = []
update_list = []

@game_window.event
def on_draw():
    game_window.clear()
    for el in draw_list:
        el.draw()

def run():
    # Attempt to use custom board 
    global board
    global player
    setup_images()
    try:
        board = Board(game.GAME_WIDTH, game.GAME_HEIGHT)
    except (AttributeError) as e:
        board = Board()
        
    game.GAME_BOARD = board

    """
    try:
        board.register(player)
        update_list.append(player)
    except (AttributeError) as e:
        print "No player"
        player = None
    """

    # Set up an fps display
    try:
        if game.DEBUG == True:
            fps_display = pyglet.clock.ClockDisplay()
            draw_list.append(fps_display)
    except AttributeError:
        pass

    # Add the board and the fps display to the draw list
    draw_list.append(board)

    # Add the keyboard handler if it's ready
    key_handler = key.KeyStateHandler()
    game.KEYBOARD = key_handler
    game_window.push_handlers(key_handler)

    try:
        handler = game.keyboard_handler
        def handler_wrapper(dt):
            handler()
        pyglet.clock.schedule_interval(handler_wrapper, 1/10.0)
    except AttributeError:
        print "No keyboard handler"
        pass
        
    # Set up the update clock
    pyglet.clock.schedule_interval(update, 1/10.)
    game.initialize()
    pyglet.app.run()

class UpdateWrapper(object):
    def __init__(self, fn):
        self.fn = fn
    def update(self, dt):
        self.fn()

if __name__ == "__main__":
    run()
