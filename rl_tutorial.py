# COMPLETE ROGUELIKE TUTORIAL WITH PYTHON TCOD
# --------------------------------------------
# Date: April 17th, 2019
# Completed everything before the chapter on Saving/Loading

# NOTE: The only important area where it differs from the source code
#       used in the tutorial on Rogue Basin is that I used "tilemap" 
#       instead of "map" to refer to the tile map. This is because
#       map is a reserved word in Python and I figured it'd be smart to
#       pro-actively use something else just in case. 
#
#       Other than that, the only differences are places where I cleaned
#       up the syntax a little. I added some parentheses to the calls to 
#       the message() function so that the string parameter is visibly
#       enclosed but that doesn't seem to make any functional difference.
#       I also used slightly different colors for the text but I figure 
#       we'll be changing all of that around anyway.
#
#       BUGS: For some reason the enemies don't attack the player as often
#       as they should, and the scrolls which automatically pick out a 
#       certain enemy within a defined radius don't work most of the time.
#       I'm not sure why. I followed the tutorial very closely and feel
#       I have a decent grasp on the logic. I can only assume I made some
#       bizarre error somewhere that I haven't detected yet. I tried to
#       refer to the example source code where possible but for most of the
#       chapters in this tutorial there don't seem to be complete examples
#       available. It is possible that there's just a small typo somewhere 
#       causing the problem.
#  ~ sgibber2018

import libtcodpy as tcod
import math
import textwrap

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
MAP_WIDTH = 80
MAP_HEIGHT = 43
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30
MAX_ROOM_MONSTERS = 3
MAX_ROOM_ITEMS = 2
FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10
BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
MSG_X = BAR_WIDTH + 2
MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1
INVENTORY_WIDTH = 50
HEAL_AMOUNT = 4
LIGHTNING_DAMAGE = 20
LIGHTNING_RANGE = 5
CONFUSE_NUM_TURNS = 10
CONFUSE_RANGE = 8
FIREBALL_RADIUS = 3
FIREBALL_DAMAGE = 12


class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
    
        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight

        self.explored = False

class RoomRect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) // 2
        center_y = (self.y1 + self.y2) // 2
        return (center_x, center_y)

    def intersect(self, other):
        # returns true if room intersects with another room
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


class Object:
    # Generic game object as defined in the libtcod rogue basin tutorial
    def __init__(self, x, y, char, name, color, blocks=False,
            fighter=None, ai=None, item=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.fighter = fighter
        if self.fighter:
            self.fighter.owner = self
        self.ai = ai
        if self.ai:
            self.ai.owner = self
        self.item = item
        if self.item:
            self.item.owner = self

    def move(self, dx, dy):
        if not is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def draw(self):
        if tcod.map_is_in_fov(fov_map, self.x, self.y):
            tcod.console_set_default_foreground(con, self.color)
            tcod.console_put_char(con, self.x, self.y, self.char, 
                tcod.BKGND_NONE)
    
    def clear(self):
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

    def move_towards(self, target_x, target_y):
        # move towards the player
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy) 

    def distance_to(self, other):
        # distance between two objects
        dx = other.x - self.x
        dy = other.x - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def distance(self, x, y):
        # returns distance to a tile
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def send_to_back(self):
        # send object to the "back" of the object list
        global objects
        objects.remove(self)
        objects.insert(0, self)

class Fighter:
    #combat-related properties and methods
    def __init__(self, hp, defense, power, death_function=None):
        self.hp = hp
        self.max_hp = hp
        self.defense = defense
        self.power = power
        self.death_function=death_function

    def heal(self, amount):
        # heal the owner of the component by a given amount
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def take_damage(self, damage):
        # apply damage
        if damage > 0:
            self.hp -= damage
        if self.hp <= 0:
            function = self.death_function
            if function is not None:
                function(self.owner)

    def attack(self, target):
        # attack!
        damage = self.power - target.fighter.defense
        
        if damage > 0:
            message((self.owner.name.capitalize() + " attacks " + 
                    target.name + " for " + str(damage) + " hit points."),
                    tcod.red)
            target.fighter.take_damage(damage)
        else:
            message((self.owner.name.capitalize() + " attacks " + 
                    target.name + " but it has no effect!"), tcod.red)

