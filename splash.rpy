init python:
     #Guess some references below!
     splash_messages = renpy.random.choice([
     "Welcome to the Literature {s}Club{/s} Abyss. You've been living here for as long as you can remember",
     "If you feel bad listen to Kaeya.\nIf you feel stressed or you need to sleep listen to Kaeya.\nIf you feel obsessed... anyway listen to Kaeya!",
     "SnVzdCBZb3UgYW5kIE1lIGFuZCBFdGVybml0eQ==",
     "Mo·Ni·Ka when??????",
     "I can't decide whether I should simp for or die",
     "Celestia is watching you!",
     "Cryo is fate!",
     "YATTA!",
     "If you feel the writing level degradation, report to the Dev ASAP",
     "This game is unnoficial fanwork affilated with one of Cyno's jokes",
     #Further plans:
     #1. Add time-limited disclaimers (idk if it's possible)
     ])

label splashscreen:

     default persistent.first_run = False

     python:
          try: renpy.file(config.basedir + "\\game\\first_run.txt")

          except: open(config.basedir + '\\game\\first_run.txt', 'r')

     show img_warning1

     pause 0.5

     pause 1.0
     "The current version is not an indicative of a final product!"
     "[config.name] is a fan game not affiliated with HoYoverse. This fanwork is a creator's own representation and is not meant to be canon by any means."
     "It contains spoilers to Kaeya's story, bits of scary content, old concept ideas, placeholders and possible grammar mistakes funny or not depending on your vision!"
     "If you found them, report to dev ASAP! But remember, there's no guarantee the dev will solve your problem fast."

     #"[config.name] is a fan game not affilated with HoYoverse and is a creator's own represantation."
     #"This story is mostly based on theories, hypotheses and assumptions made by fans and in no way is canon to his original story in Genshin Impact, whether it's his past, present or possible future."
     #"Thus, it contains spoilers for Kaeya's character story both in-game and manhua which you can read on {a=https://genshin.hoyoverse.com/en/manga}website{/a}."
     #"The next warnings might contain spoilers. Would you like to see them spoiler-free or not?"

#     menu:

#        "Yes":

#         jump spoiler_yes

#        "No":

#         jump spoiler_no

#     label spoiler_yes:

#     "The game also contains graphic depictions of suicide, alcoholism, anxiety, abandonment, murder, gore, death, depression, loneliness, military conflicts, PTSD and suggestive themes."

#     "Full list of warnings can be viewed here: 222.vn"

#     "People easily triggered by any of these may not have a safe experience playing the game."

#     jump ps

#     label spoiler_no:

#     "This game contains mature topics not suitable for children or easily disturbed. They may not have a safe experience playing the game."

#     label ps:

#     "Please, don't take it lightly, as despite being a work of fiction, the game uncovers its topics as realistically as possible, which might be not comfortable for certain individuals."

     "By playing [config.name] you agree that you have friendship level 6 Kaeya, at least 13 years old and consent to any spoilers and highly disturbing content contained within."

     menu:

        "I agree.":

         pass

     show img_warning2 with Dissolve (2.5)

     pause 1.0

     show warning_img3 with Dissolve (1.0)

     show warning_img4 with Dissolve (1.0)

     show warning_img5 with Dissolve (1.0)

     show warning_img6 with Dissolve (1.0)

     show warning_img7 with Dissolve (1.0)

     show warning_img8 with Dissolve (1.0)

     show warning_img9 with Dissolve (0.4)

     show warning_img10 with Dissolve (0.4)

     show warning_img11 with Dissolve (0.4)

     show warning_img12 with Dissolve (0.4)

     show warning_img13 with Dissolve (0.4)

     show warning_img14 with Dissolve (0.4)

     show warning_img15 with Dissolve (1.5)

     scene white with dissolve

     $ persistent.first_run = True

     jump before_main_menu

     label before_main_menu:

     show text "Original fan-game by mlka" with dissolve:
         xalign 0.5
         yalign 0.5

     pause 2

     hide text with dissolve

     if renpy.random.randint(0, 3) == 0:
         show text "[splash_messages]" with dissolve:
             xalign 0.5
             yalign 0.5
     else:

         show text "This game is an unofficial fan work unaffiliated with HoYoverse" with dissolve:
             xalign 0.5
             yalign 0.5

     pause 3

     hide text with dissolve

     return
