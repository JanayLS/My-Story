#Who said it? Quiz and Guessing Game
#Asking for age
'''
displays different colored duckies in somewhat rainbow order at the end
'''
def rainbow():
    num = 20
    while num > 2:
        def happyDuck():
            def prYellow(skk): 
                print("\033[93m {}\033[00m" .format(skk))
            def prCyan(skk): 
                print("\033[96m {}\033[00m" .format(skk))
            def prGreen(skk): 
                print("\033[92m {}\033[00m" .format(skk))
            def prRed(skk): 
                print("\033[91m {}\033[00m" .format(skk))
            def prPurple(skk): 
                print("\033[95m {}\033[00m" .format(skk))
            prRed("                         ____________")
            prRed("                      /               \\")
            prRed("                     /                 \\")
            prRed("                    /                    \\")
            prRed("                   |              o         >>")
            prRed("                   |          @               >>")
            prRed("                   |                            >>")
            prRed("-------------------                           >>")
            prRed("\                                         >>")
            prRed(" \                                       /")
            prRed("  \                                     /  ")
            prRed("   \                                   /")
            prRed("    \                                /")
            prRed("     \                              /")
            prRed("      ----------------------------")
            import os
            import time
            time.sleep(3)
            prYellow("                         ____________")
            prYellow("                      /               \\")
            prYellow("                     /                 \\")
            prYellow("                    /                    \\")
            prYellow("                   |              o         >>")
            prYellow("                   |          @               >>")
            prYellow("                   |                            >>")
            prYellow("-------------------                           >>")
            prYellow("\                                         >>")
            prYellow(" \                                       /")
            prYellow("  \                                     /  ")
            prYellow("   \                                   /")
            prYellow("    \                                /")
            prYellow("     \                              /")
            prYellow("      ----------------------------")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            prGreen("                         ____________")
            prGreen("                      /               \\")
            prGreen("                     /                 \\")
            prGreen("                    /                    \\")
            prGreen("                   |              o         >>")
            prGreen("                   |          @               >>")
            prGreen("                   |                            >>")
            prGreen("-------------------                           >>")
            prGreen("\                                         >>")
            prGreen(" \                                       /")
            prGreen("  \                                     /  ")
            prGreen("   \                                   /")
            prGreen("    \                                /")
            prGreen("     \                              /")
            prGreen("      ----------------------------")
            import os
            import time
            time.sleep(3)
            prCyan("                         ____________")
            prCyan("                      /               \\")
            prCyan("                     /                 \\")
            prCyan("                    /                    \\")
            prCyan("                   |              o         >>")
            prCyan("                   |          @               >>")
            prCyan("                   |                            >>")
            prCyan("-------------------                           >>")
            prCyan("\                                         >>")
            prCyan(" \                                       /")
            prCyan("  \                                     /  ")
            prCyan("   \                                   /")
            prCyan("    \                                /")
            prCyan("     \                              /")
            prCyan("      ----------------------------")
            import os
            import time
            time.sleep(3)
            prPurple("                         ____________")
            prPurple("                      /               \\")
            prPurple("                     /                 \\")
            prPurple("                    /                    \\")
            prPurple("                   |              o         >>")
            prPurple("                   |          @               >>")
            prPurple("                   |                            >>")
            prPurple("-------------------                           >>")
            prPurple("\                                         >>")
            prPurple(" \                                       /")
            prPurple("  \                                     /  ")
            prPurple("   \                                   /")
            prPurple("    \                                /")
            prPurple("     \                              /")
            prPurple("      ----------------------------")
            import os
            import time
            time.sleep(3)
        happyDuck()
        import os
        import time
        time.sleep(10)
def yearsOld():
    while True:
        try:
            age=int(input("Enter age: "))
            print("\n Thank you!\n")
        except ValueError:
            print("\nNot valid.\n")
        else:
            break
    ages=[13,14,15,16,17,18]
    ages.append(age)
    ages.remove(15)
    ages.insert(2,15)
    if age in ages:
        print("You are of age to play this game.\n")
        import os
        import time
        time.sleep(4)
        os.system('clear')
        try:
            num1=int(input("Enter number: "))
            num2=int(input("Enter another one: "))
            num3=int(input("One more: "))
            num4=int(input("Okay sorry. Another one: "))
            num5=int(input("For real this time. Last one: "))
            NUM=age + num1 + num2 * num3 - num4 / num5
            bigNum=print(age,"+",num1,"+", num2, "*", num3, "-", num4,"/", num5,"=",NUM,"\n\n\n")
            print("Now you must hit the letter "'P',NUM,"times.\n")
            p=input("Get started: ")

            if "p" in p:
                print("\nJust kidding, I'm just messing with you. Just enjoy this ducky light show!")
                import os
                import time
                time.sleep(7)
                os.system('clear')
                rainbow()
            
        except ValueError:
            print("Not valid answer")
        
    else:
        print("Your age is not listed. Sorry, you can't play this game.\n")
    print("")
    import os
    import time
    time.sleep(4)
    os.system('clear')

