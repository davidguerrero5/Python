#David Guerrero
#Kilometers per hour to miles per hour
try:
kmph = raw_input('Enter km per hour: ')
k = float(kmph)
mph = 0.6214*k
    strmph = str(mph)
print('Your speed is ' + strmph + ' miles per hour when you are going ' + kmph + ' km per hour.')
except:
    print 'Bad data!'