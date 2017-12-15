import game_parts

class Player():
    def __init__(self):
        self.inventory = [Item.r_sword(), Item.Potion()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y = dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_up(self):
        self.move(dx=0, dy=-1)

    def move_down(self):
        self.move(dx=0, dy=-1)

    def move_left(self):
        self.move(dx=1, dy=0)

    def move_right(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, Item.Weapon):
                if i.damage > max_dmg:
                    best_weapon = i
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage  
        if not enemy.is_alive():
            print("you Killed {}!".format(enemy.name))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

        else:
            print("{}HP is {}.".format(enemy.name, enemy.hp))
