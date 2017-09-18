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





def first_encounter():
    print("You are Sithris, a 20 year old black dragon with a knack for \
wiggling. Your two long white horns arc back and complement your sleek \
and stealthy body. You have a pair of goofy goggles on your head. You walk \
around aimlessly, watching deer running into charging panthers, giggling as\
the big cats are knocked silly. You sigh, feeling that you lack a life \
purpose. You look in the distance at a cave. You can either enter, or \
choose to wiggle away. Which do you pick? 1. wiggle away 2. enter cave")

    print("type choice")
    x = input()
    if (x == "enter cave") == True:
            print("you proceed")
    else:
        one_fail()
        game_over()

def second_encounter():
    print("You wiggle into the cave, watching the burning fire inside. To your \
right is a very grumpy orange dragon with a silver chest. He seems a tad \
cross over his home being invaded. You weigh your options. A blep is your \
standard greeting, maybe that will show the drake that you are a friend. \
You could fight the dragon, maybe your skills in ranged magic would defeat \
him. You can either 1. blep the dragon 2. fight the dragon")

    print("type choice")
    x = input()
    if (x == "blep the dragon") == True:
             print("it worked!")
    else:
        two_fail()
        game_over()




def third_encounter():
    print("You look directly at the dragon, his muscular form \
seeming even buffer at the discovery that he is short. You \
slowly poke your tongue out, smiling as the dragon giggles \
and does the same. The blep worked! The dragon explains that \
he goes by the name of Rift and is about the same age as you. \
He has been isolated from everyone for years. You feel bad for \
him. You can walk away and pretend you never met him. You can \
give him a hug. \
1. walk away 2. hug him")

    print("type choice")
    x = input()
    if (x == "hug him") == True:
             print("Aww! Cute!")
    else:
        three_fail()
        game_over()


def fourth_encounter():
    print("You give him a big hug and you two immediately \
have a connection. A few years pass and you two are gay lovers. \
You walk in one day after a hunt and find Rift in a lewd position. \
You can either bang the dragon, or turn him away. \
1. bang him 2. don't bang him")

    print("type choice")
    x = input()
    if (x == "bang him") == True:
             print("You and Rift engage in a passionate \
love making session and you giggle at how derpy he is. \
You two are now officially mates. Congrats, you have a \
life purpose! You both live a happily ever after.")
    else:
        four_fail()
        game_over()

    return sys.exit()











def main():
    first_encounter()
    second_encounter()
    third_encounter()
    fourth_encounter()

main()
