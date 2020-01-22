# Hero Class
class Character:

    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):

        enemy.health -= self.power

    def print_status(self):

        return "You have {} health and {} power". format(self.health, self.power)

    def alive(self):
        while self.health > 0:
            return True


class Hero(Character):

    def __init__(self, health, power):
        self.health = health
        self.power = power

    # def attack(self, enemy):

    #     enemy.health -= self.power

    # def print_status(self):

    #     return "You have {} health and {} power". format(self.health, self.power)

    # def alive(self):

        # Goblin Class


class Goblin(Character):

    def __init__(self, health, power):
        self.health = health
        self.power = power

        # FIX
        #self.alive = True

    # def attack(self, enemy):

    #     enemy.health -= self.power

    # def print_status(self):

    #     return "You have {} health and {} power". format(self.health, self.power)


class Zombie(Character):

    def __init__(self, health, power):
        self.health = health
        self.power = power


hero = Hero(10, 5)
goblin = Goblin(6, 2)


# Zombie
# 1zombie = Zombie(-1, -1)


def main():
    hero_health = 10
    hero_power = 30
    goblin_health = 6
    goblin_power = 2

    # while goblin.health > 0 and hero.health > 0:
    while goblin.alive() and hero.alive():

        # print(zombie.print_status())

        #print("You have %d health and %d power." % (hero.health, hero.power))
        print(hero.print_status())
        # print("The goblin has %d health and %d power." %
        #       (goblin.health, goblin.power))
        print(goblin.print_status())
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":

            # hero.attack(zombie)

            # Hero attacks goblin
            hero.attack(goblin)
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            #hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")


main()
