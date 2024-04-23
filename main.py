# Name:     Jack McGeorge
# Date:     19 Apr 2024
# Period:   1

# Purpose:  Medieval RPG-style game

import time
import random
from colorama import init, Fore, Style
init(autoreset=True)


# Grasslands enemies
e_bandit = ['🤑', 'Bandit', 5, "Bandit grunts.", "Bandit falls to his knees.", 8]
e_archer = ['🏹', 'Archer', 4, "Archer's aim falters.", "Archer falls to his knees.", 8]
e_badger = ['🦡', 'Badger', 3, "Badger lets out a chirp.", "Badger retreats to its burrow!", 2]
gr_enemies = [e_bandit, e_archer, e_badger]
# Woods enemies
e_hog = ['🐖', 'Hog', 4, "Hog oinks.", "Hog squeals and runs away.", 2]
e_wolf = ['🐺', 'Wolf', 5, "Wolf barks.", "Wolf retreats", 2]
e_moose = ['🦌', 'Moose', 6, "Moose stomps its hoof.", "Moose runs away", 4]
wo_enemies = [e_bandit, e_archer, e_badger, e_hog, e_wolf, e_moose]
# Snowy woods enemies
e_barbar = ['🪓', 'Barbarian', 7, "Barbarian growls...", "Barbarian falls to his knees.", 10]
e_fox = ['🦊', 'Fox', 4, "Fox barks.", "Fox retreats!", 3]
sn_enemies = [e_bandit, e_archer, e_wolf, e_moose, e_barbar, e_fox]
# Mountains enemies
e_mtlion = ['🦁', 'Mountain Lion', 8, "Mountain Lion roars!", "Mountain lion limps away.", 4]
e_ram = ['🐏', 'Ram', 7, "Ram shakes its head.", "Ram retreats up a cliff!", 3]
mo_enemies = [e_archer, e_wolf, e_barbar, e_mtlion, e_ram]
# Desert enemies
e_bbandit = ['🤕', 'Boom Bandit', 9, "Boom Bandit juggles dynamite.", "Boom Bandit fizzles out.", 11]
e_outlaw = ['🤠', 'Outlaw', 10, "Outlaw's aim falters.", "Outlaw falls to his knees.", 12]
e_snake = ['🐍', 'Snake', 6, "Snake hisses.", "Snake slithers away.", 4]
e_vulture = ['🦃', 'Vulture', 5, "Vulture crows.", "Vulture flies away!", 5]
de_enemies = [e_bandit, e_barbar, e_bbandit, e_outlaw, e_snake, e_vulture]
# Beach enemies
e_siren = ['🧜', 'Siren', 11, "Siren calls out!", "Siren swims into the deep...", 11]
e_crab = ['🦀', 'Crab', 6, "Crab snaps its claws.", "Crab walks away horizontally.", 3]
e_octopus = ['🐙', 'Octopus', 10, "Octopus wags a tentacle.", "Octopus crawls away", 5]
e_pirate = ['☠️', 'Pirate', 15, "Pirate stomps his peg leg.", "Pirate goes overboard!", 15]
be_enemies = [e_siren, e_crab, e_octopus, e_pirate]
# Swamp enemies
e_witch = ['🦹', 'Witch', 15, "Witch cackles!", "Witch disappears in a puff of smoke!", 14]
e_undead = ['🧟', 'Undead', 13, "Undead groans...", "Undead falls apart.", 6]
e_spider = ['🕷️', 'Spider', 8, "Spider spins a web.", "Spider skitters away...", 2]
e_gator = ['🐊', 'Gator', 9, "Gator snaps its jaw!", "Gator retreats into the swamp!", 3]
sw_enemies = [e_hog, e_witch, e_undead, e_spider, e_gator]
# Volcano enemies
e_warlock = ['🧙', 'Warlock', 16, "Warlock casts a spell", "Warlock disappears in a zap of lightning!", 13]
e_warhog = ['🐗', 'War Hog', 10, "War Hog snorts!", "War Hog squeals and retreats!", 5]
e_golem = ['🗿', 'Golem', 14, "Golem grumbles.", "Golem breaks apart!", 6]
e_bdragon = ['🦎', 'Baby Dragon', 18, "Baby dragon spits fire!", "Baby dragon flies away!", 16]
vo_enemies = [e_undead, e_warlock, e_warhog, e_golem, e_bdragon]
# Castle enemies
e_knight = ['💂', 'Knight', 19, "Knight polishes his sword.", "Knight marches away.", 17]
ca_enemies = [e_undead, e_warlock, e_golem, e_bdragon, e_knight]

