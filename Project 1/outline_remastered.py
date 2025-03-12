import random

def enter():
    input()

def cc(x): #cc = closed caption
    print(x)
    enter()
    
def beginnings():
    cc("Hello, welcome to the game")
    cc("You're Adam")
    cc("Now you can choose your own life")
    cc("In this game you're allowed to make choices")
    cc("Each different choices will lead you to different life outcomes")
    cc("Only one of these roads is what Adam had taken in real life")
    cc("Enjoy this game!")
    cc("Loading...(You only have to press enter on this prototype)")
    cc("You are in high school now. Grade 7.")
    
def notFamous():
    cc("You're abandoned among classmates")
    cc("Adolescence come. You feel specifcally attached to 2 girls. ZTR and Emma")
    
def ZTR():
    cc("At first it was only a secret")
    cc("But it became so burning hot that you cannot hide it anyway")
    cc("You decide to confess your love to her")
    cc("But unluckily you're declined")
    cc("Soon after, you have to decide between 2 senior high schools")
    cc("School A, an ordinary school, and School B, an international one")
    
def schoolA():
    cc("You've entered School A")
    cc("There you met Ms Q")
    cc("She's so dangerously charming")
    cc("But you still love ZTR so much")
    cc("It hurts but you have to forget about Q")
    cc("Meanwhile through hooking up with Q, you met Mr K")
    cc("Frankly speaking he's a bastard, but he's also a good friend of ZTR")

def giveup():
    cc("Days are so hard with person you love doesn't love you at all")
    cc("While your patience is winding down")
  
def YL():
    cc("At some point you met YL, another charming girl")
    cc("This time you're bound to be trapped")
    cc("You talk to her online day and night")
    cc("And a few encounters can make your day better")
    cc("You decide to give up on ZTR and go for this person")
    cc("And so you did")
    
def declinedYL():
    cc("But unfortunately, you got declined")
    cc("Things are getting wild")
    cc("She declined you but still would talk to you and date you")
    cc("You don't understand why but you're glad")
    cc("That she's actually become your girlfreind")
    cc("You love her so much")
    
def betrayAug():
    cc("But one day, you discovered that she's out with other boys")
    cc("You're betrayed or fooled")
    cc("You forget everything about her and began you new life")
    cc("Months later, you met Ms H online")
    cc("She's living a Canada")
    cc("You can tell from chats that she's so passionate and inncocent")
    cc("One day she invited you to visit her")
    
def H():
    cc("The flight took off for Calgary...")

def notH():
    cc("The story between you and H just ends online...")
    
def endings():
    cc("############")
    cc("5 years later...")
    cc("You're in a church somewhere in Massachusetts")
    cc("It's your wedding day")
    cc("Outside are the fireworks")
    cc("You see through the firework, and see the fireworks 10 years ago")
    cc("Which was on another couple's wedding")
    cc("And then you're passing by")
    cc("At the first day of your high school")
    
def betrayLater():
    cc("You're in different cities for college, but you manage to keep the love")
    cc("Or at least, keep the love on your side")
    cc("She wanna go to North America and so do you")
    cc("So you take her Canada after graduating")
    cc("You're working in the US while she study in Canada")
    cc("You marry her, in order that she can move in the US")
    cc("Finally you can create a home")
    cc("You decide to have a real wedding")
    cc("But just one day before the wedding day")
    cc("She dissapeared, with the ring, with you bewildered")
    cc(" \"She must have been hooked up with someone else\", you think")
    cc("But that doesn't make up for all your days in darkness, for settle this home down")
    cc("And above all, you loved her so much")
    cc("You sat down and cry in the your newly built house, on the bed that still smells like her")
  
def notdeclinedYL():
    cc("You're glad that she accepted your confession")
    cc("You two are passionately in love")
    cc("More than anyone else could've imagined")
    cc("You spend a whole summer overwhelmed by happiness")
    
def K():
    cc("Choosing to befriend K, who is close to ZTR, turns out to be a pivotal decision.")
    cc("Your friendship with K opens a new door; you find yourself in ZTR's social circle, gradually getting closer to her.")
    cc("Over time, this proximity helps kindle a relationship between you and ZTR.")
    cc("At first, everything seems like a dream come true. You share moments of joy, laughter, and mutual affection.")
    cc("But as the days turn into months, you start facing the realities of a relationship.")
    cc("Differences in interests, priorities, and perspectives begin to surface.")
    cc("Despite your best efforts, these small cracks widen, leading to misunderstandings and arguments.")
    cc("You both try to bridge the gap, but the emotional distance grows, making it harder to connect as you once did.")
    cc("Eventually, the strain takes its toll, and you both realize that things aren't working out.")
    cc("The breakup is painful")

