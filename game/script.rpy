# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define notRelWink = Character('''?????
{size=-10}They/them{/size}''')
define rell = Character('''Rell
{size=-10}She/her{/size}''')
define me = Character("me")

# The game starts here.

label start:
    play music "backround.ogg" loop
    jump Meeting
    jump Identity
    jump Fight
    jump Beauty
    jump Lovers
    jump Ending

    return

label Meeting:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene bg noxus png
    show unknown
    with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    notRelWink "You're awake."
    notRelWink "I wasn't able to help you that much. Do you remember anything?"

    menu:
        "…":
            notRelWink "You are Null. One of the students of the Black Rose Academy. You were like me, remember? {w=1.0} They made us fight each other. When you lost, your combat magic, your sigil and your mind were taken away from you. Do you remember?"

    ## "The hazy figure lets out an exasperated sigh"
    menu:
        "…":
            notRelWink "{size=+25}{i}sigh{/i}{/size}"
        "drool a bit":
            notRelWink "{size=+25}{i}sigh{/i}{/size}"


    notRelWink "This isn’t working! {w=1.0} I couldn’t save Gabriel, at least let me save you!"

    # sperated speach

    #"They grab their arm resting over the pretty shapes that curl over their skin."
    #"They wince as part of their skin tears away in a jagged piece that resembles a rock."
    #"The rock shines with the pretty shape."
    #"They press the rock into your hand, and it sinks into your skin"

    #  not seperated
    "They grab their arm resting over the pretty shapes that curl over their skin. They wince as part of their skin tears away in a jagged piece that resembles a rock. It shines with the pretty shape."
    "They press the rock into your hand, and it sinks into your skin"

    show rell base
    hide unknown
    with dissolve

    notRelWink "I know it's not the same as your own power. This was the sigil of another kid, just like you and I."
    "You feel the rock pressing into your hand. It makes you feel a bit better."

    "Words are easier to understand and you feel like you can speak.{nw}"

    menu:
        "Words are easier to understand and you feel like you can speak.{fast}"

        "…":
            rell "It didn’t work huh {cps=10}...{/cps} {w=1.0} Hopefully you’ll feel a bit better over time. I am Rell, I go by she/her, but I guess you can’t really talk about me anyway…"


        "Who are you?":
            rell "I’m Rell, I go by she/her. It’s good to meet you."

label Identity:
    rell "Well, what do we do next?"

    menu:
        "Defy Noxus and taste your own blood!":
            hide rell base
            show rell angry
            rell "Alright. Die then."
            play sound "First Blood Sound.ogg"
            scene you d
            with fade
            "Click to start over"
            return
        "I want to come with you.":
            rell "You can come with me but it might be dangerous, I’m not protecting you if you get in the way!"


    "Rell’s mount forms under her, a huge horse creature formed all out of iron. She offers you a hand up and you get pulled up behind her."

    rell "I was created to be Noxus’ knight in shining iron, to take down Mordekaiser. No matter what I do, I never know who I am."
    rell "For now, I’m going to keep traveling across Runeterra protecting Nulls like you, and fight back against the Black Rose using the powers they stole and forced into me."
    menu:
        "What did the Black Rose do?":
            rell "They made me fight other kids."
            rell "There was a boy in the Academy with me."
            rell "He was the most beautiful boy."
            image eileen movie = Movie(play="new-video.mpeg",loop=False,image="final frame.jpg",size={1240,914}, ypos=914)
            show eileen movie
            with dissolve
            rell "His power was nothing. He created clay animals. They would dance across his hands. He made them for me. It couldn't last. I had to fight him, and I won. He was Null and I grew in power. I used his power to fight back, to fight for the future we wanted.{w=1.0} "
            hide eileen
            with dissolve
            rell "I looked for Gabriel for a long time but by the time I found him it was too late."
            menu:
                "I'm sorry for your loss.":
                    rell "Gabriel is no more, but there are still Nulls out there waiting for me to save them."

    menu:
        "What are your thoughts on Mordekaiser?":
            hide rell base
            show rell blush
            rell "He's DILF material. Any enemy of the blackrose is a potential ally for me. They created me to take him down but I don't see a need to, not after this mess."
        "What are we going to do about the Null?":
            rell "Those academy kids are still out there. I'll find them all. I'll save them."
    hide rell blush
    show rell base

label Fight:
    "You ride together on Rell's iron mount towards the next town."
    "She is rather quiet{cps=10}...{/cps}"
    "On the edge of your eyesight you spot dust rolling over the land approaching you. Pointing it out to her, she helps you off her iron horse."

    rell "Stay behind me, and I will keep you safe."

    "The iron horse rears up and charges forward as Rell meets the onslaught of black clad Noxian soldiers."
    "They recognize her instantly and with the postings to capture her alive across the country they instantly engage in combat."
    "It's over fast with metal armor collapsing in on its owner's bodies."

    rell "We're free and safe."

    "The two of you continue riding until nightfall, making camp in a thicket of trees near a field. You find kindling for a fire as Rell hunts."
    #play sound "fire-crackling-noise.ogg" loop
    "{i}some time passes{/i}"
    "Rell comes back with two rabbits, each killed neatly in the head with a small piece of iron."
    "Rell explains how to prepare the rabbits, cooks them, and eats them with you. Full and relaxed she stares out across the horizon."

    "{cps=10}...{/cps}"
    #stop sound
label Beauty:

    rell "Noxus can be beautiful."

    menu:
        "Not as beautiful as you.":
            "{b}Gross{/b}. You're a bit too old for me."
        "It's good you can still find beauty in a place as horrible as this.":
            "It is the home of my nightmares but also of my dreams. My dreams of controlling my life and my decisions. My mom can't control my desires any more."

label Lovers:
    rell "I want to move on with my life. I loved Gabriel but I will find more people to love."

    menu:
        "I bet you like girls more.":
            rell "I’m only 16. I don't know if I'm gay. I’ll figure out my life when I want to."
        "I bet you like boys more.":
            rell "I’m only 16. I don't know if I'm straight. I’ll figure out my life when I want to."
    menu:
        "That makes sense, I don’t think you need to decide right away!":
            rell "Thank you."
        "Surely there is someone you have a crush on!":
            hide rell base
            show rell blush
            rell "“There might be someone{cps=10}...{/cps} tall {cps=10}...{/cps} super-strong armored lady."
    hide rell blush
    show rell base

label Ending:
    scene final
    with fade
    rell "There's a blue side and a red side in this war, but maybe somewhere in the middle we can make purple"

    "Thank you for playing!"

    "click on to return to the main menu!"