'''
Contains quiz and possible responses
Certain questions kick you out and certain ones let you continue
'''
def easy():
    import time
    wrgmsg="Nope. Try again."
    print("So the point of this game is to test your knowledge on famous people and their inspiring quotes. If you get one wrong, you either get kicked out or you can continue on. So be careful on which ones you miss! Let's see if you got what it takes.")
    time.sleep(10)
    print("Ready?")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Go!")
    time.sleep(1)
    print("")
    #Question 1
    import os
    os.system('clear')
    print('"I have a dream."\n')
    answer1=input(str(" a) Voltaire\n b) Martin Luther King\n c) Julius Caesar\n d) Patrick Star\n\n Your answer: "))
    if answer1 == "b":
        print("You got that one right. But everyone knows that one. Let's try another one.")
        print("--------------------------------------------------------------------------------------\n")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        #Question 2
        print('"Time is money."\n')
        answer2=input(" a) Albert Einstein\n b) Mahatma Gandhi\n c) Benjamin Franklin\n d) Edgar Allen Poe\n\n Your answer: ")
        if answer2 == "c":
            print("Correct. Next question.")
            print("--------------------------------------------------------------------------------------\n")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            #Question 3
            print('"You must be the change you see in the world."\n')
            answer3=input(" a) Babe Ruth\n b) Master Splinter\n c) Eeyore\n d) Mahatma Gandhi\n\n Your answer: ")
            if answer3 == "d":
                print("Nice, you're pretty good at this. Next question. ")
                print("--------------------------------------------------------------------------------------\n")
                import os
                import time
                time.sleep(3)
                os.system('clear')
                #Question 4
                print('"Life is like a box of chocolates. You never know what you\'re going to get."\n')
                answer4=input(" a) Eeyore\n b) Elmo\n c) Forrest Gump\n d) Arthur\n\n Your answer: ")
                if answer4 == "c":
                    print("Ok, Nice. Next.")
                    print("--------------------------------------------------------------------------------------\n")
                    import os
                    import time
                    time.sleep(3)
                    os.system('clear')
                    #Question 5
                    print('"That\'s one small step for a man, one giant leap for mankind."\n')
                    answer5=input(" a) Neil Armstrong\n b) Niel Strongarm\n c) Janay Snell\n d) Alien\n\n Your answer: ")
                    if answer5 == "a":
                        print("You're getting it. On to the next question!")
                        print("--------------------------------------------------------------------------------------\n")
                        import os
                        import time
                        time.sleep(3)
                        os.system('clear')
                        #Question 6
                        print('"Eat my shorts!"\n')
                        answer6=input(" a) Dory\n b) My dog\n c) My shorts\n d) Bart Simpson\n\n Your answer: ")
                        if answer6 == "d":
                            print("Yep, that's right. Moving on...")
                            print("--------------------------------------------------------------------------------------\n")
                            import os
                            import time
                            time.sleep(3)
                            os.system('clear')
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            time.sleep(3)
                                            congrats='Congratulations!'
                                            print(congrats,"you've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"you've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madhatDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                        |            |")
                                                    prYellow("                        |            |")
                                                    prYellow("                        |            |")
                                                    prYellow("                        |____________|")
                                                    prYellow("                        |____________|")
                                                    prYellow("                    |____________________|")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                             ____________")
                                                    prYellow("                            |            |")
                                                    prYellow("                            |            |")
                                                    prYellow("                            |            |")
                                                    prYellow("                            |____________|")
                                                    prYellow("                            |____________|")
                                                    prYellow("                        |____________________|")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                   ____________")
                                                    prYellow("                                  |            |")
                                                    prYellow("                                  |            |")
                                                    prYellow("                                  |            |")
                                                    prYellow("                                  |____________|")
                                                    prYellow("                                  |____________|")
                                                    prYellow("                              |____________________|")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                           ____________")
                                                    prYellow("                                          |            |")
                                                    prYellow("                                          |            |")
                                                    prYellow("                                          |            |")
                                                    prYellow("                                          |____________|")
                                                    prYellow("                                          |____________|")
                                                    prYellow("                                      |____________________|")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                       ____________")
                                                    prYellow("                                                      |            |")
                                                    prYellow("                                                      |            |")
                                                    prYellow("                                                      |            |")
                                                    prYellow("                                                      |____________|")
                                                    prYellow("                                                      |____________|")
                                                    prYellow("                                                  |____________________|")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                  ____________")
                                                    prRed("                                                                 |            |")
                                                    prRed("                                                                 |            |")
                                                    prRed("                                                                 |            |")
                                                    prRed("                                                                 |____________|")
                                                    prRed("                                                                 |____________|")
                                                    prRed("                                                             |____________________|")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madhatDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"You've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                        else:
                            print(wrgmsg,"\n")
                            import os
                            import time
                            time.sleep(5)
                            os.system('clear')
                            time.sleep(3)
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            os.system('clear')
                                            time.sleep(3)
                                            congrats='Congratulations!'
                                            print(congrats,"you've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                    else:
                        print(wrgmsg,"\n")
                        import os
                        import time
                        time.sleep(5)
                        os.system('clear')
                        #Question 6
                        print('"Eat my shorts!"\n')
                        answer6=input(" a) Dory\n b) My dog\n c) My shorts\n d) Bart Simpson\n\n Your answer: ")
                        if answer6 == "d":
                            print("Yep, that's right. Moving on...")
                            print("--------------------------------------------------------------------------------------\n")
                            import os
                            import time
                            time.sleep(3)
                            os.system('clear')
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"You've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                        else:
                            print(wrgmsg,"\n")
                            import os
                            import time
                            time.sleep(5)
                            os.system('clear')
                else:
                    print(wrgmsg,"\n")
                    import os
                    import time
                    time.sleep(5)
                    os.system('clear')
                    #Question 5
                    print('"That\'s one small step for a man, one giant leap for mankind."\n')
                    answer5=input(" a) Neil Armstrong\n b) Niel Strongarm\n c) Janay Snell\n d) Alien\n\n Your answer: ")
                    if answer5 == "a":
                        print("You're getting it. On to the next question!")
                        print("--------------------------------------------------------------------------------------\n")
                        import os
                        import time
                        time.sleep(3)
                        os.system('clear')
                        #Question 6
                        print('"Eat my shorts!"\n')
                        answer6=input(" a) Dory\n b) My dog\n c) My shorts\n d) Bart Simpson\n\n Your answer: ")
                        if answer6 == "d":
                            print("Yep, that's right. Moving on...")
                            print("--------------------------------------------------------------------------------------\n")
                            import os
                            import time
                            time.sleep(3)
                            os.system('clear')
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"You've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                        else:
                            print(wrgmsg,"\n")
                            import os
                            import time
                            time.sleep(5)
                            os.system('clear')
                    else:
                        print(wrgmsg,"\n")
                        import os
                        import time
                        time.sleep(5)
                        os.system('clear')
            else:
                print(wrgmsg,"\n")
                import os
                import time
                time.sleep(5)
                os.system('clear')
                #Question 4
                print('"Life is like a box of chocolates. You never know what you\'re going to get."\n')
                answer4=input(" a) Eeyore\n b) Elmo\n c) Forrest Gump\n d) Arthur\n\n Your answer: ")
                if answer4 == "c":
                    print("Ok, Nice. Next.")
                    print("--------------------------------------------------------------------------------------\n")
                    import os
                    import time
                    time.sleep(3)
                    os.system('clear')
                    #Question 5
                    print('"That\'s one small step for a man, one giant leap for mankind."\n')
                    answer5=input(" a) Neil Armstrong\n b) Niel Strongarm\n c) Janay Snell\n d) Alien\n\n Your answer: ")
                    if answer5 == "a":
                        print("You're getting it. On to the next question!")
                        print("--------------------------------------------------------------------------------------\n")
                        import os
                        import time
                        time.sleep(3)
                        os.system('clear')
                        #Question 6
                        print('"Eat my shorts!"\n')
                        answer6=input(" a) Dory\n b) My dog\n c) My shorts\n d) Bart Simpson\n\n Your answer: ")
                        if answer6 == "d":
                            print("Yep, that's right. Moving on...")
                            print("--------------------------------------------------------------------------------------\n")
                            import os
                            import time
                            time.sleep(3)
                            os.system('clear')
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"You've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                        else:
                            print(wrgmsg,"\n")
                            import os
                            import time
                            time.sleep(5)
                            os.system('clear')
                    else:
                        print(wrgmsg,"\n")
                        import os
                        import time
                        time.sleep(5)
                        os.system('clear')
                else:
                    print(wrgmsg,"\n")
                    import os
                    import time
                    time.sleep(5)
                    os.system('clear')
        else:
            print(wrgmsg,"\n")
            import os
            import time
            time.sleep(5)
            os.system('clear')
            #Question 3
            print('"You must be the change you see in the world."\n')
            answer3=input(" a) Babe Ruth\n b) Master Splinter\n c) Eeyore\n d) Mahatma Gandhi\n\n Your answer: ")
            if answer3 == "d":
                print("Nice, you're pretty good at this. Next question. ")
                print("--------------------------------------------------------------------------------------\n")
                import os
                import time
                time.sleep(3)
                os.system('clear')
                #Question 4
                print('"Life is like a box of chocolates. You never know what you\'re going to get."\n')
                answer4=input(" a) Eeyore\n b) Elmo\n c) Forrest Gump\n d) Arthur\n\n Your answer: ")
                if answer4 == "c":
                    print("Ok, Nice. Next.")
                    print("--------------------------------------------------------------------------------------\n")
                    import os
                    import time
                    time.sleep(3)
                    os.system('clear')
                    #Question 5
                    print('"That\'s one small step for a man, one giant leap for mankind."\n')
                    answer5=input(" a) Neil Armstrong\n b) Niel Strongarm\n c) Janay Snell\n d) Alien\n\n Your answer: ")
                    if answer5 == "a":
                        print("You're getting it. On to the next question!")
                        print("--------------------------------------------------------------------------------------\n")
                        import os
                        import time
                        time.sleep(3)
                        os.system('clear')
                        #Question 6
                        print('"Eat my shorts!"\n')
                        answer6=input(" a) Dory\n b) My dog\n c) My shorts\n d) Bart Simpson\n\n Your answer: ")
                        if answer6 == "d":
                            print("Yep, that's right. Moving on...")
                            print("--------------------------------------------------------------------------------------\n")
                            import os
                            import time
                            time.sleep(3)
                            os.system('clear')
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"You've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                        else:
                            print(wrgmsg,"\n")
                            import os
                            import time
                            time.sleep(5)
                            os.system('clear')
                    else:
                        print(wrgmsg,"\n")
                        import os
                        import time
                        time.sleep(5)
                        os.system('clear')
                else:
                    print(wrgmsg,"\n")
                    import os
                    import time
                    time.sleep(5)
                    os.system('clear')
            else:
                print(wrgmsg,"\n")
                import os
                import time
                time.sleep(5)
                os.system('clear')
    else:
        print(wrgmsg,"\n")
        print("--------------------------------------------------------------------------------------\n")
        time.sleep(3)
        #Question 2
        print('"Time is money."\n')
        answer2=input(" a) Albert Einstein\n b) Mahatma Gandhi\n c) Benjamin Franklin\n d) Edgar Allen Poe\n\n Your answer: ")
        if answer2 == "c":
            print("Correct. Next question.")
            print("--------------------------------------------------------------------------------------\n")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            #Question 3
            print('"You must be the change you see in the world."\n')
            answer3=input(" a) Babe Ruth\n b) Master Splinter\n c) Eeyore\n d) Mahatma Gandhi\n\n Your answer: ")
            if answer3 == "d":
                print("Nice, you're pretty good at this. Next question. ")
                print("--------------------------------------------------------------------------------------\n")
                import os
                import time
                time.sleep(3)
                os.system('clear')
                #Question 4
                print('"Life is like a box of chocolates. You never know what you\'re going to get."\n')
                answer4=input(" a) Eeyore\n b) Elmo\n c) Forrest Gump\n d) Arthur\n\n Your answer: ")
                if answer4 == "c":
                    print("Ok, Nice. Next.")
                    print("--------------------------------------------------------------------------------------\n")
                    import os
                    import time
                    time.sleep(3)
                    os.system('clear')
                    #Question 5
                    print('"That\'s one small step for a man, one giant leap for mankind."\n')
                    answer5=input(" a) Neil Armstrong\n b) Niel Strongarm\n c) Janay Snell\n d) Alien\n\n Your answer: ")
                    if answer5 == "a":
                        print("You're getting it. On to the next question!")
                        print("--------------------------------------------------------------------------------------\n")
                        import os
                        import time
                        time.sleep(3)
                        os.system('clear')
                        #Question 6
                        print('"Eat my shorts!"\n')
                        answer6=input(" a) Dory\n b) My dog\n c) My shorts\n d) Bart Simpson\n\n Your answer: ")
                        if answer6 == "d":
                            print("Yep, that's right. Moving on...")
                            print("--------------------------------------------------------------------------------------\n")
                            import os
                            import time
                            time.sleep(3)
                            os.system('clear')
                            #Question 7
                            print('"Ohana means family, family means no one gets left behind. Or forgotten."\n')
                            answer7=input(" a) Stitch\n b) Dora\n c) Doc Mcstuffins\n d) Mario\n\n Your answer: ")
                            if answer7 == "a":
                                print("Get into it!")
                                print("--------------------------------------------------------------------------------------\n")
                                import os
                                import time
                                time.sleep(3)
                                os.system('clear')
                                #Question 8
                                print('"Just keep swimming!"\n')
                                answer8=input(" a) Dary\n b) Cory\n c) Dory\n d) Harry\n\n Your answer: ")
                                if answer8 == "c":
                                    print("Almost there...")
                                    print("--------------------------------------------------------------------------------------\n")
                                    import os
                                    import time
                                    time.sleep(3)
                                    os.system('clear')
                                    #Question 9
                                    print('"Some people are worth melting for."\n')
                                    answer9=input(" a) a popsicle\n b) Cookie Monster\n c) Olaf\n d) Tiana\n\n Your answer: ")
                                    if answer9 == "c":
                                        print("Alright. Last one.")
                                        print("--------------------------------------------------------------------------------------\n")
                                        import os
                                        import time
                                        time.sleep(3)
                                        os.system('clear')
                                        #Question 10
                                        print('"I never look back, darling, it distracts from the now."\n')
                                        answer10=input(" a) yours truly :)\n b) Edna Mode\n c) Enda Moed\n d) The Incredibles\n\n Your answer: ")
                                        if answer10 == "b":
                                            print("Correct!")
                                            print("--------------------------------------------------------------------------------------\n")
                                            import os
                                            import time
                                            time.sleep(3)
                                            os.system('clear')
                                            congrats='Congratulations!'
                                            print(congrats,"You've survived! You managed to not get kicked out of the game! Nice! Now enjoy the show!")
                                            def moveDuck():
                                                def prYellow(skk): 
                                                    print("\033[93m {}\033[00m" .format(skk))
                                                def prRed(skk): 
                                                    print("\033[91m {}\033[00m" .format(skk))
                                                def ducky():
                                                    import time
                                                    prYellow("    _ ")
                                                    prYellow(" _( ^>")
                                                    prYellow("(____)")
                                                    prYellow(" ")
                                                    prYellow("Ducky\n\n")
                                                    ducky()
                                                def madDuck():
                                                    import time
                                                    prYellow("                         ____________")
                                                    prYellow("                      /               \\")
                                                    prYellow("                     /                 \\")
                                                    prYellow("                    /                    \\")
                                                    prYellow("                   |             \         >>")
                                                    prYellow("                   |            @             >>")
                                                    prYellow("                   |                            >>")
                                                    prYellow("-------------------                           >>")
                                                    prYellow("\                                         >>")
                                                    prYellow(" \                                       /")
                                                    prYellow("  \                                     /  ")
                                                    prYellow("   \                                   /")
                                                    prYellow("    \                                /")
                                                    prYellow("     \                              /")
                                                    prYellow("      ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                            ____________")
                                                    prYellow("                          /               \\")
                                                    prYellow("                         /                 \\")
                                                    prYellow("                        /                    \\")
                                                    prYellow("                       |             \         >>")
                                                    prYellow("                       |            @             >>")
                                                    prYellow("                       |                            >>")
                                                    prYellow("    -------------------                           >>")
                                                    prYellow("    \                                         >>")
                                                    prYellow("     \                                       /")
                                                    prYellow("      \                                     /  ")
                                                    prYellow("       \                                   /")
                                                    prYellow("        \                                /")
                                                    prYellow("         \                              /")
                                                    prYellow("           ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                  ____________")
                                                    prYellow("                                /               \\")
                                                    prYellow("                               /                 \\")
                                                    prYellow("                              /                    \\")
                                                    prYellow("                             |             \         >>")
                                                    prYellow("                             |            @             >>")
                                                    prYellow("                             |                            >>")
                                                    prYellow("         -------------------                           >>")
                                                    prYellow("         \                                         >>")
                                                    prYellow("          \                                       /")
                                                    prYellow("           \                                     /  ")
                                                    prYellow("            \                                   /")
                                                    prYellow("             \                                /")
                                                    prYellow("              \                              /")
                                                    prYellow("               ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                          ____________")
                                                    prYellow("                                        /               \\")
                                                    prYellow("                                       /                 \\")
                                                    prYellow("                                      /                    \\")
                                                    prYellow("                                     |             \         >>")
                                                    prYellow("                                     |            @             >>")
                                                    prYellow("                                     |                            >>")
                                                    prYellow("                 -------------------                           >>")
                                                    prYellow("                 \                                         >>")
                                                    prYellow("                  \                                       /")
                                                    prYellow("                   \                                     /  ")
                                                    prYellow("                    \                                   /")
                                                    prYellow("                     \                                /")
                                                    prYellow("                      \                              /")
                                                    prYellow("                       ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prYellow("                                                      ____________")
                                                    prYellow("                                                    /               \\")
                                                    prYellow("                                                   /                 \\")
                                                    prYellow("                                                  /                    \\")
                                                    prYellow("                                                 |             \         >>")
                                                    prYellow("                                                 |            @             >>")
                                                    prYellow("                                                 |                            >>")
                                                    prYellow("                             -------------------                           >>")
                                                    prYellow("                             \                                         >>")
                                                    prYellow("                              \                                       /")
                                                    prYellow("                               \                                     /  ")
                                                    prYellow("                                \                                   /")
                                                    prYellow("                                 \                                /")
                                                    prYellow("                                  \                              /")
                                                    prYellow("                                    ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    prRed("                                                                 ____________")
                                                    prRed("                                                               /               \\")
                                                    prRed("                                                              /                 \\")
                                                    prRed("                                                             /                    \\")
                                                    prRed("                                                            |             \         >>")
                                                    prRed("                                                            |            @             >>")
                                                    prRed("                                                            |                            >>")
                                                    prRed("                                         -------------------                           >>")
                                                    prRed("                                         \                                         >>")
                                                    prRed("                                         \                                       /")
                                                    prRed("                                           \                                     /  ")
                                                    prRed("                                            \                                   /")
                                                    prRed("                                             \                                /")
                                                    prRed("                                              \                              /")
                                                    prRed("                                                ----------------------------")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')    
                                                    print("                                                        c=====e")                                                 
                                                    print("                                                           H")                                                   
                                                    print(" ____________                                           _,,H__")
                                                    print("(__((__((___()                                        //|     |")
                                                    print("(__((__((___()()_____________________________________// |ACME |")
                                                    print("(__((__((___()()()------------------------------------' |_____|")
                                                    import os
                                                    import time
                                                    time.sleep(1)
                                                    os.system('clear')
                                                    print("                ________________")      
                                                    print("           ____/ (  (    )   )  \___")                  
                                                    print("         /( (  (  )   _    ))  )   )\\")                
                                                    print("        ((     (   )(    )  )   (   )  )")               
                                                    print("       ((/  ( _(   )   (   _) ) (  () )  )")             
                                                    print("      ( (  ( (_)   ((    (   )  .((_ ) .  )_")            
                                                    print("     ( (  )    (      (  )    )   ) . ) (   )")           
                                                    print("    (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")          
                                                    print("   ( (  (   ) (  )   (  ))     ) _)(   )  )  )")          
                                                    print("   ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")         
                                                    print("   (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")          
                                                    print("    ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")         
                                                    print("     ((  (   )(    (     _    )   _) _(_ (  (_ )")          
                                                    print("      (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")           
                                                    print("       ((__)        \\||lll|l||///          \_))")           
                                                    print("                (   /(/ (  )  ) )\   )")                   
                                                    print("              (    ( ( ( | | ) ) )\   )")                  
                                                    print("               (   /(| / ( )) ) ) )) )")                   
                                                    print("            (     ( ((((_(|)_)))))     )")                 
                                                    print("              (      ||\(|(|)|/||     )")                 
                                                    print("            (        |(||(||)||||        )")                
                                                    print("               (     //|/l|||)|\\ \     )")                 
                                                    print("             (/ / //  /|//||||\\  \ \  \ _)")
                                                    print("\n\n\n")
                                                    print("You've killed the ducky. Great job. It's blood is now on your hands. Murderer.")
                                                move=input("Move the ducky? y/n: ")
                                                if move.lower() == "n":
                                                    madDuck()
                                                elif move.lower() == "y":
                                                    def happyDuck():
                                                        import time
                                                        prYellow("                         ____________")
                                                        prYellow("                      /               \\")
                                                        prYellow("                     /                 \\")
                                                        prYellow("                    /                    \\")
                                                        prYellow("                   |              o         >>")
                                                        prYellow("                   |          @               >>")
                                                        prYellow("                   |                            >>")
                                                        prYellow("-------------------                           >>")
                                                        prYellow("\                                         >>")
                                                        prYellow(" \                                       /")
                                                        prYellow("  \                                     /  ")
                                                        prYellow("   \                                   /")
                                                        prYellow("    \                                /")
                                                        prYellow("     \                              /")
                                                        prYellow("      ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                            ____________")
                                                        prYellow("                          /               \\")
                                                        prYellow("                         /                 \\")
                                                        prYellow("                        /                    \\")
                                                        prYellow("                       |             o         >>")
                                                        prYellow("                       |         @               >>")
                                                        prYellow("                       |                            >>")
                                                        prYellow("    -------------------                           >>")
                                                        prYellow("    \                                         >>")
                                                        prYellow("     \                                       /")
                                                        prYellow("      \                                     /  ")
                                                        prYellow("       \                                   /")
                                                        prYellow("        \                                /")
                                                        prYellow("         \                              /")
                                                        prYellow("           ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                  ____________")
                                                        prYellow("                                /               \\")
                                                        prYellow("                               /                 \\")
                                                        prYellow("                              /                    \\")
                                                        prYellow("                             |             o         >>")
                                                        prYellow("                             |         @               >>")
                                                        prYellow("                             |                            >>")
                                                        prYellow("         -------------------                           >>")
                                                        prYellow("         \                                         >>")
                                                        prYellow("          \                                       /")
                                                        prYellow("           \                                     /  ")
                                                        prYellow("            \                                   /")
                                                        prYellow("             \                                /")
                                                        prYellow("              \                              /")
                                                        prYellow("               ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                          ____________")
                                                        prYellow("                                        /               \\")
                                                        prYellow("                                       /                 \\")
                                                        prYellow("                                      /                    \\")
                                                        prYellow("                                     |             o         >>")
                                                        prYellow("                                     |         @                >>")
                                                        prYellow("                                     |                            >>")
                                                        prYellow("                 -------------------                           >>")
                                                        prYellow("                 \                                         >>")
                                                        prYellow("                  \                                       /")
                                                        prYellow("                   \                                     /  ")
                                                        prYellow("                    \                                   /")
                                                        prYellow("                     \                                /")
                                                        prYellow("                      \                              /")
                                                        prYellow("                       ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                      ____________")
                                                        prYellow("                                                    /               \\")
                                                        prYellow("                                                   /                 \\")
                                                        prYellow("                                                  /                    \\")
                                                        prYellow("                                                 |             o         >>")
                                                        prYellow("                                                 |         @                >>")
                                                        prYellow("                                                 |                            >>")
                                                        prYellow("                             -------------------                           >>")
                                                        prYellow("                             \                                         >>")
                                                        prYellow("                              \                                       /")
                                                        prYellow("                               \                                     /  ")
                                                        prYellow("                                \                                   /")
                                                        prYellow("                                 \                                /")
                                                        prYellow("                                  \                              /")
                                                        prYellow("                                    ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        prYellow("                                                                 ____________")
                                                        prYellow("                                                               /               \\")
                                                        prYellow("                                                              /                 \\")
                                                        prYellow("                                                             /                    \\")
                                                        prYellow("                                                            |             o         >>")
                                                        prYellow("                                                            |         @                >>")
                                                        prYellow("                                                            |                            >>")
                                                        prYellow("                                         -------------------                           >>")
                                                        prYellow("                                         \                                         >>")
                                                        prYellow("                                         \                                       /")
                                                        prYellow("                                           \                                     /  ")
                                                        prYellow("                                            \                                   /")
                                                        prYellow("                                             \                                /")
                                                        prYellow("                                              \                              /")
                                                        prYellow("                                                ----------------------------")
                                                        import os
                                                        import time
                                                        time.sleep(1)
                                                        os.system('clear')
                                                        print("You've saved the ducky. Great job! It will now live a happy, peaceful life!") 
                                                    happyDuck()
                                                else:
                                                    print("not a valid response.")
                                            moveDuck()
                                        else:
                                            print(wrgmsg,"\n")
                                            import os
                                            import time
                                            time.sleep(5)
                                            os.system('clear')
                                    else:
                                        print(wrgmsg,"\n")
                                        import os
                                        import time
                                        time.sleep(5)
                                        os.system('clear')
                                else:
                                    print(wrgmsg,"\n")
                                    import os
                                    import time
                                    time.sleep(5)
                                    os.system('clear')
                            else:
                                print(wrgmsg,"\n")
                                import os
                                import time
                                time.sleep(5)
                                os.system('clear')
                        else:
                            print(wrgmsg,"\n")
                            import os
                            import time
                            time.sleep(5)
                            os.system('clear')
                    else:
                        print(wrgmsg,"\n")
                        import os
                        import time
                        time.sleep(5)
                        os.system('clear')
                else:
                    print(wrgmsg,"\n")
                    import os
                    import time
                    time.sleep(5)
                    os.system('clear')
            else:
                print(wrgmsg,"\n")
                import os
                import time
                time.sleep(5)
                os.system('clear')
        else:
            print(wrgmsg,"\n")
            import os
            import time
            time.sleep(5)
            os.system('clear')
'''
Allows user to choose a character
Options are hat ducky and a regular ducky
'''
def charGame():
    def prRed(skk): 
        print("\033[91m {}\033[00m" .format(skk))
    def prGreen(skk): 
        print("\033[92m {}\033[00m" .format(skk))
    def prYellow(skk): 
        print("\033[93m {}\033[00m" .format(skk))
    def prLightPurple(skk): 
        print("\033[94m {}\033[00m" .format(skk))
    import time
    def ducky(yellow,duck):
        yellow("    _ ")
        yellow(" _( ^>")
        yellow("(____)")
        yellow(" ")
        yellow("Ducky\n\n")
        duck=yellow
        return
    ducky(prYellow, 4)
    time.sleep(3)
    def hat_ducky(purple,hat):
        purple("   ┌─┐")
        purple("   | |")
        purple("   ┴─┴")
        purple(" _( ^>")
        purple("(____)")
        purple(" ")
        purple("Hat Ducky\n\n")
        hat=purple
        return
    hat_ducky(prLightPurple, 8)
    time.sleep(3)
    character=input("Choose your character: ").lower()
    if character.lower() == "hat ducky":
        print("You've chosen Hat Ducky.\n\n\n")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        print("Try to answer the following questions without saying 'no'.")
        import os
        import time
        time.sleep(6)
        os.system('clear')
        while 0 < 1:
            q1=input("Do you like cats? y/n: ")
            if q1 == "n":
                print("You lost REALLY fast. Too bad...\n")
                break
            elif q1 == "y":
                print("We ALL know dogs are better.")
                break
            else:
                print("not valid, try again.")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        while 56>2:
            q2=input("Do you pour your milk before your cereal?: ")
            if q2 == "n":
                print("I WIN!")
                break
            elif q2 == "y":
                print("*GASP* You MONSTER!!!")
                break
            else:
                print("not valid, try again.")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        while 1000000000 > 1:
            q3=input("Are you a kid?: ")
            if q3 == "n":
                print("hehe You LOST, I WIN")
                break
            elif q3 == "y":
                print("awwwww, you're so small.")
                break
            else:
                print("not valid, try again.")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        jump=int(input("How many times should the ducky appear?: "))
        for number in range(jump):
            print("   ┌─┐")
            print("   | |")
            print("   ┴─┴")
            print(" _( ^>")
            print("(____)")
            import os
            import time
            time.sleep(1)
            print("Bye! Thanks for playing!")
    elif character.lower() == "ducky":
        print("You've chosen Ducky.\n\n\n")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        print("Try to answer the following questions without saying 'no'.")
        import os
        import time
        time.sleep(6)
        os.system('clear')
        while 0 < 1:
            q1=input("Do you like cats? y/n: ")
            if q1 == "n":
                print("You lost REALLY fast. Too bad...\n")
                break
            elif q1 == "y":
                print("We ALL know dogs are better.")
                break
            else:
                print("not valid, try again.")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        while 56>2:
            q2=input("Do you pour your milk before your cereal?: ")
            if q2 == "n":
                print("I WIN!")
                break
            elif q2 == "y":
                print("*GASP* You MONSTER!!!")
                break
            else:
                print("not valid, try again.")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        while 1000000000 > 1:
            q3=input("Are you a kid?: ")
            if q3 == "n":
                print("hehe You LOST, I WIN")
                break
            elif q3 == "y":
                print("awwwww, you're so small.")
                break
            else:
                print("not valid, try again.")
        import os
        import time
        time.sleep(3)
        os.system('clear')
        jump=int(input("How many times should the ducky appear?: "))
        for number in range(jump):
            print("    _")
            print(" _( ^>")
            print("(____)")
            import os
            import time
            time.sleep(1)
        print("Bye! Thanks for playing!")
    else:
        import time
        print("not a valid answer. try again.")
        time.sleep(1)
        character2=input("Choose your character: ")
        if character2.lower() == "hat ducky":
            print("You've chosen Hat Ducky.\n\n\n")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            print("Try to answer the following questions without saying 'no'.")
            import os
            import time
            time.sleep(6)
            os.system('clear')
            while 0 < 1:
                q1=input("Do you like cats? y/n: ")
                if q1 == "n":
                    print("You lost REALLY fast. Too bad...\n")
                    break
                elif q1 == "y":
                    print("We ALL know dogs are better.")
                    break
                else:
                    print("not valid, try again.")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            while 56>2:
                q2=input("Do you pour your milk before your cereal?: ")
                if q2 == "n":
                    print("I WIN!")
                    break
                elif q2 == "y":
                    print("*GASP* You MONSTER!!!")
                    break
                else:
                    print("not valid, try again.")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            while 1000000000 > 1:
                q3=input("Are you a kid?: ")
                if q3 == "n":
                    print("hehe You LOST, I WIN")
                    break
                elif q3 == "y":
                    print("awwwww, you're so small.")
                    break
                else:
                    print("not valid, try again.")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            jump=int(input("How many times should the ducky appear?: "))
            for number in range(jump):
                print("   ┌─┐")
                print("   | |")
                print("   ┴─┴")
                print(" _( ^>")
                print("(____)")
                import os
                import time
                time.sleep(1)
                print("Bye! Thanks for playing!")
                print("Bye! Thanks for playing!")
        elif character2.lower() == "ducky":
            print("You've chosen Ducky.\n\n\n")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            print("Try to answer the following questions without saying 'no'.")
            import os
            import time
            time.sleep(6)
            os.system('clear')
            while 0 < 1:
                q1=input("Do you like cats? y/n: ")
                if q1 == "n":
                    print("You lost REALLY fast. Too bad...\n")
                    break
                elif q1 == "y":
                    print("We ALL know dogs are better.")
                    break
                else:
                    print("not valid, try again.")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            while 56>2:
                q2=input("Do you pour your milk before your cereal?: ")
                if q2 == "n":
                    print("I WIN!")
                    break
                elif q2 == "y":
                    print("*GASP* You MONSTER!!!")
                    break
                else:
                    print("not valid, try again.")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            while 1000000000 > 1:
                q3=input("Are you a kid?: ")
                if q3 == "n":
                    print("hehe You LOST, I WIN")
                    break
                elif q3 == "y":
                    print("awwwww, you're so small.")
                    break
                else:
                    print("not valid, try again.")
            import os
            import time
            time.sleep(3)
            os.system('clear')
            jump=int(input("How many times should the ducky appear?: "))
            for number in range(jump):
                print("    _")
                print(" _( ^>")
                print("(____)")
                import os
                import time
                time.sleep(1)
            print("Bye! Thanks for playing!")
        else:
            print("Game will restart. Hit ""Run"" and try again.")
'''
Makes user input a password in order to continue
Password is 28
'''
def guessGame():
    import time
    #Green color
    def prGreen(skk): 
        print("\033[92m {}\033[00m" .format(skk))
    #Yellow Color
    def prYellow(skk): 
        print("\033[93m {}\033[00m" .format(skk))
    #Light Purple Color
    def prLightPurple(skk): 
        print("\033[94m {}\033[00m" .format(skk))
    #Ask to play game
    user= input("Would you like to play a game? y/n:  ")
    #Rejection
    if user != "y":
        print("Goodbye. *sadly waves* ")
    #Play
    elif user.lower() == "y":
        print("Yay!")
        #Create a guessing game
        import time
        guess=print("But in order to continue, you need to put in a password. It is a single number between 1 and 100.")
        time.sleep(5)
        
        while 0 < 28:
            userG=int(input("Your password: "))
            if userG == 28:
                print("Correct! Now as a reward, enjoy this ducky light show!")
                rainbow()
            else:
                print(userG)


print("\t\t\t\tWHO SAID IT? FUN RANDOM QUIZZES AND GUESSING GAME")
print("                               --------------------------------------------------\n\n\n\n")
print(" Loading.....")
import os
import time
time.sleep(5)
os.system('clear')
'''
Topics and allows for user input on which one they'd like to play.
Displays topics
user input
if statement to determine the game to play
'''
print("\t\t\t\tTopics")
print("\t\t\t\t------")
print(" 1) Age Game\n 2) "'Who Said it'" Quiz\n 3) Choose Your Character and Random Questions Quiz\n 4) Guess the Password\n 5) See Some Random Colorful Duckies\n ")
task=int(input("Your answer: "))
import os
import time
time.sleep(1)
os.system('clear')
print("Loading....")
if task == 1:
    import os
    import time
    time.sleep(5)
    os.system('clear')
    yearsOld()
elif task == 2:
    import os
    import time
    time.sleep(5)
    os.system('clear')
    easy()
elif task == 3:
    import os
    import time
    time.sleep(5)
    os.system('clear')
    charGame()
elif task == 4:
    import os
    import time
    time.sleep(5)
    os.system('clear')
    guessGame()
elif task == 5:
    import os
    import time
    time.sleep(5)
    os.system('clear')
    rainbow()
else:
    print('not a valid answer.')
'''
Displays all of the websites used to produce the program
'''
def credits():
    print("         CREDITS")
    print("         -------")
    print("\n\n https://www.keepinspiring.me//famous-quotes/ \n\n https://www.brainyquote.com/authors/john-locke-quotes \n\n https://entertainism.com/famous-cartoon-quotes \n\n https://kidadl.com/quotes/best-cartoon-quotes-that-everyone-will-love \n\n https://kidadl.com/quotes \n\n ://www.geeksforgeeks.org/print-colors-python-terminal/ \n\n https://www.asciiart.eu/weapons/explosives \n\n\n\n")
credits()
import os
import time
time.sleep(5)