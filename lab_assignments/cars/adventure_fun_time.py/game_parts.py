import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description)

class Weapon(Item):
    def __init__(name, atk, loc):
        self.dmg = dmg
        super().__init(name, description, value)
    
    def __str__(self):
        return "{}\n=====\nDamage: {}".format(self.name, self.description, self.damage)
class r_sword(Weapon):
    def __init(self):
        super().__init__(
            name = 'Ruby Sword'
            description = "A sword that shines with a red glow."
            dmg = 10)

class c_sword(Weapon):
    def __init__(self):
        super().__init__(
            name = 'Cobalt Sword'
            description = "A sword that shines with a blue glow."
            dmg = 20)

class d_sword(Weapon):
    def __init__(self):
        super().__init__(
            name = 'Diamond Sword'
            description = "A sword that shines with a white glow."
            dmg = 30
        )
class Potion(Item):
    def __init__(health_plus):
        self.health_plus = health_plus
        super()__init__(
            name = 'Health Potion'
            description = 'Increase health points by 10 pts'
        )

class Creature:
    def __init__(self, name, hp, atk):
        self.name = name
        self.healthpoints = hp
        self.attack = atk

    def is_alive(self):
        return self.healthpoints > 0

class red_dragon(Creature):
    def __init__(self):
        super().__init__(
            name = "Red Dragon"
            hp = 100
            atk = 20
            )

class Blue_dragon(Creature):
    def __init__(self):
        super().__init__(
            name = "Blue Dragon"
            hp = 125
            atk = 30
            )

class Black_dragon(Creature):
    def __init__(self):
        super().__init__(
            name = "Black Dragon"
            hp = 150
            atk = 50
            )