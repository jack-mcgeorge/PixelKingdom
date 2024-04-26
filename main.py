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
b_dragon = ['🐉', 'Dragon', 24, "The Dragon roars!", "The Dragon has been slain...", 25]
# Bosses (secret)
b_secret = ['🤓', 'Mr. Crockett', 30, "Mr. Crockett tells you to lock in!", "Mr. Crockett blows up with confetti!", 50]

boss_list = [b_villager, b_bear, b_owl, b_yeti, b_griffin, b_bking, b_davy, b_ogre, b_taurus, b_dragon]

def say(text):
    print(text)
    time.sleep(0.8)

biome_list = ['Pixel Kingdom', 'Grasslands', 'Woods', 'Snowy Woods', 'Mountains', 'Desert', 'Beach', 'Swamp', 'Volcano', 'Castle']
current_biome = ''

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

charms = ['Shield', ['💊', 0], ['💪', 0], ['🌀', 0], ['⚡', 0], ['🧨', 0], ['🐚', 0], ['💀', 0]]
b_charms = [['', ''], ['', '', ''], ['', '', ''], ['', '', '']]

if b_charms[0][0] == '':
    b_charms[0][0] = 'No Shield'
for i in range(3):
    if b_charms[i+1][1] == '':
        b_charms[i+1][1] = 'No Potion'

charm_etc_shld = ['Shield', False, 5]
# id, used t/f, hp
charm_pot_hlth = ['💊', 'Health Potion', 'Grasslands']
charm_pot_strg = ['💪', 'Strength Potion', 'Woods']
charm_pot_frze = ['🌀', 'Freeze Potion', 'Snowy Woods']
charm_pot_zapp = ['⚡', 'Zap Potion', 'Mountains']
charm_pot_dyna = ['🧨', 'Dynamite', 'Desert']
charm_pot_crab = ['🐚', 'Crab Conch', 'Beach']
charm_pot_posn = ['💀', 'Poison Potion', 'Swamp']

potion_title = [charm_etc_shld, charm_pot_hlth, charm_pot_strg, charm_pot_frze, charm_pot_zapp, charm_pot_dyna, charm_pot_crab, charm_pot_posn]

player_name = str(input("Adventurer's name: "))
player_hp = 10
player = ['🙂', player_name, player_hp]
satchel = 0
weapon = {'name': '', 'rarity': '', 'id': 0}

sword = {'name': 'Sword', 'rarity': 'Wood', 'id': 0, 'have': False}
axe = {'name': 'Axe', 'rarity': 'Wood', 'id': 0, 'have': False}
bow = {'name': 'Bow', 'rarity': 'Wood', 'id': 0, 'have': False}
x_bow = {'name': 'X-Bow', 'rarity': 'Wood', 'id': 0, 'have': False}

win_bandit = False
win_archer = False
win_barbar = False
win_pirate = False

win_bbandit = False
win_octopus = False

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
    weapon['name'] = new_weapon['name']
    weapon['rarity'] = new_weapon['rarity']
    weapon['id'] = new_weapon['id']
    say(' | ✋ | ' + player_name + ' equipped the ' + weapon['rarity'] + ' ' + weapon['name'] + ' (Damage: ' + str(find_dmg(new_weapon)) + ')')

def find_dmg(weapon):
    if weapon['name'] == 'Sword' or weapon['name'] == 'Bow':
        for i in range(5):
            if weapon['id'] == i:
                damage = (i+1)
                return damage
    if weapon['name'] == 'Axe' or weapon['name'] == 'X-Bow':
        for i in range(5):
            if weapon['id'] == i:
                damage = (i+2)
                return damage 
    return 0 #DEBUG

def check_charm(choice, hp):
    global player_hp

    if b_charms[choice-1][1] == 'Health Potion':
        say(' | 💊 | ' + player_name + 'has been fully healed!')
        player_hp = 15 + (biome_list.index(current_biome) * 5)
    if b_charms[choice-1][1] == 'Strength Potion':
        say(' | 💪 | Super-strong punch! Triple damage!')
        hp -= find_dmg(weapon)*3
    if b_charms[choice-1][1] == 'Freeze Potion':
        hp -= 1
        return 'f'
    if b_charms[choice-1][1] == 'Zap Potion':
        hp -= 3
        return 'z'
    if b_charms[choice-1][1] == 'Dynamite':
        say (' | 💥 | BOOM!')
        return 'b'
    if b_charms[choice-1][1] == 'Crab Conch':
        return 'c'
    if b_charms[choice-1][1] == 'Poison Potion':
        hp -= 2
        return 'p'

