#David Guerrero
#Program that recites proverbs
def welcome():
    print'Hello, this is a program that recites popular proverbs'
welcome()
try:
        question = raw_input("Enter an integer between 1 to 10: ")
        int(question)
        if question == "1":
            print "You have chosen " + question 
            print "\"Don't put all your eggs in one basket.\""
            print"Have a backup plan. Don't risk all of your money or time in one plan."
        elif question == "2":
            print "You have chosen " + question 
            print "\"Two heads are better than one.\""
            print"When two people cooperate with each other, they come up with better ideas."
        elif question == "3":
            print "You have chosen " + question 
            print "\"The grass is always greener on the other side of the hill.\""
            print"People tend to want whatever they don't have."
        elif question == "4":
            print "You have chosen " + question 
            print "\"Do unto others as you would have them do unto you.\""
            print"Don't do mean things to people."
        elif question == "5":
            print "You have chosen " + question 
            print "\"A chain is only as strong as its weakest link.\""
            print"If one member of a team doesn't perform well, the whole team will fail."
        elif question == "6":
            print "You have chosen " + question 
            print "\"Honesty is the best policy.\""
            print"Don't lie."
        elif question == "7":
            print "You have chosen " + question 
            print "\"Absence makes the heart grow fonder.\""
            print"Sometimes it's good to be away from your partner, because it makes you want to see each other again."
        elif question == "8":
            print "You have chosen " + question 
            print "\"You can lead a horse to water, but you can't make him drink.\""
            print"If you try to help someone, but they don't take your advice or offers, give up. You can't force someone to accept your help."
        elif question == "9":
            print "You have chosen " + question 
            print "\"Don't count your chickens before they hatch.\""
            print"Your plans might not work out, so don't start thinking about what you'll do after you succeed. Wait until you've already succeeded, and then you can think about what to do next."
        elif question == "10":
            print "You have chosen " + question 
            print "\"If you want something done right, you have to do it yourself.\""
            print"Don't trust other people to do important things for you. You have to do things yourself to control the quality of the results."
except:
    print 'Program failure. Please enter an integer between 1 and 10 next time.'
