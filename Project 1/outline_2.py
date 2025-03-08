import random

def enter():
    input()

def cc(x): #cc = closed caption
    print(x)
    enter()
    
def beginnings():
    cc("Hello, welcome to the game")
    cc("You're Adam Cai")
    cc("Now you can choose your own life")
    cc("In this game you're allowed to make choices")
    cc("Each different choices will lead you to different life outcomes")
    cc("Only one of these roads is what Adam Cai had taken in real life")
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
    
def YL():
    cc("Days are so hard with person you love doesn't love you at all")
    cc("While your patience is winding down")
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
    cc("still on it stay tuned for more")
    
def K():
    cc("still on it stay tuned for more")

def schoolB():
    cc("still on it stay tuned for more")
    
def Emma_notfamous():
    cc("still on it stay tuned for more")
    
def Emma_famous_declined():
    cc("still on it stay tuned for more")
    
def Emma_famous_notdeclined():
    cc("still on it stay tuned for more")
    
def DLC():
    cc("still on it stay tuned for more. This feature is only available after purchase")
    
####################
  
beginnings()

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
                                    answer=input("You choose to go or not:")
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