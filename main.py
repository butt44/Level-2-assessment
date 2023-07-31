import random
import os

#Making some lists/dictionaries
possible_class_choices = []
player_classes_real = {
    "Acrobat": [1, []],
    "Assassin": [1, []],
    "Barbarian": [2, []],
    "Bard": [1, []],
    "Cleric": [3, []],
    "Druid": [3, []],
    "Fighter": [5, []],
    "Illusionist": [4, []],
    "Knight": [5, []],
    "Magic-user": [4, []],
    "Paladin": [6, []],
    "Ranger": [5, []],
    "Thief": [1, []]
}

#Making the thing that reads the text file and lets me draw blocks of text from it later. 
read_file = open('text_file.txt', 'r')

comp_list = []
comp = read_file.readline()
full_comp = ''
while len(comp) != 0:
    if comp[:-1] != '*':
        full_comp = full_comp + comp
    else:
        comp_list.append(full_comp)
        full_comp = ''
    comp = read_file.readline()

stre, dex, con, inte, wis, cha = (0, 0, 0, 0, 0, 0)
stre1, con1, dex1, inte1, wis1, cha1 = ('Strength', 'Constitution','Dexterity', 'Intelligence', 'Wisdom','Charisma')

possible_choices = [['1', '2'],
                    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]


#Calculating stats using hard mode
def calc_stat_hard(hard_stat, stat):
    for i in range(3):
        hard_stat += random.randint(1, 6)
    print(stat + ': ' + str(hard_stat))
    return hard_stat


#Calculating stats using easy mode:
def calc_stat_easy(easy_stat, stat):
    for i in range(4):
        d1, d2, d3, d4 = (
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
        )
        stat_list = [d1, d2, d3, d4]
        stat_list.sort()
        stat_list.pop(0)
        easy_stat = (stat_list[0] + stat_list[1] + stat_list[2])
    print(stat + ': ' + str(easy_stat))
    return easy_stat


def hard_mode():
    global stre, con, dex, inte, wis, cha
    stre = calc_stat_hard(stre, stre1)
    dex = calc_stat_hard(dex, dex1)
    con = calc_stat_hard(con, con1)
    inte = calc_stat_hard(inte, inte1)
    wis = calc_stat_hard(wis, wis1)
    cha = calc_stat_hard(cha, cha1)


def easy_mode():
    global stre, con, dex, inte, wis, cha
    stre = calc_stat_easy(stre, stre1)
    dex = calc_stat_easy(dex, dex1)
    con = calc_stat_easy(con, con1)
    inte = calc_stat_easy(inte, inte1)
    wis = calc_stat_easy(wis, wis1)
    cha = calc_stat_easy(cha, cha1)