# Bosses (everywhere)
b_villager = ['🧔', 'Villager', 3, "Villager cracks a mediocre joke.", "Villager pretends to die.", 3]
b_bear = ['🐻', 'Bear', 15, "Bear growls...", "Bear retreats into a cave!", 5]
b_owl = ['🦉', 'Owl', 15, "Owl hoots!", "Owl flies away!", 7]
b_yeti = ['🥶', 'Yeti', 17 ,"Yeti growls...", "Yeti retreats into the blizzard!", 9]
b_griffin = ['🦅', 'Griffin', 17, "Griffin squawks!" ,"Griffin flies away!", 11]
b_bking = ['👺', 'Bandit King', 19, "Bandit King chuckles.", "Bandit King explodes!", 13]
b_davy = ['🏴‍☠️', 'Davy Jones', 20, "Davy Jones points a hook!", "Davy Jones sinks...", 15]
b_ogre = ['🧝', 'Ogre', 20, "Ogre roars!", "Ogre goes back to his swamp...", 17]
b_taurus = ['👿', 'Minotaur', 23, "Minotaur growls...", "Minotaur retreats!", 23]
b_dragon = ['🐉', 'Dragon', 24, "The Dragon roars!", "The Dragon has been slayed...", 25]
# Bosses (secret)
b_secret = ['🤓', 'Mr. Crockett', 30, "Mr. Crockett tells you to lock in!", "Mr. Crockett blows up with confetti!", 50]


def say(text):
    print(text)
    time.sleep(0.8)

biome_list = ['Pixel Kingdom', 'Grasslands', 'Woods', 'Snowy Woods', 'Mountains', 'Desert', 'Beach', 'Swamp', 'Volcano', 'Castle']
current_biome = ''

# Spaghetti code below. Watch your step
def welcome_biome(biome):
    global current_biome

    time.sleep(1)
    print('\n')
    if biome == biome_list[0]:
        print('⣿ Welcome to PIXEL KINGDOM ⣿')
        current_biome = biome_list[0]

    if biome == biome_list[1]:
        print(Fore.GREEN + '⣿ Now entering GRASSLANDS ⣿')
        current_biome = biome_list[1]

    if biome == biome_list[2]:
        print(Style.DIM + Fore.LIGHTGREEN_EX + '⣿ Now entering WOODS ⣿')
        current_biome = biome_list[2]

    if biome == biome_list[3]:
        print(Fore.CYAN + '⣿ Now entering SNOWY WOODS ⣿')
        current_biome = biome_list[3]

    if biome == biome_list[4]:
        print(Style.DIM + Fore.CYAN + '⣿ Now entering MOUNTAINS ⣿')
        current_biome = biome_list[4]

    if biome == biome_list[5]:
        print(Fore.YELLOW + '⣿ Now entering DESERT ⣿')
        current_biome = biome_list[5]

    if biome == biome_list[6]:
        print(Fore.BLUE + '⣿ Now entering BEACH ⣿')
        current_biome = biome_list[6]

    if biome == biome_list[7]:
        print(Style.DIM + Fore.GREEN + '⣿ Now entering SWAMP ⣿')
        current_biome = biome_list[7]

    if biome == biome_list[8]:
        print(Fore.LIGHTRED_EX + '⣿ Now entering VOLCANO ⣿')
        current_biome = biome_list[8]

    if biome == biome_list[9]:
        print(Fore.RED + '⣿ Now entering CASTLE ⣿')
        current_biome = biome_list[9]

    time.sleep(1)


charms = ['0', '0', '0', '0', '0', '0', '0', '0']


charm_etc_shld = ['Shield', False, 0]
# id, used t/f, hp
charm_pot_hlth = ['💊', 'Health', 'Grasslands']
charm_pot_zapp = ['⚡', 'Zap', 'Mountains']
charm_pot_posn = ['💀', 'Poison', 'Swamp']
charm_pot_strg = ['💪', 'Strength', 'Woods']
charm_pot_frze = ['🌀', 'Freeze', 'Snowy Woods']
charm_pot_dyna = ['🧨', 'Dynamite', 'Desert']
charm_pot_crab = ['🐚', 'Crab Conch', 'Beach']

