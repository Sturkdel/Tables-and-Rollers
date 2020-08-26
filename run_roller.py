#this is a roller for random shadowruns
from random import randint
roll = randint(0,  7)
roller_output = []
print('Start roller')
roller_output.append('Meet locations')
if roll == 1:
    roller_output.append('At a bar, club or restaurant')
elif roll == 2:
    roller_output.append('at a warhouse, loading dock, or other underused location')
elif roll == 3:
    roller_output.append('in the barrens district or some other urban hell hole')
elif roll == 4:
    roller_output.append('in a moving vehicle')
elif roll == 5:
    roller_output.append('in a matrix host')
else:
    roller_output.append('in Astral space')
roller_output.append('Employers')
roll = randint(2,  13)
if roll == 2:
    roller_output.append('A secret society')
elif roll == 3:
    roller_output.append('a polictical or activist group')
elif roll == 4:
    roller_output.append('a government or government agency')
elif roll == 5 or 6:
    roller_output.append('a minor corporation')
elif roll == 7 or 8:
    roller_output.append('a megacorporation')
elif roll == 9:
    roller_output.append('a criminal syndicate')    
elif roll == 10:
    roller_output.append('a magical group') 
elif roll == 11:
    roller_output.append('a private individual') 
elif roll == 12:
    roller_output.append('an exotic or mysterious being') 
    
roller_output.append('Job Type')
roll = randint(1,  7)
if roll == 1:
    roller_output.append('a data steal')
elif roll == 2:
    roller_output.append('an assassination or demolition')
elif roll == 3:
    roller_output.append('an extraction or insertion')
elif roll == 4:
    roller_output.append('a misdirection')
elif roll == 5:
    roller_output.append('a protection')
else:
    roller_output.append('a delivery')
roller_output.append('Macguffins')
roll = randint(1,  7)
if roll == 1:
    roller_output.append('a key employee')
elif roll == 2:
    roller_output.append('a prototype product')
elif roll == 3:
    roller_output.append('cutting edge technology research')
elif roll == 4:
    roller_output.append('a bio-engineered life form')
elif roll == 5:
    roller_output.append('a magical object')
else:
    roller_output.append('an urban building, rural location, or infrastructure object')
roller_output.append('Twists')    
roll = randint(1,  7)
if roll == 1:
    roller_output.append('Security is unexpectedly high')
elif roll == 2:
    roller_output.append('A third party is also interested')
elif roll == 3:
    roller_output.append('The target is not what it appears to be (the group was lied to)')
elif roll == 4:
    roller_output.append('The job requires a rare piece of equipment')
elif roll == 5:
    roller_output.append('Target has been moved or is being moved')
else:
    roller_output.append('The employer decides to double-cross them')
    
print(roller_output)
