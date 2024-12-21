
define p = Character("[player_name]", color = "#4287f5")
define MO = Character("Molly",  image = "molly_s", color="#fcba03")
define A = Character("Agnes", image="agnes_s",color ="#0e801f")
define M = Character("The Minister",  image="minister_s", color = "#f20707")
define H = Character("Henry",image="henry_s",  color = "#94779e")
define C = Character("Constable", image="constable_s", color = "#ff7373")

#https://www.freepik.com/free-vector/18th-19th-century-old-town-fashion-carriage-set-with-isolated-icons-human-characters-aristocrats-vector-illustration_26760920.htm#position=8&new_detail=true
image henry = "/images/pikaso-creations/henry_image.png"
image molly = "/images/pikaso-creations/Molly_image.png"
image agnes = "/images/pikaso-creations/agnes_image.png"
image minister = "/images/pikaso-creations/minister_image.png"
image constable = "/images/pikaso-creations/soldier_image.png"
image agnes_left = "/images/pikaso-creations/agnes_image_left.png"

image side henry_s = "/images/pikaso-creations/henry_small.png"
image side molly_s = "/images/pikaso-creations/Molly_small.png"
image side agnes_s= "/images/pikaso-creations/agnes_small.png"
image side minister_s= "/images/pikaso-creations/minister_small.png"
image side constable_s= "/images/pikaso-creations/soldier_small.png"
#https://www.freepik.com/free-vector/medieval-german-street-with-halftimbered-houses-sunset_14878825.htm#position=2&new_detail=true
#https://www.freepik.com/free-vector/medieval-german-street-with-halftimbered-houses-night_14977749.htm#position=1&new_detail=true
#https://www.freepik.com/free-vector/medieval-town-street-with-old-european-buildings_8924480.htm#position=3&new_detail=true
init: 
    define center = Position(xalign = 0.5)
    define left = Position(xalign = 0.3)
    define right = Position(xalign = 0.7)
    define far_right = Position(xalign = 0.9)
    define far_left = Position(xalign = 0.1)

image town_morning = "/images/village_sunrise.jpg"
image town_evening = "/images/village_sunset.jpg"
image town_night = "/images/village_night.jpg"

#https://gifer.com/en/ncH
image black = "#000000"
define flame_imgs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
image flames:
    
    "/images/flames1.jpg"
    pause 0.1
    "/images/flames2.jpg"
    pause 0.1
    "/images/flames3.jpg"
    pause 0.1
    "/images/flames4.jpg"
    pause 0.1
    "/images/flames5.jpg"
    pause 0.1
    "/images/flames6.jpg"
    pause 0.1
    "/images/flames7.jpg"
    pause 0.1
    "/images/flames8.jpg"
    pause 0.1
    "/images/flames9.jpg"
    pause 0.1
    "/images/flames10.jpg"
    pause 0.1
    "/images/flames11.jpg"
    pause 0.1
    "/images/flames12.jpg"
    pause 0.1
    "/images/flames13.jpg"
    pause 0.1
    "/images/flames14.jpg"
    pause 0.1
    "/images/flames15.jpg"
    pause 0.1
    "/images/flames16.jpg"
    pause 0.1
    "/images/flames17.jpg"
    pause 0.1
    "/images/flames18.jpg"
    pause 0.1
    "/images/flames19.jpg"
    pause 0.1
    "/images/flames20.jpg"
    pause 0.1
    "/images/flames21.jpg"
    pause 0.1
    "/images/flames22.jpg"
    pause 0.1
    "/images/flames23.jpg"
    pause 0.1
    "/images/flames24.jpg"
    pause 0.1
    "/images/flames25.jpg"
    pause 0.1
    "/images/flames26.jpg"
    pause 0.1
    "/images/flames27.jpg"
    pause 0.1
    repeat
