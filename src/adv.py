from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('player', room['outside'])

# room property to check if valid movement
def try_movement(direction, room):
    attribute = direction + '_to'

    if hasattr(room, attribute):
        return getattr(room, attribute)
    else:
        print(f'\nLooks like a dead end.... try another direction.\n')
        return room

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

quit = False
helping = False

commands = ['n', 'e', 's', 'w']
controls = ['q', 'help']

help_message = '========== DIRECTIONS ===========\n\nUse the keys:  n | e | s | w - to move from room to room.\nUse the key:  q - to quit game.\n\n================================='

error_message = '\nThinking outside the box, I like it!\nPlease stick to n, e, s, w, or q.\nEnter \'help\' for more details.\n'

help_error = '\n---> Invalid input. Please type \'y\' or \'n\'. <---\n'

help_y = '\n---> Glad to be of service! <---'
help_n = '\n---> Take your time. <---\n'

while not quit:

    while helping:
        # help prompt for user input
        help_prompt = input('Done? [y] [n]: ')

        if help_prompt == 'y':
            helping = False
            print(help_y)
        elif help_prompt == 'n':
            helping = True
            print(help_n)
            print(help_message)
        else:
            helping = True
            print(help_error)
            print(help_message)

    # print players current room and description
    print(f'\n...{player.current_room.name}: {player.current_room.description}\n')
    print(f'\n...Inventory: {player.inventory}\n')
    print(f'\n...Items in Room: {player.current_room.items}\n')

    # User Input
    prompt = input('---> ')
    pt = prompt[0]

    # quit game if player inputs 'q'
    if pt == 'q':
        quit = True

    # Directions
    if prompt == 'help':
        helping = True
        print(help_message)

    # Catch non valid user inputs
    if pt not in commands and prompt not in controls:
        print(error_message)

    # Valid user inputs
    if pt in commands:
        print(f'\nChecking route....\n')
        player.current_room = try_movement(pt, player.current_room)
