#level system, mana potion, save and load
import random
import ast

class Item:
    def __init__(self, space):
        self.space = space

class HealthPotion(Item):
    def __init__(self, regenerated_health):
        Item.__init__(self, 1)
        self.regenerated_health = regenerated_health

class Character:
    def __init__(self, hp, ad, name, xp):
        self.hp =  hp
        self.ad =  ad
        self.name =  name
        self.xp =  xp

    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()

    def is_dead(self):
        return self.hp <= 0

    def die(self):
        print (self.name + " died.")

    def get_hit_by_firestorm(self):
        rand1 = random.randint(0, 1)
        rand2 = random.randint(1, 7)
        self.hp = self.hp - 250
        if rand1 == 0:
            print (str(self.name) + " was burned!")
            for i in range(1, rand2):
                self.hp = self.hp - 10
        else:
            pass
        if self.hp <= 0:
            self.die()

    def get_hit_by_thunderstorm(self):
        self.hp = self.hp - 250
        if self.hp <= 0:
            self.die()

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin", 10)

class Ork(Character):
    def __init__(self):
        Character.__init__(self, 300, 30, "Ork", 30)

class Giant(Character):
    def __init__(self):
        Character.__init__(self, 500, 50, "Giant", 50)


class Player(Character):
    items = []
    required_xp = 100
    level = 0
    def __init__(self, name, hp, ad, regenerated_health, mana, all_xp):
        Character.__init__(self, hp, ad, name, 0)
        self.max_hp = hp
        self.regenerated_health = regenerated_health
        self.mana = mana
        self.max_mana = mana
        self.all_xp = all_xp

    def die(self):
        exit ("Wasted. Try again.")

    def rest(self):
        self.hp = self.max_hp
        self.mana = self.max_mana

    def use_healthpotion(self):
        try:
            if self.items[0] == "HealthPotion":
                if int(self.hp <= 400):
                    self.hp = self.hp + self.regenerated_health
                    print ("You now have " + str(self.hp)  + " hp left.")
                    self.items.remove("HealthPotion")
                else:
                    if self.hp == self.max_hp:
                        print("You are already at full health.")
                    else:
                        self.hp = self.max_hp
                        self.items.remove("HealthPotion")
                        print ("You now have " + str(self.max_hp) + " left.")
        except IndexError:
            print ("You don't have a HealthPotion in your inventory.")

    def show_xp_and_level(self):
        print ("You have accumulated " + str(self.all_xp) + " xp.")
        print ("You are currently at level " + str(self.level) + " and need to accumulate " +
        str(self.required_xp - self.all_xp) + " xp more to level up.")

    def level_up(self):
        if self.all_xp >= self.required_xp:
            self.required_xp = self.all_xp + self.required_xp*1.5
            self.required_xp = round(self.required_xp, 2)
            self.level = self.level + 1
            print ("You have reached level " + str(self.level) + "!")
        else:
            pass

    def save(self):
        data1 = self.hp
        data2 = self.mana
        data3 = self.required_xp
        data4 = self.all_xp
        data5 = self.level
        data6 = self.items
        data7 = self.name
        data = [data1, data2, data3, data4, data5, data6, data7]
        data = str(data)
        saveFile = open("saveFile.txt", "w")
        saveFile.write(data)
        saveFile.close()
        print("You saved your data.")
    
    def load(self):
        newData_file = open("savefile.txt", "r")
        newData = newData_file.read()
        newData_file.close()
        newData = ast.literal_eval(newData)
        self.hp = newData[0]
        self.mana = newData[1]
        self.required_xp = newData[2]
        self.all_xp = newData[3]
        self.level = newData [4]
        self.items = newData[5]
        self.name = newData [6]