def counterattack(enemy):
    global player_hp
    global charm_etc_shld
    
    enemy_hp = enemy[2]

    if enemy_hp > 0: 
        dice_roll = random.randint(1, 10)

        say('\n | ' + enemy[0] + ' | ' + enemy[1] + ' attacks!')
        say(' | 🎲 | Rolling...')
        
        if charm_etc_shld[1] == True:
            charm_etc_shld = False
            return say(' | 🔄 | Hit deflected!')
            
        if dice_roll <= 3:
            return say(' | ❌ | Miss!')
        else:
            player_hp -= (round(enemy_hp/3))
            say(' | ⭕ | Hit!')
            return say(' | ❤️  | Health remaining: ' + str(player_hp))

def start_battle(enemy, weapon):
    global satchel

    global win_bandit
    global win_archer
    global win_barbar
    global win_pirate

    global win_bbandit
    global win_octopus

    enemy_hp = enemy[2]

    player_victory = False
    move = []
    
    say('\n ' + str(player[0]) + ' ⚔️  ' + str(enemy[0]))
    say(' ' + str(player[1]) + ' VS. ' + str(enemy[1]))
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
                
                if enemy_hp > 0:
                    counterattack(enemy)
                turn += 1
            elif dice_roll == 12:
                say(' | ⭐ | Critical hit!')
                enemy_hp -= (find_dmg(weapon)*2)
                say(' | ' + enemy[0] + ' | ' + enemy[3])

                if enemy_hp > 0:
                    counterattack(enemy)
                turn += 1
            else:
                say(' | ⭕ | Hit!')
                enemy_hp -= find_dmg(weapon)
                say(' | ' + enemy[0] + ' | ' + enemy[3])
                
                if enemy_hp > 0:
                    counterattack(enemy)
                turn += 1
            if enemy_hp <= 0:
                say('\n | ' + enemy[0] + ' | ' + enemy[4] + ' ' + enemy[1] + ' loses!')
                player_victory = True

        elif move[turn] == 'C' or move[turn] == 'c':
            if b_charms == [['No Shield', ''], ['', 'No Potion', ''], ['', 'No Potion', ''], ['', 'No Potion', '']]:
                time.sleep(0.5)
                say('\n | ❗ | ' + player_name + ' has no charms!')
                turn += 1
            else:
                time.sleep(0.5)
                say('\n | Here be thy charms!')
                say(' | 1 - ' + b_charms[0][0] + ' | 2 - ' + b_charms[1][1] + ' | 3 - ' + b_charms[2][1] + ' | 4 - ' + b_charms[3][1] + ' |\n')
                num = int(input(' | Choose a charm (1/2/3/4): '))
                if num == 1:
                    charm_etc_shld[1] = True
                    if enemy_hp > 0:
                        counterattack(enemy)
                else:
                    if b_charms[num - 1][1] == 0:
                        say(' | ❗ | No charms left in that slot!')
                    check_charm(num, enemy_hp)
                    b_charms[num - 1][1] -= 1
                    if check_charm(num, enemy_hp) == 'b':
                        player_victory = True

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
                b_charms[0] = charm_etc_shld
                return
            if enemy == e_archer and win_archer == False:
                say(' | 🏹 | ' + player_name + ' collected an Archer\'s bow!')
            if enemy == e_barbar and win_barbar == False:
                say(' | 🪓 | ' + player_name + ' collected a Barbarian\'s axe!')
            if enemy == e_pirate and win_pirate == False:
                say(' | ☠️ | ' + player_name + ' collected a Pirate\'s crossbow!')
            if enemy == e_bbandit and win_bbandit == False:
                win_bbandit = True
            if enemy == e_octopus and win_octopus == False:
                win_octopus = True
            return
        elif player_hp == 0:
            replay = str(input(' | 💔 | Great adventurer ' + player_name + ' has fallen. Play again? (Y/N): '))
            if replay == 'Y' or replay == 'y':
                main()
            elif replay == 'N' or replay == 'n':
                exit