#https://www.freepik.com/free-vector/local-food-market-with-wooden-stalls-with-honey-vegetables-meat-fish-cheese-vector-cartoon-summer-landscape-with-street-marketplace-with-farm-produce-kiosks-counters_24499390.htm#position=4&new_detail=true
image market = "/images/market.jpg"
#https://www.freepik.com/free-vector/courtroom-interior-background-trial-justice-room_41797388.htm#position=9&new_detail=true
image courtroom = "/images/courtroom.jpg"
#https://www.freepik.com/free-vector/typewriter-desk-author-vintage-office-vector_44156983.htm#position=1&new_detail=true
image office = "/images/office.jpg"

# default suspicion = 100 # overall score for suspicion, gets updated with each choice. 
# # The game starts here.
# default day = 1

# transform position1:
#     xalign 0.7
#  #   yalign 1
# transform position2:
#     xalign 0.9
#   #  yalign 1

label reset_game:
    default suspicion = 100 # overall score for suspicion, gets updated with each choice. 
    default day = 1
    default sold_out = False
    default stand_up = False
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene town_morning
    # directory.

    #show Player happy

    # These display lines of dialogue.

    "The small town of Holsworthy has long been filled with a tight knit community of hardworking people. They had long participated in each other's lives, and worked to support  their town and exemplify their traditional values to their neighbours. "

    "Yet, all was not right in Holsworthy these days for a madness had sprung up into their minds, turning neighbour against neighbour, and friend against friend. No one knew what was to come, yet even if they did, nothing would have derailed what was to come. "

    $player_name = renpy.input("What is your name?")
    $player_name = player_name.strip()

    if player_name == "":
        $player_name = "Player"

    # introduce to character 
    # This ends the game.

label first_day:
   
    # This is the first day scene. The player will encounter various characters and respond to their dialogue. 
    # Their choices will affect their overall score and then at the end of the scene, they will be judge based on their percentage and either be accused 
    #!!! show molly image
    scene market
    show molly at right
    MO "Did you hear [player_name]? The Nelsons' servant was just arrested for witchcraft! "

    p "Which one? For what reason? The Nelson family has always been such a pillar of the community and treated their help akin to family"

    menu:
        MO "They say the maid was caught speaking in tongues and attempting to summon the devil."

        "That is horrible, I cannot even imagine what the Nelson’s are going through":
            # change score for not standing up with someone, but going with the crowd
            $suspicion = suspicion*0.95
            MO "It goes to show the risk taking in someone of that background."
           # $suspicion = int(suspicion)
        

        "I cannot believe that! She has always been such a sweet and polite girl.":
            $suspicion = suspicion*0.85
            MO "Be careful young one, these kind of women can entrap and beguile even the most devout. Be on your guard against dark forces."


        "Wow, I had not heard that":
            $suspicion = suspicion*0.99
            #neutral answer first time does not affect the suspicion score.
            MO "I am glad that I could inform you of this deception that has taken place here in our village. You are a young girl and I would hate for you to be misled like that maid."
    
    #after choice dialogue
    hide menu
    MO "Now I will take my leave, I wish to return home well before nightfall, stay safe my dear. "
    #with dissolve
    #hide molly 
    with dissolve
    ### get rid of MOLLY image
    scene town_evening
    ## AGnes arrives 
    show agnes_left at center
    A "I could not help but overhear dear Molly about the witch who was arrested, terrible news that. You must know that that is not the end of it, for that ignores how witchery infects noble communities and drives those to sin. Do you think the Nelson’s were simply ignorant to the demonic deeds of their servant?"
    A "It is to be expected though, that family has always been overly fortunate, flaunting their wealth and bountifulness in front of everyone, displaying a false image of piety and humbleness. "
    A "Now it all makes sense, their false fortune was made through evil deeds with the devil. You must be on your guard, dear girl, to make sure the wickedness that is infecting our community does not get you too. Everyone is in danger."
    
    menu:

        "I will keep a sharp eye out for witchcraft and keep myself safe from them.":
            $suspicion = suspicion*1.1
        "Definitely. <<eyes the exit>>":
            $suspicion = suspicion*0.8
    hide menu
    A "Good good, I knew I could count on such an upstanding young lady such as yourself."

    ## Minister Appears 
    with dissolve
    show minister at left 
    M "Good day Agnes, and young [player_name]. How fare you this fine afternoon?"

    A "Well enough, now that a true attempt at saving us from evil has been made."

    M "Ah, yes of course, it is truly good to see that such a virtuous woman such as yourself can bear witness to our attempts to remove the taint of witchcraft from our fair town."

    M "You know, I as the minister of Holsworthy saw that it was necessary to volunteer my time with the searches for devilry, as only a truly righteous man can resist their beguilements and capture them."

    M "I also rely on the strength of my community for my holy work. Now, [player_name], I hope that I can trust in you to tell me if you have borne witness to any enchantments or other sorcery."

    menu:
        "I have yet to witness anything, but I will inform you should that occur.":
            $suspicion = suspicion*0.95
            M " Excellent! It is always good to see someone willubf to do the Lord's work. "

        "No, it is wrong to spy on my neighbours.":
            $suspicion = suspicion*0.4
            M "Interesting, very interesting. It is wrong to have sympathy for those who have sold their souls to the devil and are already lost. But young women such as yourself are often driven to fits of hysteria and not trusted to be able to protect themselves,  [player_name]"
    hide menu
    #with dissolve
    jump player_decision

