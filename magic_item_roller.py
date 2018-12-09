'''this is the magic item roller'''
#!/usr/bin/python
#Filename: magic_item_roller
from random import randint
times_rolled = 0
def magic_item(table): 
    roll = randint(0,101)
    print (roll)
    table = int(table)
    if table == 1:		
        if roll in range(52):
            print("Potion of healing")
        elif roll in [52,53,54,55,56,57,58,59,60]:
            print("spell scroll (cantrip)")
        elif roll in [61,62,63,64,65,66,67,68,69,70]:
            print("potion of climbing")
        elif roll in [71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]:
            print("spell scroll 1st level")
        elif roll in [92,93,94,95]:
            print("spell scroll 2nd level")
        elif roll in [96,97,98,99]:	
            print("potion of greater healing")
        elif roll in [100]:
            print("Bag of holding")
        else:
            print("Driftglobe")
    elif table == 2:
        if roll in range(0, 16):
            print ("Potion of greater healing")
        elif roll in range(16,  23):
            print ("potion of fire breath")
        elif roll in range(23,29):
            print ("Potion of resistance")
        elif roll in range(30,35):
            print ("Ammunition +1")
        elif roll in range(35,40):
            print ("Potion of animal Friendship")
        elif roll in range(40,44):
            print ("Potion of hill giant strength")
        elif roll in range(45,49):
            print ("Potion of growth")
        elif roll in range(50,54):
            print ("Potion of water breathing")
        elif roll in range(55,59):
            print ("spell scroll 2nd level")
        elif roll in range(60,64):
            print ("Spell scroll 3rd level")
        elif roll in range(65,67):
            print ("Bag of holding")
        elif roll in range(68,70):
            print ("Keoghtoms's Ointment")
        elif roll in range(71,73):
            print ("Oil of Slipperiness")
        elif roll in range(74,75):
            print ("Dust of disappearance")
        elif roll in range(76,77):
            print ("Dust of Dryness")
        elif roll in range(78,79):
            print ("Dust of sneezing and choking")
        elif roll in range(80,81):
            print ("Elemental Gem")
        elif roll in range(82,83):
            print ("Philter of love")
        elif roll == 84:
            print ("Alchemy Jug")
        elif roll == 85:
            print ("Cap of Water breathing")
        elif roll == 86:
            print ("Cloak of the manta ray")
        elif roll == 87:
            print ("Drift Globe")
        elif roll == 88:
            print ("Goggles of Night")
        elif roll == 89:
            print ("Helm of Comprehending Languages")
        elif roll == 90:
            print ("Immmovable Rod")
        elif roll == 91:
            print ("Lantern of Revealing")
        elif roll == 92:
            print ("Mariner's Armor")
        elif roll == 93:
            print ("Mithral Armor")
        elif roll == 94:
            print ("Potion of poison")
        elif roll == 95:
            print ("Ring of swimming")
        elif roll == 96:
            print ("Robe of useful items")
        elif roll == 97:
            print ("Rope of Climbing")
        elif roll == 98:
            print ("Saddle of the cavalier")
        elif roll == 99:
            print ("Wand of magic detection")   
        else:
            print ("Wand of secrets")
times_rolled = int(input("How many times do you want to roll on the table?"))
time = range(times_rolled) 
for x in time:
    magic_item(input("Which table? Instead of letters, put the number that letter "))