def boss_battle(enemy, weapon):
    global satchel

    enemy_hp = enemy[2]

    player_victory = False
    move = []
    
    say('\n ' + str(player[0]) + ' ⚔️  ' + str(enemy[0]))
    say(' ' + str(player[1]) + ' VS. (BOSS)' + str(enemy[1]))
    time.sleep(1)

    turn = 0
    while True:
        move += str(input('\n | ATTACK | CHARMS | \n Enter move (A/C): '))

        if move[turn] == 'A' or move[turn] == 'a':
            say(' | ❗ | ' + player_name + ' attacks with their ' + weapon['name'] + '!')
            say(' | 🎲 | Rolling...')
            dice_roll = random.randint(1, 12)
            if dice_roll == 1:
                say(' | ❌ | Miss!')
                say(' | ' + enemy[0] + ' | ' + enemy[3])
                
                if enemy_hp > 0:
                    counterattack(enemy)
                turn += 1
            elif dice_roll == 12:
                say(' | ⭐ | Critical hit!')
                enemy_hp -= (find_dmg(weapon)*2)
                say(' | ' + enemy[0] + ' | ' + enemy[3])

                if enemy_hp > 0:
                    counterattack(enemy)
                turn += 1
            else:
                say(' | ⭕ | Hit!')
                enemy_hp -= find_dmg(weapon)
                say(' | ' + enemy[0] + ' | ' + enemy[3])
                
                if enemy_hp > 0:
                    counterattack(enemy)
                turn += 1
            if enemy_hp <= 0:
                say('\n | ' + enemy[0] + ' | ' + enemy[4] + ' ' + enemy[1] + ' loses!')
                player_victory = True

        elif move[turn] == 'C' or move[turn] == 'c':
            if b_charms == [['No Shield', ''], ['', 'No Potion', ''], ['', 'No Potion', ''], ['', 'No Potion', '']]:
                time.sleep(0.5)
                say('\n | ❗ | ' + player_name + ' has no charms!')
                turn += 1
            else:
                time.sleep(0.5)
                say('\n | Here be thy charms!')
                say(' | 1 - ' + b_charms[0][0] + ' | 2 - ' + b_charms[1][1] + ' | 3 - ' + b_charms[2][1] + ' | 4 - ' + b_charms[3][1] + ' |\n')
                num = int(input(' | Choose a charm (1/2/3/4): '))
                if num == 1:
                    charm_etc_shld[1] = True
                    if enemy_hp > 0:
                        counterattack(enemy)
                else:
                    if b_charms[num - 1][1] == 0:
                        say(' | ❗ | No charms left in that slot!')
                    check_charm(num, enemy_hp)
                    b_charms[num - 1][1] -= 1
                    if check_charm(num, enemy_hp) == 'b':
                        player_victory = True

        if player_victory == True:
            say(' | 👑 | ' + player_name + ' wins!')
            reward = random.randint(1, enemy[5])
            satchel += reward
            say(' | 💰 | ' + player_name + ' gained ' + str(reward) + ' gold!')
        elif player_hp == 0:
            replay = str(input(' | 💔 | Great adventurer ' + player_name + ' has fallen. Play again? (Y/N): '))
            if replay == 'Y' or replay == 'y':
                main()
            elif replay == 'N' or replay == 'n':
                exit