label second_day:

    # show Molly in market scene
    with dissolve
    scene market
    show henry at center
    show molly at right
    MO "Henry dear! It is so good to see you again, I cannot thank you again for your help with my dear husband's sickness, those herbs you recommended to me were a godsend."

    H " It was no problem at all ma'am, if you have any concerns about your husband or son, do stop in to the apothecary and I will see what I can do. "

    p "It is good to hear your husband is doing better Molly. "

    # agnes appears
    show agnes at left
    A " Did you witness the execution last night? It feels so good that the evildoers are being pushed out of our dear town."
    p "I… had not, I went home early last night. What happened?"
    A "Oh, they arrested Mrs. Nelson along with the rest of her staff, apparently she had been using her powers to steal the beauty from a bunch of young girls in town. As I told you yesterday, I always suspected that she was not to be trusted. "

    
    MO " Oh dear, well I am glad that the upstanding members of the church were able to uncover her actions. "

    A "The question is who else has been taken in by those malefactors? It cannot just be those who have been accused, for they have all been pillars of the community. They had access to so many people who knows how many more witches stand among us, deceiving us with falsities and empty words. "

    H "How would you tell that someone is a witch without seeing them do witchcraft? "


    A "There are signs, you see, of how the devil reaches through them. No true righteous person would be so damaged upon their body or their soul, through blemishes, fits and poor behaviour. "

    MO "Poor behaviour? Oh have you heard of young Malcolm? A heartbreaker that one, all the girls have been chasing after him but he is just leaving a trail of broken hearts. "
    MO "One day he will take pity on one of the poor lasses and I bet they would have such beautiful babies. Maybe our dear [player_name] might take him off the market and put all those girls out of their misery so they can act proper once more. "

    menu: 
        "Yes, he is a fine young man, thank you for your suggestion.":
            $suspicion = suspicion*1.2

        " Malcolm is a nice man, however I am not interested in him.":
            $suspicion = suspicion*0.85

        "Thank you for your kind words.":
            $suspicion = suspicion*1.1

    hide menu
    
    A "Yes, I had heard. A polite gentleman, with nary a presence in any room of ill-repute. You are close with him are you not Henry? Have you seen any signs of the devil around him? It is quite strange how those young ladies fall over themselves without fail. "
    
    H "Yes, that is just Malcolm, unfailingly kind and wonderful to all women. If you will excuse me I have to go right now, fair thee well Madams. "

    #henry is about to leave but the constable appears
    with dissolve
    show constable at far_left
    C "Henry Beauchamp, I have a warrant for your arrest."
    H "Arrest? But…. I have not done anything?"

    C "You are being arrested for witchcraft based on accusations that you caused maladies and disfigurements among the upstanding populace and consorting with men in the ways of the devil. Come quietly and your fate will be in the courts hands, otherwise it will be in mine."

    menu:
        "Henry, you must trust in the court that the court will see your innocence. You will be fine, the truth will prevail over the lies spread by this madness":
            $suspicion = suspicion*0.7
        " <<say nothing>>":
            $suspicion = suspicion*1.4
        "Henry… I will pray for you. ":
            $suspicion = suspicion*0.9
    hide menu

    H "I would never do these things they say, I have only tried to heal people and—-"

    C " Save that for the judge, witch."
    with dissolve
    hide henry 
    hide constable
    hide agnes
    with dissolve
    show agnes at center


    #henry is handcuffed and he and the contasble leave
    A "It warms my heart to see the law taking charge  to protect Holsworthy's citizens"
    MO "But… it's Henry. We have known him his entire life, he has always been ever so helpful, just last week he helped me with my dear husband's malady. And my son came down with the same thing. How will he get better now?"

    A "I would be very careful with your son Molly, who knows what he could have done to infect your son with his wickedness. He could have corrupted you as well!"

    menu: 
        "I am certain Molly is just worried about her family's safety and will take steps to protect them now that Henry has been taken into custody.":
            $suspicion = suspicion*0.9

        "Molly, there is nothing to do about Henry, focus on your own family":
            $suspicion = suspicion*0.8

        "Agnes is right Molly, you should look to save your family from others influences.":
            $suspicion = suspicion*1.1
    hide menu
    MO "Rr..ight, I will go check on my family now."

   # with dissolve
    jump player_decision

