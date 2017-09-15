"""
Text based game where user makes decisions which affect the character's future.
"""


import sys

def game_over():
    print("You broke the story. Nice job asshole.")
    return sys.exit()

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
    if (x == "enter") == False:
            print("it worked!")
    else:
        game_over()





# def second_encounter():
#     print("You wiggle into the cave, watching the burning fire inside. To your \
#     right is a very grumpy orange dragon with a silver chest. He seems a tad\
#      cross over his home being invaded. You weigh your options. A blep is your \
#      standard greeting, maybe that will show the drake that you are a friend. \
#      You could fight the dragon, maybe your skills in ranged magic would defeat \
#      him. You do feel your loins tighten, maybe he’d be fine with you bending \
#      him over. You can either 1. blep the dragon 2. fight the dragon \
#      3. bang the dragon.")
#     choice = input()
#     if choice == "blep":
#
#
#     elif
#
#     else:
#         game_over()



# def third_encounter():
#     print(You look directly at the dragon, his muscular form seeming even buffer at the discovery that he is short. You slowly poke your tongue out, smiling as the dragon giggles and does the same. The blep worked! The dragon explains that he goes by the name of Rift and is about the same age as you. He has been isolated from everyone for years. You feel bad for him. You can walk away and pretend you never met him. You can offer him advice and hope he takes it. You can give him a hug. 1. walk away 2. give advice 3. hug him
#
#
#
#     )
#     if choice == "blep":
#
#
#     elif
#
#     else:
#         game_over()







# def fourth_encounter():
#     print(You give him a big hug and you two immediately have a connection. A few years pass and you two are gay lovers. You walk in one day after a hunt and find Rift in a lewd position. You can either bang the dragon, or turn him away. 1. bang him 2. don't bang him)
#
#
#
# )
#     if choice == "blep":
#
#
#     elif
#
#     else:
#         game_over()












def main():
    first_encounter()
    # second_encounter()
    # third_encounter()
    # fourth_encounter()

main()
