import time
import random
import sys

def main():
    health = 1000
    attack_hands = random.randint(1, 30)
    attack_weapon = random.randint(1,100)
    dragon_attack = random.randint(1, 50)
    boss_attack = random.randint(1, 100)
    choice2 = 'no'
    print("""Welcome, young noble one, I am more than greatful to see you.
    I have for many years dreamed of a young savior to come save my people, and finally
    you are here, please save my people from this Dark Lord who reignes over this land
    SET US FREE!""")
    print('````````````````````````````````````````````````')
    name = input('What name shall I call you?: ')
    print('````````````````````````````````````````````````')
    time.sleep(3)
    game = input('Do you wish to begin your Quest master ' + name + '?: ')
    choice = 'yes'
    if game == choice:
        print('`````````````````````````````````````````````')
        print('Great choice, lets go your journey awaits!, Sir you do not have armor or weapons, in order to slay your enemies you will need to be well equipped')
        print('`````````````````````````````````````````````')
        time.sleep(3)
        journey()
    elif game == choice2:
        print('Running away already I see... You surely can not be the one..')
        time.sleep(2)
        print('LEAVE')

def journey():
    choice = 'north'
    choice1 = 'south'
    choice2 = 'east'
    choice3 = 'west'

    print('-- The Four Paths -- ')
    print('<> North')
    print('<> South')
    print('<> East')
    print('<> West')
    print('``````````````````````````````````')
    print('<> Quit')
    print('``````````````````````````````````')
    time.sleep(3)
    journey = input('Where to young master?: ')
    print('``````````````````````````````````')


    if journey == choice:
        print('You chose to go North master, I know many elders of war this way')
        time.sleep(3)
        north()
    elif journey == choice1:
        print('South it is, lets go master. Maybe you can claim a dragon')
        time.sleep(3)
        south()
        south2()
    elif journey == choice2:
        print('** This is a dangerous Path you are taking, You must be heavily armed **')
        time.sleep(3)
        east()
    elif journey == choice3:
        print('This is the way to your village master, lets get some food and weapons')
        time.sleep(3)
        west()
        west2()
    else:
        print('Until next time master.....')
        time.sleep(2)
        sys.exit()






def north():
    choice = 'yes'
    print('``````````````````````````````````')
    print('Master the elders of War are full of great knowledge and will show you the way.')
    print('``````````````````````````````````')
    time.sleep(3)
    speak = input('Would you like to speak with them master?: ')
    if speak == choice:
        print('Great master, you will surely be many steps ahead in battle!')
        time.sleep(3)
    else:
        print('I understand sir, we shall continue on our way.')
    print('``````````````````````````````````')
    scroll = input('Look master an ancient scroll has been dropped by this tree. Do you wish to read it?:  ')
    if scroll == choice:
        time.sleep(3)
        print('1000 B.C. the elders have ruled the land and therefore createth the law, and whosever breaketh shall..........')
        print('```````````````````````````````````````````')
        time.sleep(3)
        print('Maybe thats enough reading for now master...')
        print('```````````````````````````````````````````')
        time.sleep(3)
    else:
        print('Ok master, lets keep our way.')
        print('```````````````````````````````````````````')

    print('Master this is quiet a long journey, dont worry we are near')
    print('```````````````````````````````````````````````')
    time.sleep(3)
    print('We are here master')
    print('```````````````````````````````````````````````')
    time.sleep(3)
    print('GUARDIAN: Elder this is a young King seeking your knowledge...')
    print
    time.sleep(3)
    name = input('ELDER: you are seeking my wisdom.. what is thy name?: ')
    print('```````````````````````````````````````````````')
    time.sleep(3)
    print('ELDER: master ' + name + ' take heed to my wisdom and you will surely conquer anything in thy path..')
    print('```````````````````````````````````````````````')
    time.sleep(3)
    print(name + ' : I wish to become the ruler of all and the king of all four nations.' )
    print('```````````````````````````````````````````````')
    time.sleep(3)
    print('ELDER: and thus you shall become. I have given you what you need in this short period of time. GO!')
    time.sleep(2)
    print('```````````````````````````````````````````````')
    print('Lets go master..')
    time.sleep(2)
    journey()