label third_day:
    #constable appears in the 
    with dissolve
    scene town_morning
    show constable at left
    C "The minister would like to speak with you "
    p "Now?"
    C "We don't have all day"

    # switch background to the ministers office
    with dissolve
    scene office

    show minister at center
    show constable at far_left
    M "Ah, young miss, so good of you to join us this morning. I trust that you are well. "
    p "Yes, sir."
    M "Let's skip the pleasantries and get to what I wanted to discuss with you. It has been mentioned in passing that you have been involved with several of the accused. Do you have anything to say to this?"
    menu:
        "I have always strove to help all members of the community, but I have never witnessed or been involved with any type of witchcraft.":
            $suspicion = suspicion*0.7
        "It is horrible that anyone would want to drag my name into their devilry for their own nefarious reasons. I would condemn the mere association of my name with witchcraft":
            $suspicion = suspicion*0.8
    hide menu
    M "Thank you for being honest with me dear. But, it does surprise me that you have never seen anything. Are you certain that that is the truth of the matter? You have not witnessed any immoral behaviours or perhaps seen any overly sympathetic persons to the plight of the accused?"

    menu: 
        "Well, I am not trying to judge anyone but Molly was acting a bit strange when Henry was arrested for witchcraft yesterday.":
            $sold_out = True
            $suspicion = suspicion*0.95
        "I keep to myself and have not seen or heard about anyone involved in witchcraft besides the rumours about those who have been arrested. ":
            $suspicion = suspicion*0.8
        "Not to my knowledge, sir. ":
            $suspicion = suspicion*0.6
    hide menu
    M " It is good that you have been such and upstanding citizen. It is the only way that this community can survive, you see, if we all work together to drive out the wickedness from our former friends and neighbours. Only then we can truly thrive. "

    menu:
        "Of course, sir. Thank you for your dedicated work.":
            $suspicion = suspicion*0.95
        "Yes, sir.":
            $suspicion = suspicion*0.85
    
    hide menu
    jump player_decision


