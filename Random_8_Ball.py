#David Guerrero
#UAlbany random 8-Ball
import random
import time

try:
    ans = True
    
    while ans:
        question = raw_input("Think of a question: ")
    
        answer = random.randint(1,10)
        time.sleep(5)
        if question == "":
            sys.exit()
    
        elif answer == 1:
            time.sleep(5)
            print "Certainly!"
    
        elif answer == 2:
            time.sleep(5)
            print "Of course"
    
        elif answer == 3:
            time.sleep(5)
            print "It will definitely happen"
    
        elif answer == 4:
            time.sleep(5)
            print "The answer is....YES!"
    
        elif answer == 5:
            time.sleep(5)
            print "Try again"
    
        elif answer == 6:
            time.sleep(5)
            print "Answer unclear, try again"
    
        elif answer == 7:
            time.sleep(5)
            print "Not sure"
    
        elif answer == 8:
            time.sleep(5)
            print "Nope"
        
        elif answer == 9:
            time.sleep(5)
            print "It will not happen"
            
        elif answer == 10:
            time.sleep(5)
            print "The answer is no"
except:
    print 'You have quit the program'