def south():
    choice = 'yes'
    print('If you wish to claim the skies you must first tame a dragon, you have chosen the right path master')
    time.sleep(2)
    print('`````````````````````````````````````````````````````````````````')
    print('these dragons can be quite fierce so you will need to be ready! You must first be equipped with sorecery to capture a dragon.')
    print('`````````````````````````````````````````````````````````````````')
    time.sleep(2)
    sorc = input('Do you have sorcery master?: ')
    time.sleep(2)
    if sorc == choice:
        print('`````````````````````````````````````````````````````````````````')
        print('Look master, I spot 4 dragons')
        print('`````````````````````````````````````````````````````````````````')
        time.sleep(2)
        south2()
    else:
        print('We will return when you have dark magic master..')
        time.sleep(2)
        journey()

def south2():
    choice = 'yes'
    D1 = 'gold'
    D2 = 'dark smoke'
    D3 = 'silver'
    D4 = 'shadow'
    print(' ---------------------- D R A G O N S ----------------------------------')
    print('<> The GOLD dragon is the biggest and strongest but yet the slowest')
    print('<> The DARK SMOKE dragon is the fastest with a bite that will vanquish thy enemy instantly')
    print('<> The SILVER dragon is quick and swifty, your enemy will fatique quickly, an easy victory master')
    print('<> The SHADOW dragon is great for stealth night attacks, as you will become invisible to all but other dragons')
    print('````````````````````````````````````````````````````````````````')
    dragon = input('Which dragon shall you tame master?: ')
    print('``````````````````````````````````````````````')
    if dragon == D1:
        fight1 = input('Are you sure master?: ')
        print('``````````````````')
        if fight1 == choice:
            print('OK master, you must do this yourself. GO!')
            print('````````````````````````````````````````````')
            time.sleep(2)
            dragon_fight()
        else:
            print('Another day then...')
            time.sleep(2)
            restart1()
    elif dragon == D2:
        fight2 = input('Are you sure master?: ')
        print('``````````````````')
        if fight2 == choice:
                print('Be fast master, dont take this dragon lightly, as you cannot tame him being slow, GO!')
                print('````````````````````````````````````````````')
                time.sleep(2)
                dragon_fight()
        else:
            print('Another day then...')
            time.sleep(2)
            restart1()
    elif dragon == D3:
        fight3 = input('Are you sure master?: ')
        print('``````````````````')
        if fight3 == choice:
            print('Do not stay in one place for to long with this dragon, KEEP MOVING')
            print('````````````````````````````````````````````')
            time.sleep(2)
            dragon_fight()
        else:
            print('Another day then...')
            time.sleep(2)
            restart1()
    elif dragon == D4:
        fight4 = input('Are you sure master?: ')
        print('``````````````````')
        if fight4 == choice:
            print('You must blend master, do not be seen in plain sight!')
            print('````````````````````````````````````````````')
            time.sleep(2)
            dragon_fight()
        else:
            print('Another day then...')
            time.sleep(2)
            restart1()
    else:
        print('Master wish to not Fight today?')
        restart()


def east():
    choice = 'yes'

    print('This is the Path to the Dark Lord sir, If you are not well equipped then we should not yet take this path')
    time.sleep(2)
    print('```````````````````````````````````````````````````')
    time.sleep(2)
    ready = input('Do you wish to continue master, you must have all weapons in order to proceed: ')
    print('```````````````````````````````````````````````````')
    if ready == choice:
        print('Master I will follow, lead the way')
        time.sleep(2)
        Dfight()
        Dfight2()
    else:
        print('You are not yet ready master')
        restart()

def west():


    print("""Here you will be able to equip youself with everything you will need on your journey.
            The village is a safe haven for you at anytime. feel from to wonder master""")
    print('```````````````````````````````````````````````````````')

def west_menu():
        print('MENU')
        print('``````````')
        print(' <> Apples')
        print(' <> Water')
        print(' <> Vegetables')
        print(' <> Meat')
        print('``````````')