label player_survives_day:
    
    # This is the scene for if the player survives the day and it is not the final day. They will be shown that they survived and the get to click for the next day. 
    # (Maybe see someone else be accused an burnt at the stake on some days or every night)
    

    if day == 1:
        $who_died = "the maid"
    elif day == 2:
        $who_died = "Henry and Malcolm"
    else:
        $who_died = "Molly"
    "You survived day [day] in Holsworthy, but [who_died] did not."

    if day == 3:
        jump end_of_game
    $ day = day +1

    menu:
        "Start Next Day"

        "Next Day":
            if day == 2:
                jump second_day
            else:
                jump third_day
        "Exit":
            return
    hide menu

label player_decision:
    with dissolve
    scene town_night
    
    # The decision for the player to survive or die
    #scene town_night 
    "End of Day [day]"
    # add pause then get decision 
    $decision = renpy.random.randint(0, 100)
    # survive
    if decision <= suspicion:
        jump player_survives_day
    else:
        jump player_accused


label end_of_game:

    #This is the end of the game. The player will be shown one of three endings based on their overall choices. 
    
    if sold_out == True:
        p "I made it through the first wave of madness, but at what cost? The trials are not going to stop, my neighbours are going to keep on getting arrested, there is no end in sight. "
        p "What am I supposed to do? I kept my head down, but I don't know how long that will save me. How long will I be able to live with myself while innocent people are dying?"
        p"I don't believe that they committed the evil acts the minister is saying they did. How am I supposed to move forward when nothing is being done to stop this."
        p "Who is going to stop this?"

    elif stand_up == True:
        p "It is not enough. I stood up for Henry and I protected my friends from the ministers probing questions and they still killed them. I thought I could trust in the court to stand up for the innocent and for the minister to practice the holy words he preached, but I was wrong."
        p "The law will not save any of us when in the hands of those who seek to destroy innocent lives. So I will have to intervene. "
        with dissolve 
        scene black
        show flames
        with Pause(2)
        p "The jail and the minister's house are both made of wood, and they have shown us all how fast a blaze can spread. They betrayed our community and they betrayed me. It is only right that I respond."
        p "I do not know if this will stop the madness that they have enacted, but nobody else is going to do anything. I will be the change and drag us from this path, nothing else would do."
    else:
        p "All I did was tell the minister what she said. I did not think that they would kill Molly. I was not as close to any of the others accused of witchcraft and I was not directly responsible for their accusations. I just went along with what everyone else was saying."
        p "It is alright, no accusation or lies will touch me now that I helped the Minister. I will be safe, and everyone else is on their own. It has always been this way."
        p "But… the accusations are not going to stop. I saw Agnes that day at the Ministers office, she was going into speak with him as well. She has always been overly involved with everyone elses personal business and would be glad to take down those she dislikes."
        p "I do not think I would be able to stand against anything someone of her stature and reputation. She and Molly were close for years, and the moment Molly faltered in her conviction, I could tell Agnes turned away from her."
        p "	God, what am I supposed to do?"
    

    with dissolve 
    scene town_night
    #add end choice to restart the game or exit
    menu:

        "Would a different choice change your fate?"

        "Restart":
            jump reset_game
        "Exit":
            return
    hide menu

    


label player_accused:

    # This is the scene if player gets the bad odds and gets accused. They will then be burnt at the stake 
    with dissolve
    "You have been accused of witchcraft"
    scene courtroom
    show minister at left
    if day == 1:
        M "You have been accused of the crime of witchcraft, taken in by the spread of devilry. The pyre is the only way to cleanse your soul."
    elif day == 2:
        M " You have been accused of witchcraft, after cavorting with witches and using their enchantments. It is time to cleave your misbegotten soul from this plane and bring about a just punishment."
    else:
        M "[player_name] you tried to lie about your associations with witchcraft however your wickedness showed through. The only way forward is on the pyre, where you will burn."
   
    with dissolve
    scene black
    show flames
    with Pause(2)
    "You were burnt at the stake."

    menu:

        "Would a different choice change your fate?"

        "Restart":
            jump reset_game
        "Exit":
            return
    hide menu


