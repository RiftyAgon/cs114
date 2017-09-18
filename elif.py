"""
Text based game where user makes decisions which affect the character's future.
"""


import sys

def game_over():
    print("You broke the story. Nice job asshole.")
    return sys.exit()

def one_fail():
    print("You decide to wiggle away, as you feel your laziness \
wear on you. You crawl into bed and snoozle for a few days. \
When you wake, you find the story no longer is playable. You \
grump and click the little “x” on your computer.")

def two_fail():
    print("You prepare a spell, but are unable to dodge a \
quick fireball to the face. He pins you to the ground and \
slurps you, making you his pet.")

def three_fail():
    print("You decide this dragon isn't worth burning the \
cake in your oven and decide to walk away. You really are \
a cold heartless bastard. The writer is now pissed and ends \
your game here.")

def four_fail():
    print("Sithris turns around and tells you that you will \
no longer control his life and bangs Rift anyways. The \
writer zaps you and ends your game for being a buzzkill.")






print("You wiggle into the cave, watching the burning fire inside. To your \
right is a very grumpy orange dragon with a silver chest. He seems a tad \
cross over his home being invaded. You weigh your options. A blep is your \
standard greeting, maybe that will show the drake that you are a friend. \
You could fight the dragon, maybe your skills in ranged magic would defeat \
him. You do feel your loins tighten, maybe he’d be fine with you bending \
him over. You can either 1. blep the dragon 2. fight the dragon")

print("type choice")
x = input()
if (x == "blep the dragon") == True:
         print("it worked!")

elif (x == "bang the dragon") == True:
        print("While he may have agreed after introductions, \
the dragon did not enjoy the surprise in his keister. \
He eats you
    game_over

elif (x == "fight the dragon") == True:
    two_fail
    game_over