def west2():
    choice = 'yes'
    village1 = 'food market'
    village2 = 'blacksmith'
    village3 = 'my shack'
    village4 = 'sorcery shop'
    choice2 = 'go back'
    food1 = 'apples'
    food2 = 'water'
    food3 = 'vegetables'
    food4 = 'meat'
    money = 100.00
    apples = 2.75
    water = 1.00
    vegetables = 4.25
    print('Stores')
    print('````````````````````````````````')
    print(' <> Food Market')
    print(' <> Blacksmith')
    print(' <> My shack')
    print(' <> Sorcery Shop')
    print(' <> Go Back')
    print('````````````````````````````````')
    time.sleep(2)

    village = input('Where would you like to go in the village..?: ')
    print('````````````````````````````````````````````````````````````')

    if village == village1:
        dest = input('You chose the food market. Continue?: ')
        print('````````````````````````')
        if dest == choice:
            print('`````````````````')
            print("Welcome to the Food market, here you can get what you will need to stay healthy and strong.")
            time.sleep(2)
            west_menu()
            time.sleep(2)
            print('Master thy haveth enough coins to purchase anything on the menu..')
            print('````````````')
            time.sleep(2)
            print('You have ' + str(money) + ' coins')
            print('````````````')
            time.sleep(2)
            print
            food = input('Which do you want master?: ')
            print('````````````')
            if food == food1:
                purchase = float(input('How many apples do you want?: '))
                total = money - purchase * apples
                print('You bought ' + str(purchase) + ' apples. You now have ' + str(total) + ' coins' )
                time.sleep(2)
                print('````````````````````````')
                menu = input('Continue shopping?:  ')
                if menu == choice:
                    time.sleep(2)
                    print('OK master..')
                    time.sleep(2)
                    west2()
                else:
                    west2()
            elif food == food2:
                purchase = float(input('How many bottles of water do you want?: '))
                total = money - purchase * water
                print('You bought ' + str(purchase) + ' bottles of water. You now have ' + str(total) + ' coins' )
                time.sleep(2)
                print('````````````````````````')
                menu = input('Continue shooping?:  ')
                if menu == choice:
                    time.sleep(2)
                    print('OK master..')
                    time.sleep(2)
                    west2()
                else:
                    west2()
            elif food == food3:
                purchase = float(input('How many vegetables do you want?: '))
                total = money - purchase * vegetables
                print('You bought ' + str(purchase) + ' vegetables. You now have ' + str(total) + ' coins' )
                time.sleep(2)
                print('````````````````````````')
                menu = input('Continue shopping?:  ')
                if menu == choice:
                    time.sleep(2)
                    print('OK master..')
                    time.sleep(2)
                    west2()
                else:
                    west2()
            elif food == food4:
                purchase = float(input('How many pounds of meat do you want?: '))
                total = money - purchase * apples
                print('You bought ' + str(purchase) + ' pounds of meat. You now have ' + str(total) + ' coins' )
                time.sleep(2)
                print('````````````````````````')
                menu = input('Continue shopping?:  ')
                if menu == choice:
                    time.sleep(2)
                    print('OK master..')
                    time.sleep(2)
                    west2()
                else:
                    west2()
            else:
                print('Wrong place? lets go back..')
                timne.sleep(2)
                west2()
        else:
            restart2()
    elif village == village2:
        w1 = 'sword'
        w2 = 'spear'
        w3 = 'sorcery'
        w4 = 'dragon'
        w5 = 'all'
        cash = 100
        sword = 25.50
        spear = 15.89
        sorcery = 15.23
        dragon = 25.65
        cashout = 100.00

        dest2 = input('You chose the Blacksmith. Continue?: ')
        print('````````````````````````')
        if dest2 == choice:
            print('`````````````````')
            print('AHH the blacksmith, gather the weapons you need master.')
            time.sleep(2)
            print('``````````')
            print('WEAPONS')
            print('``````````')
            print(' <> Sword')
            print(' <> Spear')
            print(' <> sorcery')
            print(' <> Dragon')
            print(' <> Buy all <>')
            print('``````````')
            print(' Go back')
            print('``````````')
            time.sleep(2)
            EQ = input(' Which weapon do you wish buy. You have ' + str(cash) + ' coins: ')
            if EQ == w1:
                total = cash - sword
                print('You have purchased a Sword for ' + str(sword) + ' coins. You now have ' + str(total) + ' coins')
                time.sleep(2)
                cont = input("Continue shopping?: ")
                if cont == choice:
                    print('OK master..')
                    west2()
                else:
                    journey()
            elif EQ == w2:
                total = cash - spear
                print('You have purchased a Spear for ' + str(spear) + ' coins. You now have ' + str(total) + ' coins')
                time.sleep(2)
                cont = input("Continue shopping?: ")
                if cont == choice:
                    print('OK master..')
                    west2()
                else:
                    journey()
            elif EQ == w3:
                total = cash - sorcery
                print('You have purchased sorcery equipement for ' + str(sorcery) + ' coins. You now have ' + str(total) + ' coins')
                time.sleep(2)
                cont = input("Continue shopping?: ")
                if cont == choice:
                    print('OK master..')
                    west2()
                else:
                    journey()
            elif EQ == w4:
                total = cash - dragon
                print('You have purchased equipement your dragon for ' + str(dragon) + ' coins. You now have ' + str(total) + ' coins')
                time.sleep(2)
                cont = input("Continue shopping?: ")
                if cont == choice:
                    print('OK master..')
                    west2()
                else:
                    journey()
            elif EQ == w5:
                total2 = cash - cashout
                print('You have purchased all weapons for ' + str(cashout) + ' coins. You now have ' + str(total2) + ' coins')
                time.sleep(2)
                cont = input("Continue shopping?: ")
                if cont == choice:
                    print('OK master..')
                    west2()
                else:
                    journey()
        else:
            restart2()
    elif village == village3:
        s = 'stay'
        l = 'leave'
        dest3 = input('You chose your Shack. Continue?: ')
        print('````````````````````````')
        if dest3 == choice:
            print('`````````````````')
            print('Go rest master, regain your strength, I shall wait for you to awaken.')
            time.sleep(1)
            print('...')
            time.sleep(2)
            print('.....')
            time.sleep(3)
            print('........')
            time.sleep(3)
            print('OK master.. we must not waste any more time lets go!')
            stay = input('Stay West or leave master?: ')
            if stay == s:
                time.sleep(2)
                print('Ok master')
                print('`````````')
                west2()
            else:
                print('Ok master off we go..')
                time.sleep(1)
                journey()
        else:
            restart2()
    elif village == village4:
        choice = 'yes'
        dest4 = input('You chose the Sorcery Store. Continue?: ')
        print('````````````````````````')
        if dest4 == choice:
            time.sleep(2)
            print('Who knows you may need a spell or two.')
            print('``````````````````````````````````````')
            time.sleep(2)
            print(' Sorcerer: Welcome! seeking the power of magic I see.. ')
            time.sleep(2)
            print('``````````````````````````````````````')
            power = input(' Sorcerer: Do you wish to possess this dark magic?: ')
            if power == choice:
                time.sleep(2)
                print(' Sorcerer: Ok young one. I now bestow dark magic powers upon you')
                time.sleep(1)
                print('...')
                time.sleep(2)
                print('Sorcery equipped')
                time.sleep(2)
                print('.......')
                time.sleep(3)
                print('Your health has increased + 25')
                time.sleep(3)
                print('..........')
                time.sleep(2)
                print(' Sorcerer: Go now use your power to destroy the Dark Lord...')
                time.sleep(2)
                west2()
            else:
                print('Ok lets go somewhere else master..')
                time.sleep(2)
                west2()




        else:
            restart2()
    elif village == choice2:
        CH = input('Are you sure you want to go back?: ')
        if CH == choice:
            print('OK master off we go..')
            journey()
        else:
            print("OK master, we will stay")
            west2()
    else:
        print('`````````````````')
        print('Change your mind master?')
        restart2()



