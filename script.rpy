#Must it be from the 2nd person or from the 1st?
init python:

    import random

    import datetime

label start:

    python:
     traveler = renpy.input("From that moment you will be known as...", length = 20, allow = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝßàáâãäåçèéêëìíîïðñòóôõöøùúûüýÿĀāĂăĄąĆćĈĉĦċČčĎďĐĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪġĬĭĮįİıĲĳĴĵķĸĹĺĻļĽľĿŀŁłŃńŅŇňŉŊŋŌōŎŏŐőŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž")

     traveler = traveler.strip() or __("traveler")

    pause 2

    play music crickets

    $ renpy.music.set_volume(0.2)

    play sound footsteps

    t "(As far as I remember it must be...)"

    t "(Here! *sigh* I hope this is the right address.)"

    play sound knock

    pause 1.5

    t "Is anyone here?"

    $ renpy.music.set_volume(0.5)

    pause 3

    $ renpy.music.set_volume(0.2)

    play sound creak

    "Instead, a door opens creaking as if it invited you to go inside. The first thing you meet as you step into the place is a mist of silence."

    play sound heartbeat

    t "{i}What if it didn't work? What if everyone...{/i}"

    #stop sound heartbeat

    "However, your thoughts are quickly washed away as you try to fly forward. Led by ornaments, you come closer to the table, a lantern and matches lying on it."

    "As you try to reach for a match, however, your entire body shakes as you feel a warm breath with a barely perceptible smell of alcohol."

    t "Ah, so there IS someone alive? Are they alright? Do they need help?"

    t "There's only one way to find out!"

    $ default_mouse = "match"

    call screen lantern1

    label intr:

    $ default_mouse = "pointer"

    stop music fadeout 1

    show bg_night

    show kn2

    with flashbulb

    pause 0.5

    t "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-!{nw}"

    t "What are you doing here, Kaeya? You scared me to death!"

    hide kn2

    show kn

    k "And I thought you were hard to surprise!{w=0.5} Ha-ha,{w=0.25} turns out you are still afraid of unexpected surprises,{w=0.5} right?"

    t "Straight to details, Kaeya!"

    hide kn

    show kn2

    k "Then let me ask you first."

    hide kn2

    show kn3
    # questioned Kaeya
    k "What made you come here, [traveler]?{w=0.5} To me?{w=1.0} Alone and in the darkness of night?{w=1} You had to be looking for a sibling on your journey as I remember."

    menu:

       "Instead, the fate decided to return to you":

         $ kaeya_afp +=5

         hide kn3

         show knb3
         # wondering blushing Kaeya
         k "(Ah?{w=1} Seriously?)"

         k "(How could [traveler] remember me through all their journey?)"

         k "(I thought they had already forgotten me.{w=0.5} I thought I was useless because of being a starter character.)"

         hide knb3

         show knb2

         k "(But somehow they did manage to remember me whenever they are.)"

         k "(I don't know how to describe the feeling exactly,{w=0.25} but it feels{w=1.0}...nice?)"

         hide knb2

         show kn3
         # thinking Kaeya
         k "(But wait...{w=1.5}Something's off...)"

         jump intr1

       "But as the Archons don't help at all distracting with their work I decided to go back to ask you instead":
         #Note: The script has been being written since Inazuma release, so that's why it contains such phrases.
         show kn
         # wondered Kaeya
         k "Me? O-ho-ho, quite an interesting choice on your side."
         menu:

            "I've heard you know about some 'Leader of the Abyss', haven't I?":

             pass

         k "(Whoa, whoa, wait! It's too early to ask about this!)"
         #even if you told them such information

         k "Ah, the Prince?"

         k "Ha-ha, the thing is{w=0.25} if such conversation happened in the original game{w=0.25} then the developers wouldn't let us interact.{w=0.5} What a shame!"

         k "But I promise I will tell you everything as the time comes.{w=0.5} Who knows maybe you'll learn some of my secrets as well?"

    label intr1:

     hide kn3

     hide kn

     show kn2
     # serious Kaeya
     k "Wait...{w=1.5} I feel something has changed{w=0.25} and you might be the reason for it."

     show static with {"master": Dissolve (10.0)}

     play sound sound_glitch
     # wondered Kaeya
     k "{cps=25}Haven't you somehow...{w=1.5} {i}altered{/i} the world recently, [traveler]?{w=0.5} Or...{w=0.5} May I call you...{/cps=25}"

     menu:

        "Lumine":

         pass

     hide static

     k "But even if you have your own name,{w=0.5} you still have as many secrets as I do, right?"

     k "{cps=25}And don't even dare to lie with your innocent appearance.{/cps=25}{w=0.5} Having angelic blonde hair and amber eyes doesn't make you look exactly the same in your world,{w=0.5} does it?"

     k "And as unfortunately I can neither see you nor imagine,{w=0.5} I would like you to describe yourself."

     k "First,{w=0.25} let's begin from the soul.{nw}"

     t "Kaeya! But you promised!{nw}"

     # show kaeya happy

     play music music_night1 fadein 2

     k "Ha-ha,{w=0.25} sorry,{w=0.25} I'm just kidding."

     #show kaeya

     k "Although it's just a joke, but not for nothing eyes are called {a=https://www.phrases.org.uk/bulletin_board/31/messages/1165.html#:~:text=EYES%%20ARE%%20THE%%20MIRROR%%20(MIRRORS,to%%20'Regiment%%20of%%20Life'%%20.}'Mirrors of the Soul'{/a}."
     #I still don't know how to make it look normal in auto ToT
     #Also, I will probably
     k "Earlier this expression used to be a part of Cicero's quote 'Ut imago est amini voltus sic indices oculi'.{w=0.5} It means 'The face is a picture of the mind{w=0.25} as the eyes are its interpreter'."

     k "In the world of Teyvat they play a role even greater than you imagine."

     k "Eyes can literally express the personality of the character.{w=0.5} Except for those united with blood you will never find two people with the same eye color."

     k "But even if they do,{w=0.5} you will never confuse them{w=0.25} and it's all thanks to pupils and eye form."

     k "Big rounded eyes can often express a carefree,{w=0.5} outgoing{w=0.5} and cute character.{w=0.5} Whereas almost closed looking ones show us some kind of serious and mysterious one."

     k "My eyes have a secret as well...{w=2} And what about you, [traveler]?"

     window hide

     with dissolve

     menu:

       "They look like Cider Lake on a cloudy day":

         $ kaeya_afp +=10

         jump grey

       "My eyes are as blue as the sky":

         $ kaeya_afp +=10

         $ eyes_blue = True
         $ eyes_red = False
         $ eyes_cyan = False
         $ eyes_green = False
         $ eyes_hazel = False

         jump blue

       "They are as cyan as the waves of the sea":

         $ kaeya_afp +=10

         $ eyes_blue = False
         $ eyes_red = False
         $ eyes_cyan = True
         $ eyes_green = False
         $ eyes_hazel = False
         jump cyan

       "They share the color of the most beautiful emerald":

         $ kaeya_afp +=10

         $ eyes_green = True
         $ eyes_red = False
         $ eyes_blue = False
         $ eyes_cyan = False
         $ eyes_hazel = False

         jump emerald

       "They will remind you afternoons when you were walking in the woods":

         $ kaeya_afp +=10

         $ eyes_hazel = True
         $ eyes_red = False
         $ eyes_blue = False
         $ eyes_cyan = False
         $ eyes_green = False

         jump hazel

       "They are as dark and deep as the ocean":

         $ kaeya_afp +=10

         jump dark

       "They look like two different gems shining in the light of sun":

         $ kaeya_afp +=10

         jump heterochromia

       "They are like scarlet roses in the garden":

         $ kaeya_afp +=10

         $ eyes_red = True
         $ eyes_blue = False
         $ eyes_cyan = False
         $ eyes_green = False
         $ eyes_hazel = False
         jump red

     label grey:

     k "Oh, that's...{w=2} interesting."

     menu:

        "Ah? What do you find interesting in grey eyes?":

         pass

     k "Ha-ha-ha, you must be right.{w=0.5} Grey eyes are boring alone as the element of Anemo."

     k "At least this is the first impression.{w=0.5} But be fooled not, as the real gem is hidden deep and dark."

     k "As Anemo swirls with Cryo,{w=0.375} Pyro,{w=0.375} Hydro{w=0.375} and Electro,{w=0.375} grey eyes may infuse with other eye colors, as well..."

     k "...and thus make the uniqueness appear out of nowhere."

     k "From the color as pure as ice to the one as festive as champagne, mixed grey eyes dazzle with diversity of shades and hues."

     #show kaeya happy

     k "So, don't judge a book by its cover!"

     jump hair

     label blue:

     #show kaeya wondered blush

     k "Oh, those eyes of blue, so often described in love novels and poems!{w=0.5} I can definitely say you've got the most beautiful eyes in the world!"

     k "Moreover, it is proven that blue is favored by most people, so no wonder such eyes would be considered one of the most beautiful."
     #Proof
     #https://today.yougov.com/international/articles/12335-why-blue-worlds-favorite-color

     k "As a color, it shines with a variety of shades, like, for example...{w=1.5} If you didn't know the shade of my eyes,{w=0.25} which color would come first to your mind?"

     menu:

         "Blue, of course!":

             k "You are absolutely right!"

             jump expl

         "Violet, I think.":
            #Hey, why didn't you write purple?
            #Here is the explanation: https://www.quora.com/What-is-the-difference-between-violet-and-purple
            k "This one is very interesting to listen to,{w=0.5} but here is one thing."

     label expl:

     k "Although periwinkle is a mix of violet and blue, this shade has more blue in it.{w=0.5} That's why a lot of people would describe and see my eyes as blue."
     #Another explanation of what Kaeya just said:
     #https://www.homedit.com/periwinkle-color/#:~:text=older%20kids'%20rooms.-,What%20Is%20The%20Difference%20Between%20Periwinkle%20And%20Lavender%3F,as%20both%20purple%20and%20blue.

     k "And next time don't be shy to pick something more complex to describe a blue color.{w=0.5} It does have a lot of sides, after all~"

     jump hair

     label cyan:

     k "O-ho-ho,{w=0.5} want me to take you to the sea?~"

     k "He-he, interesting idea, I'll need to think about it one day.{w=0.5} No promise I would grant your wish, though."

     k "Wait a minute...{w=0.5} you reminded me of some legendary place described in one book."

     k "Heard of Dandelion Sea?"

     menu:

        "Yes, I read about it in one book":

          jump book_yes

        "No, never":

         jump book_no

     label book_yes:

     k "Does 'The Fox in the Dandelion Sea' happen to be that book?"

     t "Yeah, the same one!"

     k "May I ask you one more question, [traveler]? Do you think Dandelion Sea exists?"

     menu:

        "Yes":

         k "I have the same suspicions as you, to be honest, though sometimes just suspicions might not be enough."

         jump hair

        "No":

         k "Fine with me! It's just a place from a book, after all."

         jump hair

     label book_no:

     k "From what I've heard it's a place full of dandelions and foxes. One hunter wanted just to eat, but then learned much more after saving a white fox."

     k "Read it in 'The Fox in the Dandelion Sea', if you have a chance."

     jump hair

     label emerald:

     k "Though this color is commonly considered rare,{w=0.25} but I have seen at least three people with such eyes, which might be too much for such a small town as Mondstadt."

     k "Lisa,{w=0.5} Fischl,{w=0.5} Noelle,{w=0.5} Bennet...{w=0.5} doesn't it seem to be mysterious?{w=1} Mona would also fall in that category."

     k "Ah,{w=0.25} I forgot it's not your world where people could burn others for their eye color.{w=0.5} At least from what I heard."

     menu:

        "They really used to do it because of beliefs. Thanks goodness, times have changed.":

         pass

     stop music

     k "Then this is true...{w=2} At least we don't practice this in Teyvat."

     k "However, things here are much scarier than in your world,{w=0.5} so my advice is to be careful."

     hide kn

     hide bg_night

     window hide

     pause 5

     window show

     with dissolve

     k2 "{=abyss_text}caelestia te spectat{/=abyss_text}{p=5}"
     #Note: if you want to write something in Abyss, don't write with capital letters or glitches will appear.
     #Fun fact: The phrase means "Celestia is watching you!" and is put as random message on the splash screen.
     k "Sorry,{w=0.25} I don't even know what came over me.{w=0.5} Did I scare you?"

     k "If so,{w=0.5} then I'm truly sorry."

     show bg_night

     show kn

     play music music_night1

     jump hair

     label hazel:

     k "..."

     k "Don't worry,{w=0.5} I'm just impressed by the way you described it."

     k "Frankly,{w=0.25} I kind of wish to have the same worldview as you."

     menu:

        "It seems quite usual, he-he...":

         pass

     k "Quite usual, huh?{w=0.5} Do you...{w=0.5} actually know a lot of people feel kind of...{w=0.5} jealous right now?"

     menu:

        "But why? I'm not a superhero or anything, so there's nothing unusual!":

         pass

     k "Ironically,{w=0.5} it is your superpower.{w=0.5} You're the first person I've met to have such intentions."

     k "The thing is...{w=0.5} a lot of people are often obsessed with the idea of having a Vision.{w=0.5} As not many actually have it, they have built their beliefs like it can make you strong,{w=0.5} powerful{w=0.5} and gain respect towards others."

     menu:

        "I see... it's like getting famous and rich, isn't it?":

         pass

     k "Right on spot!{w=1} And though the wish is common, the reasons and obstacles...{w=2} I can't say the same for them."

     k "From innocent intentions such as a good deed to deep or even tragic ones...{w=2}And unlike being famous gods won't react at all if you have a sinister wish to show off."
     #unless you prove it yourselves as I've never seen or heard about such human beings.
     k "Huh...{w=0.5}I wish people could understand how it feels living with a Vision.{w=0.5} They would feel much happier if they learnt how to appreciate even the smallest things."

     jump hair

     label dark:

     k "(Dark as the night sky and deep as the Abyss...{w=2} Is this the way you are?{w=0.5} Or the way you appear to be?)"

     k "Seems you've brought some secrets with yourself,{w=0.5} haven't you?"

     k "Just for you to know.{w=0.5} People like you often catch my interest just for being mysterious."

     k "So, remember{w=0.5} I will be watching you."

     jump hair

     label heterochromia:

     k "So,{w=0.5} you have heterochromia, huh?{w=0.5} I've heard it is a very rare phenomenon in your world."

     k "But{w=0.25} what I didn't know however is that it's so rare in Teyvat,{w=0.5} where the elemental power flows in both air and soils,{w=0.25} that even know-it-alls{w=0.25} such as me are not familiar with those."

     menu:

        "I've heard you have heterochromia as well":

         pass

     k "Me?{w=0.5} You must be leaping to conclusions, [traveler].{w=0.5} What made you think *I* have heterochromia in the first place?"

     menu:

        "He-he, e-e-eh... w-well, I just wanted to know what's under your eyepatch, a-and...":
         #Who hasn't done that?
         pass

     k "{cps=25}Tsk-tsk,{w=0.25} such inappropriate behavior!{w=0.5} I see you're brave enough to dig inside one's secrets just for fulfilling your thirst,{w=0.5} aren't you?{/cps=25}"

     k "In that case...{w=1.5} How about we make a deal?"

     menu:

        "A deal?":

         pass

     k "M-hm,{w=0.5} when I trust you enough{w=0.5} I'll spoil you bit by bit with information about myself to feed your ever-hungry curiosity.{w=0.5} On your side,{w=0.5} promise not to spread or tell anyone..."

     k "Or else it will become the least of your worries."

     menu:

        "Alright then, a deal":

         pass

     jump hair

     label red:

     k "Y-your eyes are scaringly beautiful, as I see."

     menu:

        "Kaeya???":

         pass

     k "Ah, never mind. Just got lost in myself."

     label hair:

     window hide

     pause 2

     window show

     with dissolve

     k "And now I would like to know one more thing about you."

     k "You see,{w=0.25} if you don't want for all the secrets to be revealed through your eyes, then you can just hide them under colorful bangs.{w=0.5} Simple,{w=0.25} isn't it?"

     k "Doing such a thing, people can always turn to who they want to seem.{w=0.5} And reading hairstyles can help you learn a lot about them."

     k "Do they seem to be perfectionists,{w=0.25} strict and tidy at first?{w=0.5} Or brave and confident?{w=0.25} After all,{w=0.25} your hair can reveal as many things as your eyes."

     k "So, I wonder what your hair's like?"

     menu:

        "It's as colorful as a dawn":

         $ kaeya_afp +=10

         jump hair_red

        "It's 'the brightest Sun that's ever Sunned'!":
         #Don't google it, pwetty pwease!
         #Ah, never mind... if you know, you know
         #https://x.com/JoseyMcCoy/status/1534588128593252352
          $ kaeya_afp +=10

          jump hair_lightblonde

        "It will remind you a walk in wheat fields":

          $ kaeya_afp +=10

          jump hair_blonde
         #Interesting (not) fact: Blond is for boys, blonde is for girls.
        "It'a akin to a morning coffee with milk":

          $ kaeya_afp +=10

          jump hair_lightbrown

        "It's grey-ny!":

         $ kaeya_afp +=10

         jump hair_grey

        "It tastes like chocolate":

         $ kaeya_afp +=10

         jump hair_chestnut

        "It's as mysterious as night":

         $ kaeya_afp +=10

         jump hair_black

        "It's of colors of the rainbow":

          $ kaeya_afp +=10

          jump hair_colorful

#Beware!
#The next area is known as if-elif-else field, so the code will be a little bit messy here.
#How it works:
#1. We choose any eye color
#2. If that eye color is within if/elif, Kaeya will say who we resemble
#3. Otherwise, he will say lines under "else"
#The information about characters' hair color is brought straight from the wiki (except me, of course~)

    label hair_red:
     #Can be both about bright red hair and "ginger" hair
     if eyes_red:

         k "Do you also happen to inherit a hairstyle or two from your parents?{w=0.5} Or do you happen to live in the world of your own?"

         k "I'm joking, of course! You are definitely not like that, aren't you?"

         jump dayend

     else:

         k "What a beautiful way to describe such a rare color! I can already imagine the Sun rays on your hair!"

         jump dayend

    label hair_lightblonde:

     if eyes_red:

         k "You remind me of... the Spark Knight!"

         k "Brighter than the Sun, she emits lots of energy, even though sometimes it may disturb the peace of Mondstadt."

         k "As for what she's doing, 'Fun stuff', she says. 'Throwing bombs, blasting fish...'"

         k "Her parents are far away, so she's got no one to babysit her... except of Knights of Favonius. And a 'weird grown up', he-he."

         menu:

            "What are you laughing at?":

             pass

         k "Never mind."

         k "Anyway, that's how I came up with a set of rules for Klee..."
         #Sorry, there won't be CG for a while
         #The beginning of CG
         klee "'Explosion inside city wall, grounded be thy woe'"

         klee "'Explosions can hurt people, Jean can be dreadful'"

         klee "'Mondstadt be bombed, Klee be doomed'"
         #Cici, we need your help here! Was it meant to be "rhymed" in Chinese?
         k "These survival rules are for you, Klee! Don't break these rules or something terrible will happen!"

         klee "Alright, I will try my best! Thank you, Kaeya!"
         #The end of CG
         k "I hope she will not be trapped to the confinement room again... eh, poor Klee!"

         jump dayend

     elif eyes_cyan:
     #Straight from my memory (2023)~
         k "Everyone praises Albedo for his abilities.{w=0.5} But there is one interesting thing which no one told you."

         k "Did you know that Albedo had his counterpart in your world?"

         k "As a usual human they made mistakes,{w=0.5} but the difference is that they had an influence on the whole kingdom.{w=0.5} And as usual human, they had hobbies as well."

         k "Today's story will be about that.{w=0.5} So, come here and listen."

         k "There was a beautiful castle standing on the bank of the Vistula River.{w=0.5} It was called Wawel Castle and for a long time it used to be a residence for many royal families."

         k "But one year everything changed during one king's stay."

         k "His name was Sigismund III Vasa, a gifted painter and an incredibly talented alchemist who tried to find the mystery of Philosopher's Stone."

         t "Hm-m, I see where you are going."

         k "And one day one of his experiments caused a great fire."

         k "Some say that he didn't restore the castle while others suggest the opposite. However, that doesn't matter as long as it has become one of the reasons for moving the capital from Kraków to Warsaw."

         k "I feel he'd have a lot of interesting conversations with Albedo, don't you think?"

         jump dayend

     else:

         k "I wonder how you could come up with such a funny joke..."

         k "Anyway, I feel I would have been blinded, had I seen your hair."

         jump dayend

    label hair_blonde:

     if eyes_blue:

         k "Go Barbara go!"
         #Guess the reference! again...
         #https://youtu.be/yeeYROGwEII?t=2597
         menu:

            "Absolute cinema!":

             pass

         k "Ha-ha, I'm just joking.{w=0.5} In fact, I wonder how her sister Jean is doing given the amount of work she has to do as acting grandmaster."

         k "I've witnessed her constantly working hard, even overworking herself for the sake of Mondstadt being a better place. Every request, no matter how small it may be, is handled with Jean's perfection."

         menu:

            "Then why won't you give these tasks to Noelle?":

             pass

         k "It's a great idea! I think I must report it to Jean! Even though Noelle is not a knight yet, I think small commissions should be for her."

         menu:

            "So, I guess that's why you are Jean's trusted knight...":

             pass

         jump dayend

     elif eyes_hazel:

         k "So you DO look like Traveler in real life!"

         k "I'm sorry for accusing you earlier. I shouldn't have jumped to conclusions!"

         menu:

            "It's alright! I forgive you, Kaeya":

             pass

         k "Thank you, [traveler]!"

         jump dayend

     else:

         k "Oh... when you described it, I suddenly felt a breeze coming in."

         k "I remembered those beautiful, happy days in Mondstadt when Diluc and I used to collect seashells on the beach. "

         k "Eh... I wish I could return those times back."

         jump dayend

    label hair_lightbrown:
     #TODO: I feel there needs to be more text
     if eyes_green:

         k "Lisa, ah..."

         k "Legends are spreading everywhere about her power...{w=0.5} yet no one witnessed it.{w=0.5} Except me, of course!"

         menu:

            "You? But how?":

             pass

         k "Lisa's title as 'the best student in 200 years' couldn't help but pass through my ears, and so I had a small idea for the Grandmaster:"

         k "'How about a training combat session between Nymph and this novice from Sumeru?'"

         k "Varka accepted my idea.{w=0.5} Meanwhile Nymph...{w=0.5} laughed at such a possibility."

         n "This nerd from Sumeru? Against me?"

         k "Her reason for laugh was understandable.{w=0.5} Nymph was a quite strong mage,{w=0.5} so fighting her even as a joke was already dangerous."

         k "Nevertheless,{w=0.25} Lisa accepted my idea and few days later everything was ready for the battle."

         menu:

            "And how was it?":
             pass

         k "That was a spectacular performance!{w=0.5} I had the chance to see Lisa's powers in bloom.{w=0.5} But two minutes in, Lisa told us she doesn't want to be a Captain."

         k "Ironically enough, Nymph started sending tons of letters to Grandmaster with requests to make Lisa the Captain."
     #Thanks to this post, btw!
     #https://www.reddit.com/r/KaeyaMains/comments/1c5pl74/after_kaeya_replaced_diluc_as_calvary_captain_he/
         jump dayend

     else:

         k "The smell of fresh morning coffee... what a perfect way to start the day!"

         k "Your head must have fresh and cool ideas to share with everyone!"

         jump dayend

    label hair_grey:

     if eyes_red:

         k "Ha-ha, I wonder who could teach you such a funny joke!{w=0.5} Could it be your deer friend from Sumeru, buy any chance?"

         menu:

            "X-actly! Do you want won more joke?":

             pass

         k "How could I Cyno 2u~?"

         t "*clears her throat*"

         t "I've heard you've been pretty popular with Reyvateils lately."

         k "And people say my charm is fake!{w=0.5} Anyway, what they've been up to?"
         #A little bit of being silly will not be too much (I hope)
         t "He-he, they've been constantly asking you about something."

         k "Asking? {w=0.5}What's that?"

         window hide

         pause 2

         window show

         with dissolve

         play sound badumtss

         t "Kaeya, give me a present!"
         #aquagon will kill me for the joke X_X (save me please)
         k "Give you... a present?"

         k "{cps=25}I didn't know you were such a...{w=1.5} joker!{/cps}"

         t "Seems no one will get the joke, even Cyno."

         scn "Psst..."

         scn "Sorry to interrupt, but seems our Traveler heard the phrase wrong. There is no such phrase in Hymmnos, a language used by Reyvateils and people alike on Ar Ciel."

         scn "Instead, what Traveler might have heard was {font=hymmnos.ttf}Rrha yea ra hymme meo clemezen{/font}. You can learn more about this phrase {a=https://youtu.be/NDtO2rMv6QY?t=293}here{/a} or {a=https://hymmnoserver.uguu.ca/search.php?word=Rrha+yea+ra+hymme+meo+clemezen}here{/a}"

         scn "Uh-uh, Professor will probably cook me for it, so Cyn-ing out! ^_*"
         #And I'm also sorry for writing Cyno instead of Razor, cuz I happen to have moar Cyno jokes!
         jump dayend

     else:

         k "..."

         k "Aha, so, you combined grey and rainy to get this word?"

         k "Ha-ha, well done, [traveler]!"

         jump dayend

    label hair_chestnut:

     if eyes_blue:

         k "If I had a nickel for every person with such features, I'd have two nickels.{w=0.5} Which isn't a lot, but might seem surprising it happened twice."
         #Surprised Kaeya
         k "The first one is my{w=0.5}...voice donor?{w=0.5} Is that how you call such people?"

         menu:

            "Ha-ha, Kaeya, we call them voice actors!":

             pass

         k "I'm blessed to have his voice!{w=0.5} From what I've heard, I would have have a great time with him as we both share a lot"

         k "As for the second one..."

         k "She is an active guest in Teyvat.{w=0.5} We used to explore a lot together taking photos of landscapes from Mondstadt to Natlan."

         k "Ah, those were good times..."

         k "I was one of the first characters to get to the level 90,{w=0.5} Friendship level 10,{w=0.5} and be tripled crowned,{w=0.5} though the latter happened much, much later.{w=0.5} And it's not speaking about artifacts and gear!"

         k "I was also the first to live in several teapots, where we shared stories of our adventures.{w=0.5} The more Friendship Levels were unlocked, the more I was willing to tell her stories of myself."

         k "She didn't mind and so, told her stories.{w=0.5} Some were funny, and some were sad.{w=0.5} She also kept talking about her dream{w=0.5} - to find a certain person."

         k "No,{w=0.5} it was not brother, as some could think, but her friend, who she hasn't seen{w=1.0}... for ages."

         k "As New Year was coming, she finally had a chance to reunite with her friend!{w=0.5} But she forgot one more thing:"

         k "'Can we still be friends even despite what I'm about to tell?' {w=0.5}- was the question she forgot to ask.{w=0.5} Up to this day she still blames herself for being a coward..."
         window hide

         pause 3

         window show

         with dissolve

         k "If you want me to tell some facts about the developer (and her shenanigans), be free to include that in feedback!"

         jump dayend

     elif eyes_hazel:
     #Even though her eyes are stated to be amber, hazel eyes seem to be the closest to amber, I imagine... unless, you wanna change it!
         k "A clever and courageous knight, Amber is a model for justice. Nothing would stop her: neither difficulties she had in the Knights of Favonius, nor a horde of hilichurls."

         k "Even if she is the only outrider in the Knights of Favonius, she always does her work well."

         k "That's what I like about her."

         jump dayend

     else:

         k "Suddenly, I also want chocolate! Can you share a bar with me, please?"

         menu:

            "Silly Kaeya! I can't do it through the screen!":

             pass

         jump dayend

    label hair_black:

         k "You seem to bury some secrets within yourself, don't you?"

         jump dayend

    label hair_colorful:

     if eyes_blue:
         #there should have been an excited Kaeya
         k "Hey! Are you just like... me?"

         menu:

            "I'm just like you":

             pass

         k "That's something anyone can see! Do you deceive? And do you lie just to hide your scars?"

         k "Or... do you perhaps know about the mechanic and decided to learn about my reaction?"

         k "Alright, alright, it seems I have some lookalikes, he-he."

         jump dayend

     else:

         k "Wow, I've never seen such a beautiful hair! You would make a perfect vision holder."

         menu:

            "Me? Ha-ha, I'm not sure":

             pass


         k "Not sure? Why?"

         menu:

            "Unfortunately, people in real world are not born with such beautiful hair. They dye it":

             pass

         k "Dye it? Like we would paint walls? What an interesting technology. But I still wonder why they do it."

         menu:

            "They do it for many reasons, but mostly to stand out of the crowd":

             pass

         k "If we follow that logic, vision holders also stand out of the crowd. So, at least you would have the same spirit."

         jump dayend

    label dayend:

     window hide

     pause 3

     window show

     with dissolve

     k "Phew, {w=0.5}that's all I needed to know [traveler]."

     k "First impression is important of course, but...{nw}"
     #it was meant to be "first impression is important of course, but it doesn't represent your whole personality"

     stop music

     window hide

     show layer master:

         blur 10

     scene black

     with Dissolve (1.5)

     window show

     t "Z-z-z... Z-z-z...Z-z-z..."

     k "Ah?{w=0.5} [traveler]?{w=0.5} Are you alright?"

     k "[traveler]?"

     show bg_night

     show kn

     with dissolve

     "I've been quickly woken up by the unusually worried tone of Kaeya's voice."

     t "Ah? Sorry for worrying. *yawn* I'm a little bit tired."

     k "('Curiosity killed the cat', they say.{w=0.5} Instead,{w=0.5} I have almost killed [traveler] with my own curiosity.{w=0.5} Who am I even at that point?)"

     k "Oh, sorry,{w=0.5} I shouldn't have bombarded you with a bunch of questions.{w=0.5} Let's go find a place to rest. I suppose you need it the most now, don't you agree?"

     "I nodded in agreement. A beauty sleep was exactly what I needed after an exhausting journey."

     hide kn

     show layer master:

         blur 10

     with dissolve

     "You both got up. Kaeya leads you to the bedroom, so you could not fall on the floor at any moment. Your legs hurt and your mind got too blurry and foggy to remember the way. "

     k "Here we are."

     "Kaeya easily opens the door for you to enter the bedroom."

     k "Alright then, have a rest, [traveler].{w=0.5} Goodnight."

     "Soon you don't notice as you fall asleep in your travelling outfit..."
     #CONCEPT: Initially, the next segment is meant to be a tutorial (with some lore) described in dialogue pop-up windows.

     scene black with dissolve

     window hide

     play ambience wind

     sh "E-ler..."

     t "(My first night here and I already hear strange voices. Nice...)"

     sh "E-veler..."

     t "(Was the trip THAT tiring? I know my every journey is, but never in my life have I had such side effects!)"

     sh "Traveler..."

     show goddess1 with flashbulb

     sh1 "The winds sense you are anxious. Is there something that troubles you?"

     t "What if it's not real? What if it turns out to be a dream inside of a dream?"

     sh1 "Your reasons for concern do seem valid, [traveler]. However, remember one and only thing:"

     sh1 "You can always end the story the way you want!"

     sh1 "So, to stop this nightmare once and for all please accept this gift of Thousand Winds! It will give you power to rewrite fate."

     sh1 "Travel to Mondstadt, save its people and change the direction of the winds!"

     hide goddess1 with dissolve

     show text "Through long-forgotten winds have my memories returned" with dissolve:
         xalign 0.5
         yalign 0.4

     pause 2

     show text "Through long-forgotten winds, however, I've heard a sorrow song:" with dissolve:
          xalign 0.5
          yalign 0.5

     pause 2

     show text "'What used to be a land of freedom, is now a land of waste." with dissolve:
          xalign 0.5
          yalign 0.6

     pause 2

     show text "Instead of fields of greenery I feel a bloody taste...'" with dissolve:
           xalign 0.5
           yalign 0.7

     pause 2

     hide text

     with dissolve

     stop ambience

     t "Huh?"

     play ambience birds fadein 3

     "A mysterious aura of night has dissolved into the morning sky along with the stars. As well as dreams, you'd say. But this one however didn't want to go away."

     t "Anyway, how could such a bizarre dream be forgotten?"

     play music morning1

     show bg_h_day

     show table1

     show lantern_off:
         xalign 0.9 yalign 0.9
         linear 0.9 xalign 0.9

     show kd3

     with dissolve

     k "Good morning, [traveler]!{w=0.5} How's the night?"

     menu:

        "Pretty confusing, I'd say":

         pass

     t "At first I heard the sound of wind with someone's voice calling my name, then I saw a white light, and here she was, glad to see me again..."
     #How to address a Deity?
     t "Later she told me something... let me remember..."

     window hide

     pause 1.5

     window show

     with dissolve

     t "WHAT? I can't remember! It must be some kind of magic!"

     k "Hm-m, let me think{w=0.5}... The dream you've had is quite{w=0.5}... interesting"

     t "In...teresting?"
     window hide
     #TODO: add a sound almost similar to the one we experience when blacking out and a glitch on the screen

     show bg_h_day

     show table1

     show lantern_off:
         xalign 0.9 yalign 0.9
         linear 0.9 xalign 0.9

     show kd

     with hpunch

     with pixellate

     window show

     with dissolve

     #show kaeya worried

     k "Are you alright, [traveler]?"

     menu:

        "Yes, but my head hurts a little bit":

         pass

     #show kaeya serious

     k "I understand how it feels being overwhelmed with a ton of information. And{w=0.5}... oh, you're probably starving{w=0.5}... How about we have breakfast then?"

     window hide

     hide kd

     window show

     with dissolve
     #with fade
     #TODO: draw a CG of MC and Kaeya having a breakfast
     #In the future a Fade transition will be used instead, so do not uncomment until a scetch is ready
     "You and Kaeya enjoy a delicious breakfast. During the meal your headache soothes, thoughts become clear and mood better."

     #show kaeya wondered

     k "How is breakfast?{w=0.5} Do you like it?"

     t "Om-nom-nom-nom-nom-nom-nom... M-mm, delicious! Can I have one more, please?"
     #https://www.youtube.com/watch?v=_OKGUAbpj5k
     #show kaeya happy

     k "Of course!{w=0.5} Everything for you!"

     window hide

     show kd

     window show

     with dissolve

     t "Kaeya, thank you so much for the meal! This is one of the best breakfasts I've ever had!"

     k "Glad you liked it!{w=0.5} And now you may ask whatever has been worrying your curious mind."

     label question:

     menu:

        "About my dream...":

         pass

     stop music fadeout 1.5

     stop ambience fadeout 1.0

     k "I'm actually intrigued about your dream, or let's say, that figure.{w=0.5} According to your description, the figure who appeared in your dream might be none other than{w=0.5}...The Thousand Winds."
     #Please don't trust a mere fan game! They are not signs of Istaroth!
     menu:

        "The Thousand Winds?":

         pass

     k "Long time ago,{w=0.25} people in Mondstadt used to worship them along with Anemo Archon, but they have gone with the wind over time."
     #Note: currently it is unknown which pronoun Kaeya should use whenever mentioning Istaroth
     #No, it's not about DEI, it's about a DEIty (silly joke, I know).
     #Using they/them, as if we know nothing about the person seems to be right(?)
     #Using "she/her" on the other hand would quickly imply that Kaeya knows(?) the information about the Shade, thus making him
     #extremely sus
     k "The only thing that's been left is Thousand Winds Temple.{w=0.5} Would you like to go there?"

     label choice_f:

     menu:

        "Yes!":

         jump beta_end

     label beta_end:

     play sound finale fadein 1.0

     "Unfortunately, this option is unavailable."

     menu:

        "Maybe for the next time":

         pass

     k "Oh,{w=0.25} is that so?{w=0.5} Well, then, we lost nothing!"

     menu:

        "Nothing?":

         pass

     k "For some reason the area is closed for viewers, so even if we went there, we wouldn't be welcomed for sure."

     k "Meanwhile, my time is off, [traveler]!{w=0.5} I was glad to hang out with you "

     hide bg_h_day

     hide table1

     hide lantern_off

     hide kd

     hide kd2

     hide kd3

     stop ambience

     with fade

     scn "Dear Kaeya..."

     scn "This is only the beginning. I still have a long way to go despite the work I've done."

     scn "And though I wasn't as active as I used to be, I still cared about the game. As well as you, silly!"

     scn "We have gone through lots of adventures and difficulties, both in Teyvat and real life. The more we learned about each other, the more similarities were found out."

     scn "From crying hard because of the dark past and comforting... to actually smiling with tears and feeling relief when you see a happy end."

     scn "That's what I love about it. That feeling when you grow up and mature with your favourite character."

     scn "Oh..."

     scn "And this is to you, player..."

     scn "I hope your experience was mostly positive despite the game being very short and most interesting content hidden under sketches in .txt files."

     scn "But even if the experience was not a positive one I'm still glad you decided to try it."

     scn "After all, it's completely normal to criticize something. Who knows, maybe your constructive criticism will teach me something!"

     scn "Well, you see I'm still a beginner making this game alone. So, if you're willing to help me, I will be very glad to see you in my little family."

     scn "Thank you for playing the game! ^-^"

     scn "And see you in future episodes of 'Two Stars, Two Fates, Two Worlds'!"

     scn "With love, mlka"

     $ renpy.quit()