class BasicMonster:
    # AI for a basic monster
    def take_turn(self):
        # sgibber2018 Note: I have commented out the growling
        #                   because it obscures other messages
        # message(("The " + self.owner.name + " growls!"), tcod.yellow)
        monster = self.owner
        if tcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(player) >= 2:
                monster.move_towards(player.x, player.y)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player)

class ConfusedMonster:
    # AI for a confused monster
    def __init__(self, old_ai, num_turns=CONFUSE_NUM_TURNS):
        self.old_ai = old_ai
        self.num_turns = num_turns

    def take_turn(self):
        if self.num_turns > 0:
            # move in a random direction
            self.owner.move(tcod.random_get_int(0, -1, 1), 
                    tcod.random_get_int(0, -1, 1))
            self.num_turns -= 1
        else:
            self.owner.ai = self.old_ai
            message(("The " + self.owner.name + " is no longer confused!"),
                    tcod.red)
        

class Item:
    # an item that can be picked up and used
    def __init__(self, use_function=None):
        self.use_function = use_function

    def pick_up(self):
        # add to inventory and remove from map
        if len(inventory) >= 26:
            message(("Your inventory is full " + self.owner.name + 
                    "!"), tcod.yellow)
        else:
            inventory.append(self.owner)
            objects.remove(self.owner)
            message(("You picked up a " + self.owner.name + "!"),
                    tcod.yellow)

    def use(self):
        # use the item according to it's use_function, if any
        if self.use_function is None:
            message("The " + self.owner.name + " cannot be used!")
        else:
            if self.use_function() != "cancelled":
                inventory.remove(self.owner)

    def drop(self):
        # add to the map and remove from the inventory
        objects.append(self.owner)
        inventory.remove(self.owner)
        self.owner.x = player.x
        self.owner.y = player.y
        message(("You dropped a " + self.owner.name + "."),
                tcod.yellow)

def cast_heal():
    # heal the player 
    if player.fighter.hp == player.fighter.max_hp:
        message("At max health!", tcod.yellow)
        return "cancelled"

    message("Your wounds start to feel better!",
            tcod.light_violet)
    player.fighter.heal(HEAL_AMOUNT)

def cast_lightning():
    # casts a lightning bolt spell
    monster = closest_monster(LIGHTNING_RANGE)
    if monster is None: 
        # if no enemy in range
        message("No enemy is close enough to strike!", tcod.red)
        return "cancelled"

    # zappity
    message(("A lightning bolt strikes the " + monster.name + " for " +
            str(LIGHTNING_DAMAGE) + " damage!"), tcod.light_blue)
    monster.fighter.take_damage(LIGHTNING_DAMAGE)

def cast_confuse():
    # find closest enemy in range and confuse it
    message("Left click an enemy to confuse it! Right click to cancel",
            tcod.light_cyan)
    monster = target_monster(CONFUSE_RANGE)
    if monster is None:
        return "cancelled"
    
    old_ai = monster.ai
    monster.ai = ConfusedMonster(old_ai)
    monster.ai.owner = monster
    message(("The eyes of the " + monster.name + " look confused!"),
            tcod.light_green)

def cast_fireball():
    # ask player for a target tile to shoot a fireball
    global objects
    message("Left click a tile to cast Fireball, or right click to cancel", 
            tcod.light_cyan)
    (x, y) = target_tile()
    if x is None:
        return "cancelled"

    for obj in objects:
        if obj.distance(x, y) <= FIREBALL_RADIUS and obj.fighter:
            message(("The " + obj.name + " gets burned for " + str(FIREBALL_DAMAGE) + " damage!"), tcod.orange)
            obj.fighter.take_damage(FIREBALL_DAMAGE)

