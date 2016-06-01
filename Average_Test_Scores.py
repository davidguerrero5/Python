#David Guerrero
#Calculate the average of three test scores

testScore = 0
testSum = 0
amtscores = 0
f = 'fin'
while amtscores < 4:
    testScore = float(raw_input('Test score(type fin to quit): '))
    amtscores = amtscores + 1
    testSum = float(testSum + testScore)
    if testScore < 0:
        print 'Negative number, exiting the loop'
        break
    if testScore == f:
        print 'Exiting the loop'
        break
    if amtscores == 3:
        avg = float(testSum/3)
        print'The average for all of your tests is', avg
        break
