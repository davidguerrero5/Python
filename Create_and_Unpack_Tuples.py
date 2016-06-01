#David Guerrero
#Creating and unpacking tuples
import random

character = ('DarkLord', 'Male')
characterattributes = ('Agility Level:', 'Stealth Level:', 'Magic Level:')
name, gender = character
attribute1, attribute2, attribute3 = characterattributes
for item in character:
    print item
for attribute in characterattributes:
    print attribute,random.randint(0,10)