def loop(biome):
    global satchel
    global player_hp

    history = []
    choice = 0

    while True:
        say('\n | 🎒 | Open inventory (I)\n | ⚔️  | Fight an enemy (E)\n | 💰 | Search for loot (L)\n | 🔨 | Talk to the blacksmith (B)')
        if satchel >= 50+(25*biome_list.index(current_biome)):
            if current_biome == 'Castle':
                travel = str(input(' | 🐉 | Face the mighty dragon? (Y/N): '))
                if travel == 'Y' or travel == 'y':
                    start_battle(b_dragon, weapon)
            else:
                travel = str(input(' | 🗺️  | Travel to next biome? (Y/N): '))
                if travel == 'Y' or travel == 'y':
                    start_battle(boss_list[biome_list.index(current_biome)], weapon)
                    satchel -= 50+(25*biome_list.index(current_biome))
                    player_hp = (15+(biome_list.index(current_biome)*5))
                    say(' | ✨ | Max HP upgraded! Maximum health: ' + str(15+(biome_list.index(current_biome) * 5)))
                    break
        if (50-satchel) <= 0:
            say(' | 🗺️  | Gold required to reach next biome: 0')
        else:
           say(' | 🗺️  | Gold required to reach next biome: ' + str(50+(25*biome_list.index(current_biome))-satchel))
        history += str(input(' | ❓ | Make a choice (I/E/L/B): '))
        if history[choice] == 'I' or history[choice] == 'i':
            say('\n | 🎒 | INVENTORY\n | 🎒 | Weapons, Charms, Satchel')
            inventory_menu = str(input(' | ❓ | Pick which menu (W/C/S): '))
            if inventory_menu == 'W' or inventory_menu == 'w':
                say(' | Equipped weapon: ' + weapon['rarity'] + ' ' + weapon['name'])
                say(' | All weapons:\n | Sword (Rarity: ' + sword['rarity'] + ')\n | Axe (Rarity: ' + axe['rarity'] + ')\n | Bow (Rarity: ' + bow['rarity'] + ')\n | X-Bow (Rarity: ' + x_bow['rarity'] + ')')
                equip = str(input(' | ❓ | Equip weapons? Any other key to cancel. (S/A/B/X): '))
                if equip == 'S' or equip == 's':
                    if weapon['name'] == 'Sword':
                        say(' | ❗ | ' + player_name + ' already has a Sword equipped!')
                    elif sword['have'] == False:
                        say(' | ❗ | ' + player_name + ' doesn\'t have a Sword!')
                    else:
                        equip_weapon(sword)
                if equip == 'A' or equip == 'a':
                    if weapon['name'] == 'Axe':
                        say(' | ❗ | ' + player_name + ' already has an Axe equipped!')
                    elif axe['have'] == False:
                        say(' | ❗ | ' + player_name + ' doesn\'t have an Axe!')
                    else:
                        equip_weapon(axe)
                if equip == 'B' or equip == 'b':
                    if weapon['name'] == 'Bow':
                        say(' | ❗ | ' + player_name + ' already has a Bow equipped!')
                    elif axe['have'] == False:
                        say(' | ❗ | ' + player_name + ' doesn\'t have a Bow!')
                    else:
                        equip_weapon(bow)
                if equip == 'X' or equip == 'x':
                    if weapon['name'] == 'X-Bow':
                        say(' | ❗ | ' + player_name + ' already has a X-Bow equipped!')
                    elif axe['have'] == False:
                        say(' | ❗ | ' + player_name + ' doesn\'t have a X-Bow!')
                    else:
                        equip_weapon(bow)

            elif inventory_menu == 'C' or inventory_menu == 'c':
                say(' | Battle Charms: ' + b_charms[0][0] + ', ' + b_charms[1][1] + ', ' + b_charms[2][1] + ', ' + b_charms[3][1])
                say(' | All Charms:    ' + charms[1][0] + ' x' + str(charms[1][1]) + ', ' + charms[2][0] + ' x' + str(charms[2][1]) + ', ' + charms[3][0] + ' x' + str(charms[3][1]) + ', ' + charms[4][0] + ' x' + str(charms[4][1]) + ', ' + charms[5][0] + ' x' + str(charms[5][1]) + ', ' + charms[6][0] + ' x' + str(charms[6][1]) + ', ' + charms[7][0] + ' x' + str(charms[7][1]))
                swap = str(input(' | Type B to equip charms for battle. Any other key to cancel. '))
                if swap == 'B' or swap == 'b':
                    charm_x = int(input(' | Choose the charm to move (1/2/3/4/5/6/7): '))
                    charm_y = int(input(' | Choose the slot to move it to (1/2/3): '))
                    if charms[charm_x][1] - 1 <= 0:
                        say(' | ❗ | Not enough charms to move!\n')
                    else:
                        b_charms[charm_y] = potion_title[charm_x]
                        charms[charm_x][1] -= 1
            else:
                say(' | 💰 | You have ' + str(satchel) + ' gold in your satchel.')

        if history[choice] == 'E' or history[choice] == 'e':
            start_battle(biome[random.randint(0, len(biome))], weapon)

        if history[choice] == 'L' or history[choice] == 'l':
            if satchel - 5 < 0:
                say('\n | ❗ | Not enough gold to search!')
            else:
                say('\n | ❗ | -5 Gold!')
                satchel -= 5
                say('\n | 💰 | Searching for loot...')
                loot_roll = random.randint(1, (biome_list.index(current_biome) + 3))
                if loot_roll == 1:
                    gold = random.randint(1, player_hp)
                    say(' | 💰 | ' + player_name + ' found ' + str(gold) + ' gold!')
                    satchel += gold
                elif loot_roll == 2:
                    if current_biome == 'Volcano' or current_biome == 'Castle':
                        gold = (random.randint(1, player_hp))*2
                        say(' | 💰 | ' + player_name + ' found ' + str(gold) + ' gold!')
                        satchel += gold
                    else:
                        if (current_biome == 'Desert' and win_bbandit == True) or (current_biome == 'Beach' and win_octopus == True):
                            say(' | ❗ | ' + player_name + ' found a ' + potion_title[biome_list.index(current_biome)][1] + '!')
                            charms[potion_title[biome_list.index(current_biome)]][1] += 1
                        elif (current_biome == 'Desert' and win_bbandit == False) or (current_biome == 'Beach' and win_octopus == False):
                            say(' | 💢 | ' + player_name + ' found nothing!\n')
                        else:
                            say(' | ❗ | ' + player_name + ' found a ' + potion_title[biome_list.index(current_biome)][1] + '!')
                            charms[potion_title[biome_list.index(current_biome)]][1] += 1
                else:
                    say(' | 💢 | ' + player_name + ' found nothing!\n')

        if history[choice] == 'B' or history[choice] == 'b':
            choice += 1
            say(' | 🔨 | BLACKSMITH\n | 🔨 | Upgrade your equipped weapon?')
            upgrade = str(input(' | ❓ | Upgrade weapon? Any other key to cancel. (Y/N): '))
            if upgrade == 'Y' or upgrade == 'y':
                upgrade_weapon(weapon)
            elif upgrade == 'N' or upgrade == 'n':
                say(' | 🔨 | See you soon!')
        choice += 1