def closest_monster(max_range):
    # finds the closest monster within a maximum range
    # and within the player's field of view
    global objects

    closest_enemy = None
    closest_dist = max_range + 1

    for object in objects:
        if object.fighter and not object == player and tcod.map_is_in_fov(fov_map, object.x, object.y):
            dist = player.distance_to(object)
            if dist < closest_dist:
                closest_enemy = object
                closest_dist = dist

    return closest_enemy

def player_death(player):
    # game over
    global game_state
    message(("You died!"), tcod.green)
    game_state = "dead"
    player.char = '%'
    player.color = tcod.dark_red

def monster_death(monster):
    # turn monster into a corpse
    message((monster.name.capitalize() + " died!"), tcod.green)
    monster.char = '%'
    monster.color = tcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = "remains of " + monster.name
    monster.send_to_back()

def create_room(room):
    # carve out a RoomRect on the tilemap
    global tilemap
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            tilemap[x][y].blocked = False
            tilemap[x][y].block_sight = False

def create_h_tunnel(x1, x2, y):
    # carve a horizontal tunnel on the tilemap
    global tilemap
    for x in range(min(x1, x2), max(x1, x2) + 1):
        tilemap[x][y].blocked = False
        tilemap[x][y].block_sight = False

def create_v_tunnel(y1, y2, x):
    # carve a vertical tunnel on the tilemap
    global tilemap
    for y in range(min(y1, y2), max(y1, y2) + 1):
        tilemap[x][y].blocked = False
        tilemap[x][y].block_sight = False

def place_objects(room):
    # place monsters and objects within a room
    global objects
    num_monsters = tcod.random_get_int(0, 0, MAX_ROOM_MONSTERS)
    
    for i in range(num_monsters):
        # spot monsters
        x = tcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = tcod.random_get_int(0, room.y1 + 1, room.y2 - 1)

        if not is_blocked(x, y):
            if tcod.random_get_int(0, 0, 100) < 80:
                # 80% chance of Orc
                fighter_component = Fighter(hp=10, defense=0, power=3,
                    death_function=monster_death)
                ai_component = BasicMonster()
                monster = Object(x, y, 'o', "orc", tcod.desaturated_green,
                    blocks=True, fighter=fighter_component, 
                    ai=ai_component)
            else:
                # 20% chance of troll
                fighter_component = Fighter(hp=16, defense=1, power=4,
                    death_function=monster_death)
                ai_component = BasicMonster()
                monster = Object(x, y, 'T', "troll", tcod.darker_green,
                    blocks=True, fighter=fighter_component, 
                    ai=ai_component)

            objects.append(monster)

    num_items = tcod.random_get_int(0, 0, MAX_ROOM_ITEMS)
    for i in range(num_items):
        # place items
        x = tcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = tcod.random_get_int(0, room.y1 + 1, room.y2 - 1)

        if not is_blocked(x, y):
            dice = tcod.random_get_int(0, 0, 100)
            if dice < 70:
                # 70% chance of plopping a healing potion
                item_component = Item(use_function=cast_heal)
                item = Object(x, y, '!', "healing potion", tcod.violet, 
                        item=item_component)
            elif dice < 70 + 10:
                # 10% chance of lightning bolt scroll
                item_component = Item(use_function=cast_lightning)
                item = Object(x, y, '?', "scroll of lightning bolt", 
                        tcod.violet, item=item_component)
            elif dice < 70 + 10 + 10:
                # 10% chance for firefall scroll
                item_component = Item(use_function=cast_fireball)
                item = Object(x, y, '?', "scroll of fireball",
                        tcod.violet, item=item_component)
            else:
                # 10% chance fo confuse scroll
                item_component = Item(use_function=cast_confuse)
                item = Object(x, y, '?', "scroll of confusion",
                        tcod.violet, item=item_component)

            # append new item to objects list and send it to the "back"    
            objects.append(item)
            item.send_to_back()  # make items appear below other objects

