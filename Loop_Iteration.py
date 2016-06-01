#David Guerrero
#For loop that iterates 200 times and tells user the largest number
 
import random
 
numbers = random.sample(range(1, 1000), 200)
# Create a largest variable
largest = None
for num in numbers:
    print 'The largest integer so far is: ', largest
    if num > largest:
        largest = num
        print 'The new largest integer so far is:  ', largest, '\n'