def hub():
    while True:
        say('\n | 🗺️  | ' + player_name + ' finds themself in a grassy plain. Do they...')
        loop(gr_enemies)
        
        welcome_biome(biome_list[2])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a dense forest. Do they...')
        loop(wo_enemies)

        welcome_biome(biome_list[3])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a snow-covered forest. Do they...')
        loop(sn_enemies)

        welcome_biome(biome_list[4])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a steep mountain range. Do they...')
        loop(mo_enemies)

        welcome_biome(biome_list[5])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a hot desert canyon. Do they...')
        loop(de_enemies)

        welcome_biome(biome_list[6])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a tropical beach. Do they...')
        loop(be_enemies)

        welcome_biome(biome_list[7])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a murky swamp. Do they...')
        loop(sw_enemies)

        welcome_biome(biome_list[8])
        say('\n | 🗺️  | ' + player_name + ' finds themself in a hot volcano! Do they...')
        loop(vo_enemies)

        welcome_biome(biome_list[9])
        say('\n | 🗺️  | ' + player_name + ' finds themself in the dragon\'s keep. Do they...')
        loop(ca_enemies)
        say(' | 🧔 | "Well done! You have slain the evil dragon."\n | 🧔 | "As a reward I leave you the key to the kingdom\'s treasure!"')
        say(' | 🗝️ | You approach the treasure chest.\n | 🗝️ | Upon opening it, you find a small box that has a code reader on it.')
        code = str(input(' | ❗ | Enter the code: '))
        if code == '937':
            boss_battle(b_secret)
            say(' | 💰 | After the battle, you are flooded with riches!')
            say(' | 🏅 | Thanks for playing Pixel Kingdom!')

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

if __name__ == "__main__":
    main()

# The code for the box is 937 ;)