def make_map():
    # Generate the tilemap itself
    global tilemap
    tilemap = [[Tile(True) for y in range(MAP_HEIGHT)]
            for x in range(MAP_WIDTH)]

    rooms = []
    num_rooms = 0
    
    for r in range(MAX_ROOMS):
        # random width and height
        w = tcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = tcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        # random posiiton without going out of bounds
        x = tcod.random_get_int(0, 0, MAP_WIDTH - w - 1)
        y = tcod.random_get_int(0, 0, MAP_HEIGHT - h - 1)

        new_room = RoomRect(x, y, w, h)
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break
        if not failed:
            create_room(new_room)
            (new_x, new_y) = new_room.center()
            if num_rooms == 0:
                player.x = new_x
                player.y = new_y
            else:
                # all rooms after the first room
                (prev_x, prev_y) = rooms[num_rooms - 1].center()
                if tcod.random_get_int(0, 0, 1) == 1:
                    # first tunnel horizontally, then tunnel vertically
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    # first vertical, then horizontal
                    create_v_tunnel(prev_y, new_y, prev_x)
                    create_h_tunnel(prev_x, new_x, new_y)

            # append room to list
            rooms.append(new_room)
            num_rooms += 1
            
            # place objects
            place_objects(new_room)


def is_blocked(x, y):
    global objects
    if tilemap[x][y].blocked:
        return True
    
    for object in objects:
        if object.blocks and object.x == x and object.y == y:
            return True

    return False

def player_move_or_attack(dx, dy):
    global fov_compute

    y = player.y + dy
    x = player.x + dx
    
    target = None
    for object in objects:
        if object.fighter and object.x == x and object.y == y:
            target = object
            break

    if target is not None:
        player.fighter.attack(target)
    else:
        player.move(dx, dy)
        fov_recompute = True

def get_names_under_mouse():
    global mouse, objects

    (x, y) = (mouse.cx, mouse.cy)
    
    names = [obj.name for obj in objects if obj.x == x and
            obj.y == y and tcod.map_is_in_fov(fov_map, obj.x, obj.y)]

    names = ', '.join(names)
    return names.capitalize()

def target_tile(max_range=None):
    # return the position of a tile that is left-clicked within the
    # player's FOV (or optionally in a range) or None if right-clicked.
    global key, mouse
    while True:
        # render screen, erasing inventory menu and showing the name of
        # any objects under the mouse
        tcod.console_flush()
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS|tcod.EVENT_MOUSE,key,mouse)
        render_all()

        (x, y) = (mouse.cx, mouse.cy)

        if (mouse.lbutton_pressed and tcod.map_is_in_fov(fov_map, x, y) and
                (max_range is None or player.distance(x, y) <= max_range)):
            return (x, y)

        if mouse.rbutton_pressed or key.vk == tcod.KEY_ESCAPE:
            return (None, None)

def target_monster(max_range=None):
    # returns a clicked monster inside FOV up to a range,
    # or returns None if right-clicked
    global objects
    while True:
        (x, y) = target_tile(max_range)
        if x is None:
            return None

        # return first clicked monster
        for obj in objects:
            if obj.x == x and obj.y == y and obj.fighter and obj != player:
                return obj

