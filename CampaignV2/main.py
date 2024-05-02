import os
import math
import random
from character import Hero, Enemy
from weapon import fists, short_bow, iron_sword
from health_bar import HealthBar

itemH = [fists, short_bow, iron_sword]
itemE = [fists, short_bow, iron_sword]



hero = Hero(name="Hero", health= 100, weapon = random.choice(itemH))
# hero.equip(random.choice(item))
enemy = Enemy(name="Enemy", health=100, weapon = random.choice(itemE))

gameOver = False
weaponEquiped = False

# while hero.health > 0:
#     if weaponEquiped == False:
#         hero.weapon = random.choice(item)
#         print(f"The hero picked from the weapon: {random.choice}")
#         weaponEquiped = True
#     else:
#         pass

while True:
    if hero.health and enemy.health > 0:
        os.system("cls")
        hero.attack(enemy)
        enemy.attack(hero)

        hero.health_bar.draw()
        enemy.health_bar.draw()

        input()

    elif enemy.health > hero.health:
        if gameOver == False:
            print("The game is over! The Enemy has WON!")
            gameOver = True
        else:
            pass
    elif enemy.health < hero.health:
        if gameOver == False:
            print("The game is over! The Hero has WON!")
            gameOver = True
        else:
            pass
    else:
        if gameOver == False:
            print("The game is over! The Enemy and Hero have LOST!")
            gameOver = True


# print(f"The hero picked from the weapon: {random.choice}")
