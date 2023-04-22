import random
class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
class Boss:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
heroes = [
    Hero('Warrior', 100, 20),
    Hero('Berserk', 80, 25),
    Hero('Magic', 90, 18),
    Hero('Thor', 85, 22),
    Hero('Golem', 120, 16)
]
boss = Boss('Big Boss', 200, 25)
def print_stats(heroes, boss):
    print('Heroes:')
    for hero in heroes:
        print('{} - Health: {}, Damage: {}'.format(hero.name, hero.health, hero.damage))
    print('Boss:')
    print('{} - Health: {}, Damage: {}'.format(boss.name, boss.health, boss.damage))
def warrior_attack(hero, boss):
    damage = hero.damage * random.uniform(1.5, 2.5)
    boss.health -= damage
    print('{} deals {} damage to {} with a critical hit!'.format(hero.name, damage, boss.name))
def berserk_attack(hero, boss):
    damage = hero.damage
    block = random.uniform(0.1, 0.3)
    blocked_damage = boss.damage * block
    boss.health -= blocked_damage
    hero.damage += blocked_damage
    print('{} blocks {} damage and deals {} damage to {}!'.format(hero.name, blocked_damage, blocked_damage, boss.name))
def magic_attack(hero, boss):
    hero.damage += random.randint(5, 10)
    print('{} increases their damage to {}!'.format(hero.name, hero.damage))
def thor_attack(hero, boss):
    if random.uniform(0, 1) < 0.2:
        boss.health -= hero.damage
        print('{} stuns {} for 1 round!'.format(hero.name, boss.name))
    else:
        boss.health -= hero.damage
        print('{} deals {} damage to {}!'.format(hero.name, hero.damage, boss.name))
def golem_protect(hero, boss):
    damage = boss.damage // 5
    hero.health -= damage
    print('{} takes {} damage for {}!'.format(hero.name, damage, boss.name))
def boss_attack(heroes, boss):
    hero = random.choice(heroes)
    hero.health -= boss.damage
    print('{} deals {} damage to {}!'.format(boss.name, boss.damage, hero.name))
print_stats(heroes, boss)
while boss.health > 0 and any(hero.health > 0 for hero in heroes):
    for hero in heroes:
        if hero.health > 0:
            if hero.name == 'Warrior':
                warrior_attack(hero, boss)
            elif hero.name == 'Berserk':
                berserk_attack(hero, boss)
            elif hero.name == 'Magic':
                magic_attack(hero, boss)
            elif hero.name == 'Thor':
                thor_attack(hero, boss)
            elif hero.name == 'Golem':
                golem_protect(hero, boss)
        if boss.health <= 0 or all(hero.health <= 0 for hero in heroes):
            break
    boss_attack(heroes, boss)
    print_stats(heroes, boss)
if boss.health <= 0:
    print('Congratulations! You have defeated {}!'.format(boss.name))
else:
    print('Game over! {} has defeated all the heroes!'.format(boss.name))