def handle_keys():
    # Handles keypresses!
    global player_x, player_y, fov_map, game_statei, key
    
    # fullscreen key
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    # quit key
    elif key.vk == tcod.KEY_ESCAPE:
        return "exit"

    # movement keys:
    if game_state == "playing":
        # up key
        if key.vk == tcod.KEY_UP:
                player_move_or_attack(0, -1)
                fov_recomputer = True
        # down key
        elif key.vk == tcod.KEY_DOWN:
                player_move_or_attack(0, 1)
                fov_recomputer = True
        # left key
        elif key.vk == tcod.KEY_LEFT:
                player_move_or_attack(-1, 0)
                fov_recomputer = True
        # right key
        elif key.vk == tcod.KEY_RIGHT:
                player_move_or_attack(1, 0)
                fov_recomputer = True
        else:
            # test for other keys
            key_char = chr(key.c)

            if key_char == 'g':
                # pick up an item
                for object in objects:
                    if object.x == player.x and object.y == player.y and object.item:
                        object.item.pick_up()
                        break
            if key_char == 'i':
                # show the inventory
                chosen_item = inventory_menu("Press the listed to use an item or any other to cancel. \n")
                if chosen_item is not None:
                    chosen_item.use()
            if key_char == 'd':
                # show the inventory, select item, drop item
                chosen_item = inventory_menu("Press letter of item you want to drop, or any other button to cancel.\n")
                if chosen_item is not None:
                    chosen_item.drop()

            return "didnt-take-turn"

        if game_state == "playing" and player_action != "didnt-take-turn":
            for object in objects:
                if object != player:
                    # sgibber2018 Note: I have commented out the growling
                    #                   because it obscures other messages
                    # message(("The " + object.name + " growls!"), 
                    #         tcod.yellow)
                    pass
        

def render_all():
    # Render all of the game objects and the tilemap
    global fov_map, game_msgs


    if fov_recompute:
        # recomputer fov if needed
        fov_recomputer = False
        tcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS,
            FOV_LIGHT_WALLS, FOV_ALGO)
    
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            # render map tile by tile
            wall = tilemap[x][y].block_sight
            visible = tcod.map_is_in_fov(fov_map, x, y) 
            if not visible:
                if tilemap[x][y].explored: 
                    if wall:
                        tcod.console_set_char_background(con, x, y, 
                            color_dark_wall, tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(con, x, y,
                            color_dark_ground, tcod.BKGND_SET)
            else:
                if wall:
                    tcod.console_set_char_background(con, x, y, 
                        color_light_wall, tcod.BKGND_SET)
                else:
                    tcod.console_set_char_background(con, x, y, 
                        color_light_ground, tcod.BKGND_SET)
                tilemap[x][y].explored = True

    for object in objects:
        object.draw()
    player.draw()
 
    # blit console
    tcod.console_blit(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)

    # panel
    tcod.console_set_default_background(panel, tcod.black)
    tcod.console_clear(panel)
    
    y = 1
    for (line, color) in game_msgs:
        tcod.console_set_default_foreground(panel, color)
        tcod.console_print_ex(panel, MSG_X, y, tcod.BKGND_NONE,
                tcod.LEFT, line)
        y += 1
    # health bar
    render_bar(1, 1, BAR_WIDTH, "HP", player.fighter.hp, 
            player.fighter.max_hp, tcod.light_red, tcod.darker_red)

    # whatever is under the mouse:
    tcod.console_set_default_foreground(panel, tcod.light_gray)
    tcod.console_print_ex(panel, 1, 0, tcod.BKGND_NONE, tcod.LEFT,
            get_names_under_mouse())

    # blit panel to root console
    tcod.console_blit(panel, 0, 0, SCREEN_WIDTH, PANEL_HEIGHT, 
            0, 0, PANEL_Y)

def render_bar(x, y, total_width, name, value, maximum, bar_color,
        back_color):
    # render a bar representing a stat
    bar_width = int(float(value) / maximum + total_width)
    # render background
    tcod.console_set_default_background(panel, back_color)
    tcod.console_rect(panel, x, y, total_width, 1, False, 
            tcod.BKGND_SCREEN)
    # render bar on top of background
    tcod.console_set_default_background(panel, bar_color)
    if bar_width > 0:
        tcod.console_rect(panel, x, y, bar_width, 1, False,
                tcod.BKGND_SCREEN)
    # text
    tcod.console_set_default_foreground(panel, tcod.white)
    tcod.console_print_ex(panel, x + total_width // 2, y, 
            tcod.BKGND_NONE, tcod.CENTER,
            name + ": " + str(value) + "/" + str(maximum))

def message(new_msg, color=tcod.white):
    # adds a message to the game_msgs list
    global game_msgs
    
    new_msg_lines = textwrap.wrap(new_msg, MSG_WIDTH)

    for line in new_msg_lines:
        if len(game_msgs) == MSG_HEIGHT:
            del game_msgs[0]

        game_msgs.append((line, color))

def menu(header, options, width):

    if len(options) > 26:
        raise ValueError("can't have more than 26 options")
    
    header_height = tcod.console_get_height_rect(con, 0, 0, width,
            SCREEN_HEIGHT, header)
    height = len(options) + header_height
    
    # create new off-screen console for menu
    window = tcod.console_new(width, height)

    # print the header with auto-wrap
    tcod.console_set_default_foreground(window, tcod.white)
    tcod.console_print_rect_ex(window, 0, 0, width, height, 
            tcod.BKGND_NONE, tcod.LEFT, header)

    # print the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = "(" + chr(letter_index) + ") " + option_text
        tcod.console_print_ex(window, 0, y, tcod.BKGND_NONE,
                tcod.LEFT, text)
        y += 1
        letter_index += 1

    # blit offscreen console to the screen
    x = SCREEN_WIDTH // 2 - width // 2
    y = SCREEN_HEIGHT // 2 - height // 2
    tcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)

    tcod.console_flush()
    key = tcod.console_wait_for_keypress(True)

    index = key.c - ord('a')
    if index >= 0 and index < len(options):
        return index

    return None