def Dfight():


    print('the dark lord, there he is what shal we do master?!')
    time.sleep(3)
    print('MASTER, WATCH OUT')
    time.sleep(2)

def Dfight2():

    hit = random.randint(80, 100)
    kick = random.randint(1, 50)
    sword = random.randint(3, 75)
    spear = random.randint(2, 105)
    dragon = random.randint(80, 100)

    choice = 'yes'
    justin = 100
    boss = 100
    w1 = 'sword'
    w2 = 'spear'
    w3 = 'dragon'

    boss_attack = justin - hit
    justin_attack = boss - kick
    sword_attack = boss - sword
    spear_attack = boss - spear
    dragon_attack = boss - dragon

    print('the Dark Lord attacked you')
    time.sleep(2)
    print('Your health is now: ' + str(boss_attack) + ' Percent')


    while boss_attack <= justin:

        if boss != 0:
            attack = input('attack?: ')
            if attack == choice:
                print('``````````')
                time.sleep(1)
                print('WEAPONS')
                print('``````````')
                print(' <> Sword')
                print(' <> Spear')
                print(' <> sorcery')
                print(' <> Dragon')
                print('``````````')
                weapon = input('What weapon shall you use?: ')
                time.sleep(2)
                print('``````````')

                if weapon == w1:
                    print('You attacked the Dark Lord with your sword')
                    print('````````````````````````````````````````````')
                    time.sleep(2)
                    print('His health is now ' + str(sword_attack) + ' Percent')
                    time.sleep(2)
                    if boss_attack < sword_attack:
                        time.sleep(2)
                        print('** you have been defeated **')
                        time.sleep(2)
                        print('Come back when your are stronger master...Off we go')
                        time.sleep(2)
                        print('```````````````````')
                        journey()
                    else:
                        print('```````````````````')
                        print('you defeated the dark lord ')
                        time.sleep(1)
                        print(' What a great VICTORY you are now the ruler of all Four nations!...')
                        time.sleep(3)
                        print('All shall bow before you as you are now the KING!!!')
                        time.sleep(4)
                        print('```````````````````')
                        print('GAME OVER')
                        time.sleep(3)
                        new_game = input(' Do you wish to begin a new game?: ')
                        if new_game == choice:
                            print('As you wish...')
                            print('```````````````````')
                            time.sleep(2)
                            main()
                        else:
                            print('Til we meet again....')
                            print('```````````````````')
                            time.sleep(2)
                            sys.exit()
                elif weapon == w2:
                    print('You attacked the Dark Lord with your spear')
                    print('````````````````````````````````````````````')
                    time.sleep(2)
                    print('His health is now ' + str(spear_attack) + ' Percent')
                    time.sleep(2)
                    if boss_attack < spear_attack:
                        time.sleep(2)
                        print('** you have been defeated **')
                        time.sleep(1)
                        print('Come back when your are stronger master...Off we go')
                        time.sleep(2)
                        print('```````````````````')
                        journey()
                    else:
                        print('```````````````````')
                        print('you defeated the dark lord')
                        time.sleep(1)
                        print(' What a great VICTORY you are now the ruler of all Four nations!...')
                        time.sleep(3)
                        print('All shall bow before you as you are now the KING!!!')
                        time.sleep(4)
                        print('```````````````````')
                        print('GAME OVER')
                        time.sleep(3)
                        new_game = input(' Do you wish to begin a new game?: ')
                        if new_game == choice:
                            print('As you wish...')
                            print('```````````````````')
                            time.sleep(2)
                            main()
                        else:
                            print('Til we meet again....')
                            print('```````````````````')
                            time.sleep(2)
                            sys.exit()
                elif weapon == w3:
                    print('You attacked the Dark Lord with your Dragon')
                    print('````````````````````````````````````````````')
                    time.sleep(2)
                    print('His health is now ' + str(dragon_attack) + ' Percent')
                    time.sleep(2)
                    if boss_attack < dragon_attack:
                        time.sleep(2)
                        print('** you have been defeated **')
                        time.sleep(1)
                        print('Come back when your are stronger master...Off we go')
                        time.sleep(2)
                        print('```````````````````')
                        journey()
                    else:
                        print('```````````````````')
                        print('you defeated the dark lord')
                        time.sleep(1)
                        print(' What a great VICTORY you are now the ruler of all Four nations!...')
                        time.sleep(3)
                        print('All shall bow before you as you are now the KING!!!')
                        time.sleep(4)
                        print('```````````````````')
                        print('GAME OVER')
                        time.sleep(3)
                        new_game = input(' Do you wish to begin a new game?: ')
                        if new_game == choice:
                            print('As you wish...')
                            print('```````````````````')
                            time.sleep(2)
                            main()
                        else:
                            print('Til we meet again....')
                            print('```````````````````')
                            time.sleep(2)
                            sys.exit()
                else:
                    print('You attacked the Dark Lord with your sorcery')
                    print('````````````````````````````````````````````')
                    time.sleep(2)
                    print('the Dark Lord health is now ' + str(justin_attack) + ' Percent')
                    time.sleep(2)
                    if boss_attack < justin_attack:
                        time.sleep(2)
                        print('** you have been defeated **')
                        time.sleep(1)
                        print('Come back when your are stronger master...Off we go')
                        time.sleep(2)
                        print('```````````````````')
                        journey()
                    else:
                        print('```````````````````')
                        print('you defeated the dark lord')
                        time.sleep(1)
                        print(' What a great VICTORY you are now the ruler of all Four nations!...')
                        time.sleep(3)
                        print('All shall bow before you as you are now the KING!!!')
                        time.sleep(4)
                        print('```````````````````')
                        print('GAME OVER')
                        time.sleep(3)
                        new_game = input(' Do you wish to begin a new game?: ')
                        if new_game == choice:
                            print('As you wish...')
                            print('```````````````````')
                            time.sleep(2)
                            main()
                        else:
                            print('Til we meet again....')
                            print('```````````````````')
                            time.sleep(2)
                            sys.exit()

            else:
                print('RUN')
        elif justin == 0:
            print('You have been defeated, come back to fight another day.')
        else:
            print('you defeated the boss')





