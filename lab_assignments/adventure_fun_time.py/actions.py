import player


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return"{}: {}".format(self.hotkey, self.name)

class Up(Action):
    def __init__(self):
        super().__init__(method = Player.up, name = 'Move Up', hotkey = 'w')

class Down(Action):
    def __init__(self):
        super().__init__(method = Player.down, name = 'Move Down', hotkey = 's')

class Left(Action):
    def __init__(self):
        super().__init__(method = Player.left, name = 'Move Left', hotkey = 'a')

class Right(Action):
    def __init__(self):
        super().__init__(method = Player.move_right, name = 'Move Right', hotkey = 'd')

class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init(method = Player.print_inventory, name ='view inventory', hotkey='i')

class Attack(Action):
    def __init__(self, Creature):
            super().__init__(method = Player.attack, name ='Attack', hotkey='a', creature = Creature)
