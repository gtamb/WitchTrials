# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#from email.mime.nonmultipart import MIMENonMultipart


define p = Character("Player")
define t = Character("Townsperson")

# default suspicion = 100 # overall score for suspicion, gets updated with each choice. 
# # The game starts here.
# default day = 1
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show Player happy

    # These display lines of dialogue.

    "You have entered the sleepy town of 'Salem' (temp name), which never thought it would experience anything like this again"

   # p "Once you add a story, pictures, and music, you can release it to the world!"


    # introduce to character 
    # This ends the game.
label reset_game:
    default suspicion = 100 # overall score for suspicion, gets updated with each choice. 
    default day = 1
label first_day:
   
    # This is the first day scene. The player will encounter various characters and respond to their dialogue. 
    # Their choices will affect their overall score and then at the end of the scene, they will be judge based on their percentage and either be accused 
    
    t "Did you hear Mary was seen speaking in tongues in her garden?"

    menu:
        t "Can you believe it?"

        "How could she? I always knew something was not right with her.":
            # change score for not standing up with someone, but going with the crowd
            $suspicion = suspicion - 10
           # $suspicion = int(suspicion)
            

        "They could never! I have known Mary for all my life and she has always been a good person.":
            $suspicion = suspicion - 30

        "Wow, I had not heard that":
            $suspicion = suspicion
            #neutral answer first time does not affect the suspicion score. 

    jump player_decision
    #temp !!! 
   # hide choice1
   # t "Your score after that decision is [suspicion]"

label second_day:

    #temp dialogue
    "Day 2 dialogue and choices"

    jump end_of_game
    # menu:

    #     "Would you like to try again or exit?"

    #     "Restart":
    #         jump reset_game
    #     "Exit":
    #         return



label player_accused:

    # This is the scene if player gets the bad odds and gets accused. They will then be burnt at the stake 
    
    "You have been accused of witchcraft"

    #jump to being burnt at the stake

    # You survived # days

    menu:

        "Would you like to try again or exit?"

        "Restart":
            jump reset_game
        "Exit":
            return


    # add button for restarting game and exiting

label player_survives_day:
    
    # This is the scene for if the player survives the day and it is not the final day. They will be shown that they survived and the get to click for the next day. 
    # (Maybe see someone else be accused an burnt at the stake on some days or every night)
    


    "You survived day [day]"
    if day == 5:
        jump end_of_game
    $ day = day +1

    menu:
        "Start Next Day"

        "Next Day":
            jump second_day
        "Exit":
            return

label player_decision:
    
    # The decision for the player to survive or die
    

    $decision = renpy.random.randint(0, 100)
    # survive
    if decision <= suspicion:
        jump player_survives_day
    else:
        jump player_accused
# init python:

#     def get_decision():
#         decision = renpy.random.randint(0, 100)
label end_of_game:
    """
    This is the end of the game. The player will be shown one of three endings based on their overall choices. 
    """
    return