def schoolB():
    cc("You've chosen School B, the international school.")
    cc("Here, you find a diverse group of students from all around the world.")
    cc("This new environment challenges you but also opens up a world of opportunities.")
    cc("You join various clubs and start to develop a new set of interests and skills.")
    cc("Your confidence grows, and you start participating in competitions.")
    cc("In one of these competitions, you meet a mentor who guides you in your academic journey.")
    cc("You are heading towards an international college, in Canada")
    
def Emma_notfamous():
    cc("Choosing a quieter life, you embrace being a 'nerd'.")
    cc("Which means you never really connect with Emma.")
    cc("She remains an unattainable figure, a reminder of what might have been.")
    cc("Your journey takes a different turn, filled with personal achievements but also a tinge of 'what if'.")
    cc("You learn to find contentment in your own company and in the pursuit of knowledge.")
    
def Emma_famous_declined():
    cc("In your pursuit of popularity, you gather the courage to confess your feelings to Emma.")
    cc("However, she does not reciprocate, leaving you in a state of rejection and self-reflection.")
    cc("This experience becomes a turning point, leading you to reassess your priorities.")
    cc("You begin to focus more on genuine connections rather than social status.")
    cc("This new mindset opens up a path of self-discovery and meaningful relationships.")

def Emma_famous_notdeclined():
    cc("As a popular and charismatic figure, you capture Emma's attention and affection.")
    cc("She is attracted to your outgoing personality and zest for life.")
    cc("Emma generously shares her world with you")
    cc("You both go to Canada, enjoying a life of freedom and happiness")
    cc("However, as time passes, you find yourself drifting away from her.")
    cc("You make the difficult decision to leave Emma, seeking a different path for your life.")
    
def DLC():
    cc("############")
    cc("Below are exclusive contents")
    cc("You are now in Canada, a place of interest and ferment")
    cc("You enter the top school and can finally live the life you want")
    cc("And most importantly, even air here smells like love")
    cc("You cannot wait to go out for social")
    cc("One day at a party, you meet YL, a charming girl who is also from China")
    cc("You ask her for contact and talk to her day and night")
    cc("Of course, just online")
    cc("As days pass, your conversations with YL become the highlight of your day.")
    cc("You find her intriguing, not just for her charming looks, but for her intellect and wit.")
    cc("She shares your love for literature and music, creating a deep, invisible bond.")
    cc("One day, you decide to take a leap of faith and ask her out on a real date.")
    cc("To your delight, she agrees. The plan is simple: a walk along the beautiful streets of the city, followed by dinner.")
    cc("The date is magical. You both discover the joy of each other's company outside the digital world.")
    cc("Her laughter is more melodious in person, her insights more profound.")
    cc("You feel a connection that's rare and special, something that goes beyond mere attraction.")
    cc("As the evening ends, you realize you don't want it to. You ask her if she feels the same way, and she smiles and nods.")
    cc("One crisp autumn evening, as the sunset paints the sky in hues of orange and gold, you take her to the place where you first met.")
    cc("Your heart races as you reach into your pocket.")
    cc("With a deep breath, you kneel before her")
    cc("You pulled out a ring...")

    
####################
  
beginnings()
#with open("hello.txt", 'r') as file:
    #print(file.read())


while True:
    answer=input("You're trying to be famous among guys:\n")
    if answer.lower() == "no":
        notFamous()
        
        while True:
            answer=input("You have to choose one:\n")
            if answer.lower() == "ztr":
                ZTR()
                
                while True:
                    answer=input("Your choice?\n")
                    if answer == "A":
                        schoolA()
                        
                        while True:
                            answer=input("But if you're going to make friends with him?:\n")
                            if answer.lower() == "yes":
                                K()
                                break
                            elif answer.lower() == "no":
                                giveup()
                                break
                            else:
                                print("invalid answer, try again")
                        
                        YL()
                        chance=random.random()
                        if chance > 0.5:
                            declinedYL()
                            chance=random.random()
                            if chance > 0.5:
                                betrayAug()
                                
                                while True:
                                    answer=input("You choose to go or not:\n")
                                    if answer.lower() == "yes":
                                        H()
                                        break
                                    elif answer.lower() == "no":
                                        notH()
                                        break
                                    else:
                                        print("invalid answer, try again")
                                
                            else:
                                betrayLater()
                        else:
                            notdeclinedYL()
                            betrayLater()
                                
                        break
                    elif answer == "B":
                        schoolB()
                        DLC()
                        break
                    else:
                        print("invalid answer, try again")
                    
                break
            elif answer.lower() == "emma":
                Emma_notfamous()
                schoolB()
                DLC()
                break
            else:
                print("invalid answer, try again")
        
        break
    elif answer.lower() == "yes":
        chance=random.random()
        if chance > 0.5:
            Emma_famous_declined()
            schoolB()
            DLC()
        else:
            Emma_famous_notdeclined()
            DLC()
        break
    else:
        print("invalid answer, try again")

endings()