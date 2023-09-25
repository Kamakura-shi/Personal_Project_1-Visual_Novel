# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Midoriya")

transform left:
    xalign 0.25
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

transform middle:
    xalign 0.5
    yalign 1.0    

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "midoriya happy.png" to the images
    # directory.

    show midoriya happy at left

    play music "ua.mp3" fadeout 1

    # These display lines of dialogue.

    e "My name is Midorya, welcome to my world!"

    e "Now, we'll go to UA,follow me!"

    menu:

        "No":
            jump choice1_no
        
        "ok":
            jump choice1_yes

label choice1_no:

    $ menu_flag = False

    e "Alright! Where do you want to go instead?"

    menu:

        "Somewhere cooler":
            jump choice1a_cool
        
        "I want to fight!":
            jump choice1a_fight

label choice1a_cool:

    $ menu_flag = True

    e "Alright! I have the right place for you..."

    jump konoha

label choice1a_fight:

    $ menu_flag = False

    e "Okay, what do you think of this place then?..."

    jump cell        

label konoha:

    scene bg konoha

    show midoriya happy at right

    play music "konoha.mp3" fadeout 1

    e "Alright! What do you think of this place?"

    menu:

        "It's fine":
            jump fine
        
        "Not cool enough!":
            jump no

label fine:

        $ menu_flag = True

        e "Alright! Enjoy!"

        return

label no:

        $ menu_flag = False

        e "Okay, come with me then"

        jump cell

label cell:

    scene bg cell

    show midoriya happy at middle:

    play music "cell.mp3" fadeout 1

    e "Alright! Let's fight!"

    return

label choice1_yes:

    $ menu_flag = True

    e "Okay! let's go!"

    jump ua

label ua:

    scene bg ua

    show midoriya happy:
        xalign 0.25
        yalign 1.0

    play music "ua.mp3" fadeout 1

    e "There we are!"

    e "Okay, bye bye!"

    # This ends the game.

    return