def dragon_fight():

        hit = random.randint(50, 100)
        sorcery = random.randint(45, 95)
        sword = random.randint(3, 75)
        spear = random.randint(2, 105)
        dragon = random.randint(80, 100)

        choice = 'yes'
        player = 80
        dragon = 100
        w1 = 'sorcery'


        dragon_attack = player - hit
        player_attack = dragon - sorcery

        print('Remember master, you must not stand in one place for to long..')
        time.sleep(2)
        print('the Dragon Lord attacked you')
        time.sleep(2)
        print('Your health is now: ' + str(dragon_attack) + ' Percent')
        time.sleep(2)
        print('Now master, tame this beast!..')
        time.sleep(2)


        while dragon_attack <= player:

            if dragon != 0:
                attack = input('Do you wish to attack master?: ')
                if attack == choice:
                    print('``````````')
                    time.sleep(1)
                    print('WEAPONS')
                    print('``````````')
                    print(' <> sorcery <> ')
                    print('``````````')
                    weapon = input('Do you wish to fight? What weapon shall you use?: ')
                    time.sleep(2)
                    print('``````````')

                    if weapon == w1:
                        print('You attacked the Dragon with your sorcery')
                        print('````````````````````````````````````````````')
                        time.sleep(2)
                        print('````````````````````````````````````````````')
                        print('surely your dark magic was enough to tame this beast')
                        print('````````````````````````````````````````````')
                        time.sleep(2)
                        print('His health is now ' + str(player_attack) + ' Percent')
                        time.sleep(2)
                        if dragon_attack < player_attack:
                            time.sleep(2)
                            print('** you have been slain **')
                            print('``````````')
                            time.sleep(2)
                            print('Come back when your dark magic is stronger...Off we go')
                            time.sleep(2)
                            print('```````````````````')
                            journey()
                        else:
                            print('```````````````````')
                            print('Great master, you tamed this great beast ')
                            print('``````````')
                            time.sleep(1)
                            print(' What a great VICTORY master where shall we go next?...')
                            time.sleep(2)
                            print('```````````````````')
                            journey()
                    else:
                        print("RUN master, we will come back when you are stronger!!!")
                        time.sleep(3)
                        print(' that was a close one... off we go')
                        time.sleep(2)
                        journey()





def restart():
    choice = 'yes'
    restart = input('Go Back?: ')
    while True:
        if restart != choice:
            print('You are not worthy of my loyalty, goodbye!')
            break
        else:
            print('Sir lets get you taken care!')
            print('````````````````````````````')
            journey()

def restart1():
    choice = 'yes'
    restart = input('Change dragons?: ')
    print('```````````````````````````')
    while True:
        if restart == choice:
            south2()

def restart2():
    choice = 'yes'
    restart = input('Wrong place?: ')
    print('```````````````````````````')
    while True:
        if restart == choice:
            west2()
        else:
            west2()



main()