potion_title = [charm_etc_shld, charm_pot_hlth, charm_pot_strg, charm_pot_frze, charm_pot_zapp, charm_pot_dyna, charm_pot_crab, charm_pot_posn]


player_name = str(input("Adventurer's name: "))
player_hp = 10
player = ['🙂', player_name, player_hp]
satchel = 0
weapon = {'name': '', 'rarity': '', 'id': 0}

sword = {'name': 'Sword', 'rarity': 'Wood', 'id': 0}
axe = {'name': 'Axe', 'rarity': 'Wood', 'id': 0}
bow = {'name': 'Bow', 'rarity': 'Wood', 'id': 0}
x_bow = {'name': 'X-Bow', 'rarity': 'Wood', 'id': 0}

inventory = {'primary': weapon, 'secondary': [sword, axe, bow, x_bow]}

win_bandit = False
win_archer = False
win_barbar = False


def find_rarity(id):
    rarity = ''
    if id == 0:
        rarity = 'Wood'
        return rarity
    if id == 1:
        rarity = 'Stone'
        return rarity
    if id == 2:
        rarity = 'Bronze'
        return rarity
    if id == 3:
        rarity = 'Iron'
        return rarity
    if id == 4:
        rarity = 'Gold'
        return rarity
    if id == 5:
        rarity = 'Damascus'
        return rarity

def upgrade_weapon(weapon):
    global satchel

    for i in range(5):
        if weapon['id'] == i:
            if satchel - ((i+1**2)) <= 0:
                return say('\n | ❗ | Not enough gold to upgrade!')
            if weapon['rarity'] == 'Damascus':
                return say('\n | ❗ | Already fully upgraded!')
            satchel -= ((i+1)**2)
            weapon['id'] += 1
            say(' | ✅ | Weapon upgraded. New rarity: ' + find_rarity(weapon['id']))

     
def equip_weapon(new_weapon):
    weapon = new_weapon
    say(' | ✋ | ' + player_name + ' equipped the ' + weapon['rarity'] + ' ' + weapon['name'] + ' (Damage: ' + str(find_dmg(new_weapon)) + ')')


def find_dmg(weapon):
    if 'Sword' in weapon['name'] or 'Bow' in weapon['name']:
        for i in range(5):
            if weapon['id'] == i:
                damage = (i+1)
                return damage
    if 'Axe' in weapon['name'] or 'X-Bow' in weapon['name']:
        for i in range(5):
            if weapon['id'] == i:
                damage = (i+2)
                return damage


def counterattack(enemy):
    global player_hp
    enemy_hp = enemy[2]

    if enemy_hp > 0: 
        dice_roll = random.randint(1, 20)

        say('\n | ' + enemy[0] + ' | ' + enemy[1] + ' attacks!')
        say(' | 🎲 | Rolling...')
        
        if charm_etc_shld[1] == True:
            charm_etc_shld[2] -= 1
            if charm_etc_shld > 0:
                return say(' | 🔄 | Hit deflected!')
            else:
                return say(' | 🔄 | Shield broken!')

        if dice_roll <= 5:
            return say(' | ❌ | Miss!')
        elif dice_roll == 20:
            player_hp -= (round(enemy_hp/3)+2)
            return say(' | ⭐ | Critical hit!')
        else:
            player_hp -= (round(enemy_hp/3))
            return say(' | ⭕ | Hit!')