class Field:
    def __init__(self, enemies):
        self.enemies = enemies

    def print_state(self):
        print ("You have " + str(p.hp) + " hp and " + str(p.mana) + " mana.")
        print ("Your inventory: " + str(p.items))
        print ("You look around and see ")
        for i in self.enemies:
            print (i.name)

    @staticmethod
    def gen_random(self):
        rand = random.randint(0, 3)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([Ork()])
        if rand == 2:
            return Field([Goblin(), Ork()])
        if rand == 3:
            return Field([Giant()])
        if rand == 4:
            return Field([Goblin(), Giant()])

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random(self))
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x] [self.y].enemies

    def forward (self):
        if self.x == len(self.state) - 1:
            print ("You see huge mountains, which you can't pass.")
        else:
            self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
            print ("You see cliffs, but you can't jump safely.")
        else:
            self.x = self.x - 1

    def right (self):
        if self.y == len(self.state[self.x]) - 1:
            print ("You see huge mountains, which you can't pass.")
        else:
            self.y = self.y + 1

    def left (self):
        if self.y == 0:
            print ("You see cliffs, but you can't jump safely.")
        else:
            self.y = self.y - 1

def forward (m, p):
    map.forward()

def right(m, p):
    map.right()

def left (m, p):
    map.left()

def backwards(m, p):
    map.backwards()

def save():
    pass

def load():
    pass

def quit_game(p, m):
    print ("Suicide is a BADASS, that's why you decide to commit suicide and leave this world. " )
    exit (0)

def print_help(p, m):
        print(Commands.keys())

def pickup(p, m):
    pass

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        attack(p, m)
        if enemies[0].is_dead():
            add_healthpotion_to_inventory(p, m)
            p.all_xp = p.all_xp + enemies[0].xp
            p.level_up()
            enemies.remove(enemies[0])
        for i in enemies:
            block(p, m)
        try:
            for i in enemies:
                print (str(enemies[0].name) + " has " + str(enemies[0].hp) + " hp left.")
        except IndexError:
            pass
        print ("You have " + str(p.hp) + " hp " + str(p.mana) + " mana left.")

def rest(p, m):
    p.rest()

def use_healthpotion(p, m):
    p.use_healthpotion()

def run_away(p, m):
    enemies = m.get_enemies()
    for i in enemies:
        enemies.remove(i)

def add_healthpotion_to_inventory(p, m):
    rand = random.randint(0, 1)
    if rand == 0:
        print ("It dropped nothing. ")
    elif rand == 1:
            if len(p.items) < 11:
                p.items.append("HealthPotion")
                print ("It dropped a HealthPotion.")
            if len(p.items) == 10:
                print ("Your inventory is full.")

def attack(p, m):
    enemies = m.get_enemies()
    answer = input ("With what do you want to attack? (auto_attack, firestorm, thunderstorm) ")
    if answer == "auto_attack":
        enemies[0].get_hit(p.ad)
    elif answer == "firestorm":
        if p.mana >= 10:
            enemies[0].get_hit_by_firestorm()
            p.mana = p.mana - 10
        else:
            print("You don't have enough mana. ")
    elif answer == "thunderstorm":
        if p.mana >= 10:
            enemies[0].get_hit_by_thunderstorm()
            p.mana = p.mana - 10
        else:
            print ("You don't have enough mana. ")
    else:
        print ("That's not a correct input.")
        pass

def block(p, m):
    rand = random.randint(0, 1)
    enemies = m.get_enemies()
    answer = input ("Do you want to block? ")
    if answer == "yes":
        if rand == 0:
            pass
        else:
            for i in enemies:
                print ("You are Nobb and fail to block. ")
                p.get_hit(i.ad)
    elif answer == "no":
        for i in enemies:
            p.get_hit(i.ad)
    else:
        print ("That's not a correct input.")
        for i in enemies:
            p.get_hit(i.ad)

def show_xp_and_level(p, m):
    p.show_xp_and_level()

def save(p, m):
    p.save()

def load(p, m):
    p.load()
Commands = {
    "help": print_help,
    "quit": quit_game,
    "pickup": pickup,
    "forward": forward,
    "right": right,
    "left": left,
    "backwards": backwards,
    "fight": fight,
    "rest": rest,
    "use_healthpotion": use_healthpotion,
    "run_away": run_away,
    "show_xp_and_level": show_xp_and_level,
    "save": save,
    "load": load,
}

if __name__=="__main__":
    name = input ("Enter your name: ")
    p = Player (name, 500, 100, 100, 100, 0)
    map = Map(5, 5)
    print ("(type help to list the commands available)\n")
    while True:
        command = input (">").lower().split(" ")
        if command [0] in Commands:
            Commands[command[0]](p, map)
        else:
            print ("You run around in circles and don't know what to do.")
        map.print_state()
