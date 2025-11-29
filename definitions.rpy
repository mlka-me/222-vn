 #Explanation for Definitions:
 #This section defines stuff for the game, including sprites for our boi, backgrounds, etc.
define config.developer = True
#Turn off this function when released
init python:
    renpy.music.register_channel("ambience", loop=True, mixer ="ambience")
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass
#Code from the file script-ch30.rpy, Doki Doki Literature Club. This code will be temporarily used for troubleshooting some files.
#Fun fact: initially, this code was planed to be used for getting Traveller's name from Genshin Impact, known from the "leaks"
#under the variable {NICKNAME}. However, it was scrapped in the process (for obvious reasons)
#Actually, it's a funny bug in Scions of the Canopy Tribal Chronicles.
#https://www.reddit.com/r/Genshin_Impact/comments/1fixvu0/ah_yes_it_is_i_mr_nickname/

   ##DO NOT UNCOMMENT IF YOU ARE NOT SURE!!!!!!!!!!!!!
   ## If you're an experienced Python coder (not a poor self-taught like me),
   ## then I wish you all the best trying to integrate this type of stuff
   ## while fighting with countless errors and tracebacks.
   #define config.mouse = ()

   #define config.mouse = mouse{ ("pointer", 0,0) }

   #define config.mouse = mouse("match", 0,32)


   #images:

image black = "#000"

image dark = "#000000e4"

image darkred = "#110000c8"

image white = "#ffffff"

   #complex images:

screen lantern1():

    imagebutton:

        xalign 0.812 ypos 0.597
        idle "lantern_bw"
        hover "lantern_off"
        action Jump ("intr")

#screen lantern2():

#    imagebutton:

#        xalign 0.87 ypos 0.58
#        idle "lantern_bw"
#        hover "lantern_off"
#        action Jump ("exit")

$renpy.transition(dissolve, layer="master")

image static:

    "static3" with Dissolve(0.2)
    0.2
    "static4" with Dissolve(0.2)
    0.2
    repeat

image bg_night:

    "bg_h_night1"
    0.2
    "bg_h_night3"
    0.2
    "bg_h_night2"
    0.2
    "bg_h_night3"
    0.2
    repeat


#characters:

define k = Character(_("Kaeya"), what_xalign=0.5, what_textalign=0.5)

define k1 = Character("???", what_xalign=0.5, what_textalign=0.5)

define k2 = Character("kaeya", font="Gsenochian.ttf", what_xalign=0.5)

define klee = Character(_("Klee"), what_xalign=0.5, what_textalign=0.5)

define n = Character(_("Nymph"), what_xalign=0.5, what_textalign=0.5)

define t = Character ("[traveler]", what_xalign=0.5, what_textalign=0.5)

define sh = Character (_("A mysterious voice"), what_xalign=0.5, what_textalign=0.5)

define sh1 = Character (_("A Deity"), what_xalign=0.5, what_textalign=0.5)

define scn = Character (what_italic=True)
#Meet a self-concious narrator!

#For the future:

define adl = Character (_("Adelinde"), what_xalign=0.5, what_textalign=0.5)

define abysl = Character("???", what_xalign=0.5, what_textalign=0.5)

define b = Character (_("Barbara"), what_xalign=0.5, what_textalign=0.5)

define d = Character (_("Diluc"), what_xalign=0.5, what_textalign=0.5)

define j = Character (_("Jean"), what_xalign=0.5, what_textalign=0.5)

#in-game stuff:
#Point system
#In the game there will be 2 point systems and they will reflect the ending you'll get!
#Affection points indicate your rizz strength towards Kaeya (aka how romantically he is attracted to you). Can be grinded through
#different activities in the interaction mode (except Talk Topics unlocked through the story)
#Trust points indicate how much Kaeya trusts you. Can be maxed via choosing the right choices in the main plot + Realm of
#Consciousness events, as well as certain Talk Topics
#While affection points are important, trust points are even more important, as maximizing them is NECCESSARY for BOTH happy
#endings!
#To reach Friendship ending, you need to max ONLY kaeya_tp
#To reach Romance ending, you need to max BOTH kaeya_tp and kaeya_afp
default kaeya_afp = 0

define min_kaeya_afp = -10000
#There will be no way to reach negative affection, except Game Over
define max_kaeya_afp = 10000

default kaeya_tp = 0
#For later versions include Trust Points (IMPORTANT)

style abyss_text:
    color "#db03fc"
    font "Gsenochian.ttf"
    outlines [ (2, "#eaa2fc", 0, 0) ]

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

   #endings:
#Have in mind, there is no true end, as it depends on your perceptioon of Kaeya and Traveler's relationship
#(whether you see them as friends or romantic partners)
define end_rom = False
   #aka Happy End (romance)
define end_bad_s = False
   #aka Suicide End
define end_bad_o = False
   #aka Overdose End
define end_fr = False
    #aka Happy End (friendship)
define end = False
   #aka Romeo and Juliette end
define loop = False
   #the scariest ending ever!
define gameover = False
   #self-explainatory
   #Warning: SYF (SAVE your files!)
#layeredimage kaeya:
 #TODO: uncomment when Kaeya's sprites are done
    #always "k_base"

    #group head auto:

    #    attribute head default

    #    attribute head1

    #group clothes auto:

    #    attribute shirt default

    #    attribute fur default

    #group eye auto:

         #attribute open default
     #attribute blinking:

         #"blinking"
#    group eyebrows auto:

#        attribute 3 default

#        attribute 2

#        attribute 1

     #group mouth auto:

         #attribute smile default
     #group emotion auto