def start_battle(enemy, weapon):
    global satchel

    global win_bandit
    global win_archer
    global win_barbar

    enemy_hp = enemy[2]

    player_victory = False
    move = []
    
    say('\n ' + str(player[0]) + ' ⚔️  ' + str(enemy[0]))
    say(' ' + str(player[1]) + ' VS ' + str(enemy[1]))
    time.sleep(1)

    turn = 0
    while True:
        move += str(input('\n | ATTACK | CHARMS | FLEE | \n Enter move (A/C/F): '))


        if move[turn] == 'A' or move[turn] == 'a':
            say(' | ❗ | ' + player_name + ' attacks with their ' + weapon['name'] + '!')
            say(' | 🎲 | Rolling...')
            dice_roll = random.randint(1, 12)
            if dice_roll == 1:
                say(' | ❌ | Miss!')
                say(' | ' + enemy[0] + ' | ' + enemy[3])
                
                counterattack(enemy)
                turn += 1
            elif dice_roll == 12:
                say(' | ⭐ | Critical hit!')
                enemy_hp -= (find_dmg(weapon)*2)
                say(' | ' + enemy[0] + ' | ' + enemy[3])

                counterattack(enemy)
                say(' | ❤️  | Health remaining: ' + str(player_hp))
                turn += 1
            else:
                say(' | ⭕ | Hit!')
                enemy_hp -= find_dmg(weapon)
                say(' | ' + enemy[0] + ' | ' + enemy[3])
                
                counterattack(enemy)
                say(' | ❤️  | Health remaining: ' + str(player_hp))
                turn += 1
            if enemy_hp <= 0:
                say('\n | ' + enemy[0] + ' | ' + enemy[4] + ' ' + enemy[1] + ' loses!')
                player_victory = True
        elif move[turn] == 'C' or move[turn] == 'c':
            if charms == ['0', '0', '0', '0', '0', '0', '0', '0']:
                time.sleep(0.5)
                say('\n | ❗ | ' + player_name + ' has no charms!')
                if charms[0] == '0':
                    charms[0] = 'No Shield'
                for n in range(7):
                    if charms[n+1] == '0':
                        charms[n+1] = 'No Potion'
                turn += 1
            else:
                time.sleep(0.5)
                say('\n | Here be thy charms!')
                say(' | 1 - ' + charms[0] + ' | 2 - ' + charms[1] + ' | 3 - ' + charms[2] + ' | 4 - ' + charms[3] + ' |\n')
                choice = int(input(' | Choose a charm (1/2/3/4):'))
                if choice == 1:
                    charm_etc_shld[1] = True
                    counterattack(enemy)
                
                
        elif move[turn] == 'F' or move[turn] == 'f':
            flee_confirm = str(input(' | ❗ | Flee from battle? (Y/N): '))
            if flee_confirm == 'Y' or flee_confirm == 'y':
                satchel -= 5
                return
            elif flee_confirm == 'N' or flee_confirm == 'n':
                continue
        if player_victory == True:
            say(' | 👑 | ' + player_name + ' wins!')
            reward = random.randint(1, enemy[5])
            satchel += reward
            say(' | 💰 | ' + player_name + ' gained ' + str(reward) + ' gold!')
            if enemy == e_bandit and win_bandit == False:
                say(' | 🤑 | ' + player_name + ' collected a Bandit\'s shield!')
                charms[0] = charm_etc_shld
                return
            if enemy == e_archer and win_archer == False:
                say(' | 🏹 | ' + player_name + ' collected an Archer\'s crossbow!')
            if enemy == e_barbar and win_barbar == False:
                say(' | 🪓 | ' + player_name + ' collected a Barbarian\'s axe!')
            return
        elif player_hp == 0:
            replay = str(input(' | 💔 | Great adventurer ' + player_name + ' has fallen. Play again? (Y/N): '))
            if replay == 'Y' or replay == 'y':
                main()
            elif replay == 'N' or replay == 'n':
                exit