#Disclaimer:
os.system('clear')
check_guide = '0'
#Asking the user if they want to disable guides during the character creation process:
while check_guide not in possible_choices[0]:
    check_guide = input('Do you want to turn off the guide?\n\n1.Yes\n\n2.No\n\n> ')
    if check_guide == '1':
        guide = bool(False)
    elif check_guide == '2':
        guide = bool(True)
    else:
        input("Error, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')

os.system('clear')

#Asking the user if they want to use dark mode:
check_dark_mode = '0'
while check_dark_mode not in possible_choices[0]:
    check_dark_mode = input('Do you want to use dark mode?\n\n1.Yes\n\n2.No\n\n> ')
    if check_dark_mode in possible_choices[0]:
        if check_dark_mode == '1':
            dark_mode = bool(True)
            break
        if check_dark_mode == '2':
            dark_mode = bool(False)
            break
    else:
        input("Error, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')

os.system('clear')

if guide == True:
    print(
        'Stat generation blah blah blah... describe to the user what each option does and what they mean'
    )

#Asking the user for either easy mode or hard mode with stat generation
easy_or_hard = '0'
while easy_or_hard not in possible_choices[0]:
    easy_or_hard = input('Do you want your character\'s stat the easy way or the hard way?\n\n1. Easy\n\n2. Hard\n\n> ')
    if easy_or_hard in possible_choices[0]:
        if easy_or_hard == '1':
            print('\nHere are your stats:\n\n')
            easy_mode()
            break
        if easy_or_hard == '2':
            print('\nHere are your stats:\n\n')
            hard_mode()
            break
    else:
        input("Error, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')
            
input('\nPress [Enter] to continue')
os.system('clear')

#Organized list of stats for future calculations:
stat_list_before_add = [stre, inte, wis, dex, con, cha]
stat_list_after_add = [0, 0, 0, 0, 0, 0]

#Asking the user if they want to use level cap for class by race (an optional rule):
check_level_preferences = '0'
while check_level_preferences not in possible_choices[0]:
    check_level_preferences = input('Do you want to use level cap preferences?\n\n1.Yes\n\n2.No\n\n> ')
    if check_level_preferences == '1':
        level_preferences = bool(True)
    elif check_level_preferences == '2':
        level_preferences = bool(False)
    else:
        input("Error, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')
os.system('clear')

#Dictionary with all possible race choices
if level_preferences == True:
    guys = {
        "1": [
            "drow", [0, 0, 0, 1, -1, 0],
            [10, 10, 0, 0, 11, 0, 7, 0, 9, 9, 0, 9, 11], comp_list[0]
        ],
        "2": [
            "human", [0, 0, 0, 0, 0, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14], comp_list[1]
        ],
        "3": [
            "elf", [0, 0, 0, 1, -1, 0],
            [10, 10, 0, 0, 7, 8, 7, 0, 11, 11, 0, 11, 10], comp_list[3]
        ],
        "4": [
            "dwarf", [0, 0, 0, 0, 1, -1],
            [0, 9, 0, 0, 8, 0, 10, 0, 0, 0, 0, 0, 9], comp_list[4]
        ],
        "5": [
            "half elf", [0, 0, 0, 0, 0, 0],
            [12, 11, 0, 12, 5, 12, 8, 0, 12, 8, 12, 8, 12], comp_list[5]
        ],
        "6": [
            "half orc", [1, 0, 0, 0, 1, -2],
            [8, 8, 0, 0, 4, 0, 10, 0, 0, 0, 0, 0, 8], comp_list[6]
        ],
        "7": [
            "duergar", [0, 0, 0, 0, 1, -1],
            [0, 9, 0, 0, 8, 0, 10, 0, 0, 0, 0, 0, 9], comp_list[7]
        ],
        "8": [
            "gnome", [0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 7, 0, 6, 7, 0, 0, 0, 0, 8], comp_list[8]
        ],
        "9": [
            "svirfneblin", [0, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 7, 0, 6, 7, 0, 0, 0, 0, 8], comp_list[9]
        ],
        "10": [
            "halfling", [-1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 8], comp_list[10]
        ]
    }
if level_preferences == False:
    guys = {
        "1": [
            "drow", [0, 0, 0, 1, -1, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "2": [
            "human", [0, 0, 0, 0, 1, 1],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14], comp_list[2]
        ],
        "3": [
            "elf", [0, 0, 0, 1, -1, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "4": [
            "dwarf", [0, 0, 0, 0, 1, -1],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "5": [
            "half elf", [0, 0, 0, 0, 0, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "6": [
            "half orc", [1, 0, 0, 0, 1, -2],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "7": [
            "duergar", [0, 0, 0, 0, 1, -1],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "8": [
            "gnome", [0, 0, 0, 0, 0, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "9": [
            "svirfneblin", [0, 0, 0, 0, 0, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ],
        "10": [
            "halfling", [-1, 0, 0, 1, 0, 0],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
        ]
    }

#Dictionary with all possible class choices:

player_class = {}

#list with all classes:

classes = [
    'Acrobat', 'Assassin', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
    'Illusionist', 'Knight', 'Magic-user', 'Paladin', 'Ranger', 'Thief'
]

#asking user if they want to calculate their characters level by exp or level:
check_level_exp = '0'
while check_level_exp not in possible_choices[0]:
    check_level_exp = input('Do you want to calculate your characters level from exp or level?\n\n1.Exp\n\n2.Level\n\n> ')
    if check_level_exp == '1':
        level_exp = bool(True)
    elif check_level_exp == '2':
        level_exp = bool(False)
    else:
        input("eError, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')

os.system('clear')

#Asking the user what race they want to be:
check_race = '0'
while check_race not in possible_choices[1]:
    check_race = input('What race do you want your character to be?\n\n1.Drow\n\n2.Human\n\n3.Elf\n\n4.Dwarf\n\n5.Half-elf\n\n6.Half-orc\n\n7.Deurgar\n\n8.Gnome\n\n9.Svirfneblin\n\n10.Halfling\n\n> ')
    if check_race in possible_choices[1]:
        break
    else:
        input("Error, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')

os.system('clear')

#Calculating race stats and other things that will affect the rest of the code:

for i in range(0, 6):
    stat_list_after_add[i] = stat_list_before_add[i] + guys[check_race][1][i]

#checking what classes are available according to the race that the user has chosen:
player_classes = {}
check_class = '1'
while check_class == '1':
    print('Which class do you want to pick?\n\n')
    num = 0
    for i in range(0, 13):
        if guys[check_race][2][i] > 1:
            num += 1
            possible_class_choices.append(num)
            print(str(num) + ': ' + classes[i] + '   Max level: ' +str(guys[check_race][2][i]) + '\n')
            player_classes[str(num)] = str(classes[i])
    character_class = input('\n> ')
    if character_class in possible_class_choices:
        check_class = '2'
    else:
        input("Error, input must be either '1' or '2', press [Enter] to try again\n\n")
        os.system('clear')

print(player_classes_real[player_classes[str(character_class)]])


