import Weapon, Item, Creature, World

class MapTiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.left())
        
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.right())
        
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.up())
        
        if world.tile_exists(self.x, self.y +1):
            moves.append(actions.down())

        return moves
    def available_actions(self):
        """Returns all of the Available actions in this room 
        """
        moves = self.adjacent_moves()
        moves.append(action.ViewInventory())
        return moves

class StartRoom(MapTiles):
    def intro_text(self):
        """
        {}, are you awake now?
        We were attacked by a {} and now the town is on fire.
        While we put out the flames you've got to find that
        wretched creature and destroy him!

        """.formate(player, creature)

    def modify_player(self, player):
        #Room has no action on player
        pass

class HideItem(MapTile):
    def __init__(self, X, y, item):
        self.item = item
        super().__init__(x, y)

    def add_item(self, player):
        player.inventory.append(self.item)
    
    def modify_player(self, player):
        self.add_item(player)

class HideCreature(MapTile):
    def _init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("{} does {} damage.\nYou have {} HP remaining.".format(creature.name, self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            return [actions.Flee(tile=self), actions.Attack(creature=self.creature)]
        else:
            return self.adjacent_moves()
    
class HideRdDragon(HideCreature):
    def __init__(self, x, y):
        super().__init__(x, y, creatures.red_dragon())

    def intro_text(self):
        if self.creature.is_alive():
            return """
            You find yourself face to face with a Red Dragon. It's belly warm with fire
            he lets out a deafening screech.
        """
        else:
            return """
            The carcaus is still warm from your previous battle.
        """

class HideBlDragon(HideCreature):
    def __init__(self, x, y):
        super().__init__(x, y, Creature.blue_dragon())

    def intro_text(self):
        if self.creature.is_alive():
            return """
            You find yourself face to face with a Blue Dragon. She doesn't like to be disturbed.
            The dragon lunges at you.
        """
        else:
            return """
            The carcaus is still warm from your previous battle.
        """

class HideBlkDragon(HideCreature):
    def __init__(self, x, y):
        super().__init__(x, y, Creature.black_dragon())

    def intro_text(self):
        if self.creature.is_alive():
            return """
            You find yourself face to face with a Black Dragon.
            He lays in a valcano that seems to be the fuel for his rage.
        """
        else:
            return """
            The carcaus is still warm from your previous battle.
        """
class HidePotion(HideItem):
    def __init__(self, x, y):
        super().__init__(x, y, Item.Potion())

    def intro_text(self):
        return """
        You have found a potion, it will bring you back to life.
    """

class HideRdSword(HideItem):
    def __init__(self, x, y):
        super().__init__(x, y, Item.r_sword())

    def intro_text(self):
        return """
        You have found a sword that shines Red.
    """

class HideCSword(HideItem):
    def __init__(self, x, y):
        super().__init__(x, y, Item.c_sword())

    def intro_text(self):
        return """
        You have found a sword that shines blue.
    """

class HideDSword(HideItem):
    def __init__(self, x, y):
        super().__init__(x, y, Item.d_sword())

    def intro_text(self):
        return """
        You have found a sword that shines with a white light.
    """

class Victory(MapTiles):
    def intro_text(self):
        return """
        You have defeated the great dragon and saved our land!
    """

    def modify_player(self, player):
        player.victory = True