def loop(alpha, bravo, charlie):
    global satchel
    
    delta = biome_list.index(current_biome)

    say(' | 🎒 | Open inventory (I)\n | ⚔️ | Fight an enemy (E)\n | 💰 | Search for loot (L)\n | 🔨 | Talk to the blacksmith (B)')
    alpha += str(input(' | ❓ | Make a choice (I/E/L/B): '))
    if alpha[bravo] == 'I' or alpha[bravo] == 'i':
        say(' | 🎒 | INVENTORY')
    if alpha[bravo] == 'E' or alpha[bravo] == 'e':
        start_battle(charlie[random.randint(0, (len(charlie))-1)], weapon)
    if alpha[bravo] == 'L' or alpha[bravo] == 'l':
        say(' | 💰 | Searching for loot...')
        loot_roll = random.randint(1, (delta + 3))
        if loot_roll == 1:
            gold = random.randint(1, player_hp)
            say(' | 💰 | ' + player_name + ' found ' + str(gold) + ' gold!')
            satchel += gold
        elif loot_roll == 2:
            if current_biome == 'Beach':
                say(' | 🐚 | ' + player_name + ' found a Crab Conch!')
            elif current_biome == 'Desert':
                say(' | 🧨 | ' + player_name + ' found Dynamite!')
            elif current_biome == 'Volcano' or current_biome == 'Castle':
                gold = (random.randint(1, player_hp))*2
                say(' | 💰 | ' + player_name + ' found ' + str(gold) + ' gold!')
                satchel += gold
            else:
                say(' | 🧪 | ' + player_name + ' found a ' + potion_title[delta][1] + ' Potion!')
                charms[delta] = potion_title[delta]
                print(charms) #DEBUG
        else:
            say(' | 💢 | ' + player_name + ' Found nothing!')
    if alpha[bravo] == 'B' or alpha[bravo] == 'b':
        say(' | 🔨 |')


def hub():
    history = []
    choice = 0

    while True:
        if current_biome == 'Grasslands':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a grassy plain. Do they...')
            loop(history, choice, gr_enemies)
            choice += 1
        if current_biome == 'Woods':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a dense forest. Do they...')
            loop(history, choice, wo_enemies)
            choice += 1
        if current_biome == 'Snowy Woods':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a snow-covered forest. Do they...')
            loop(history, choice, sn_enemies)
            choice += 1
        if current_biome == 'Mountains':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a steep mountain range. Do they...')
            loop(history, choice, mo_enemies)
            choice += 1
        if current_biome == 'Desert':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a hot desert canyon. Do they...')
            loop(history, choice, de_enemies)
            choice += 1
        if current_biome == 'Beach':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a tropical beach. Do they...')
            loop(history, choice, be_enemies)
            choice += 1
        if current_biome == 'Swamp':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a murky swamp. Do they...')
            loop(history, choice, sw_enemies)
            choice += 1
        if current_biome == 'Volcano':
            say('\n | 🗺️  | ' + player_name + ' finds themself in a hot volcano! Do they...')
            loop(history, choice, vo_enemies)
            choice += 1
        if current_biome == 'Castle':
            say('\n | 🗺️  | ' + player_name + ' finds themself in the dragon\'s keep. Do they...')
            loop(history, choice, ca_enemies)
            choice += 1


def tutorial():
    global player_hp

    say('\n | 🧔 | "Welcome to the tutorial, ' + player_name + '!"')
    say(' | 🧔 | "Have you played Pixel Kingdom before?"')
    tut_exit = str(input(' | ❓ | Enter response (Y/N): '))
    if tut_exit == 'Y' or tut_exit == 'y':
        player_hp = 15
        say(' | 🧔 | "Well, you look a little worse for wear...take this!"')
        say(' | ✨ | Max HP upgraded! Maximum health: 15')
        say(' | 🧔 | "Excellent! Here\'s a sword for your troubles."')
        say(' | ✨ | ' + player_name + ' got WOOD SWORD')
        equip_weapon(sword)
    elif tut_exit == 'N' or tut_exit == 'n':
        say(' | 🧔 | "Excellent! Let\'s begin!"')
        say(' | 🧔 | "I\'ll teach you to fight!"')
        say(' | 🧔 | "Take this!"')
        say(' | ✨ | ' + player_name + ' got WOOD SWORD')
        equip_weapon(sword)
        start_battle(b_villager, weapon)
        player_hp = 15
        say(' | 🧔 | "Wow! Well done! You\'ll make a fine adventurer yet."')
        time.sleep(0.45)
        say(' | 🧔 | "You look a little rough after that battle though. Take this!"')
        say(' | ✨ | ' + player_name + ' has been healed! Current health: 10')
        time.sleep(0.45)
        say(' | 🧔 | "And for good luck, this too..!"')
        say(' | ✨ | Max HP upgraded! Maximum health: 15')
        time.sleep(0.45)
        say(' | 🧔 | "Good luck on your journey, traveler!"')


def main():
    welcome_biome('Pixel Kingdom')
    tutorial()
    welcome_biome('Grasslands')
    hub()


main()

# I learned how to use Colorama on https://pypi.org/project/colorama/