def inventory_menu(header):
    global inventory
    # show an inventory menu with each item listed
    if len(inventory) == 0:
        options = ["Inventory is empty..."]
    else:
        options = [item.name for item in inventory]
    index = menu(header, options, INVENTORY_WIDTH)

    if index is None or len(inventory) == 0:
        return None

    return inventory[index].item

font_path = "arial10x10.png"
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)

window_title = "Python3 libtcod tutorial"
fullscreen = False
tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, 
        fullscreen)

tcod.sys_set_fps(LIMIT_FPS)

# COLORS
color_dark_wall = tcod.Color(0, 0, 100)
color_dark_ground = tcod.Color(50, 50, 150)
color_light_wall = tcod.Color(130, 110, 50)
color_light_ground = tcod.Color(200, 180, 50)

# init the game objects
fighter_component = Fighter(hp=30, defense=2, power=5,
    death_function=player_death)
player = Object(0, 0, '@', "player", tcod.white, blocks=True,
    fighter=fighter_component)
objects = [player]

inventory = []

# init the map
make_map()

# game messages 
game_msgs = []

fov_map = tcod.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        tcod.map_set_properties(fov_map, x, y, not 
            tilemap[x][y].block_sight, not
            tilemap[x][y].blocked)

fov_recompute = True
game_state = 'playing'
player_action = None

con = tcod.console_new(MAP_WIDTH, MAP_HEIGHT)
panel = tcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)

# welcome message
message("Welcome Stranger! Prepare to perish!", tcod.red)

mouse = tcod.Mouse()
key = tcod.Key()

# main loop
while not tcod.console_is_window_closed():
    # main loop
    tcod.console_set_default_foreground(0, tcod.white)

    tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS|tcod.EVENT_MOUSE,key,mouse)

    # draw
    render_all()

    # refresh
    tcod.console_flush()
    
    # clear
    for object in objects:
        object.clear()

    player_action = handle_keys()
    if player_action == "exit":
        break

    if game_state == "playing" and player_action != "didnt-take-turn":
        for object in objects:
            if object.ai:
                object.ai.take_turn()

