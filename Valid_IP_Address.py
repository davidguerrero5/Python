#Valid IP Address
#David Guerrero 
str1 = '192.168.1.100'
str2 = '100.200.300.10'
delimiter = '.'
nodots1 = str1.split(delimiter)
nodots2 = str2.split(delimiter)
intlist1 = map(int, nodots1)
intlist2 = map(int, nodots2)
counter = 1
for num in intlist1:
    if num <= 255 and num >= 0:
        print 'Number',counter,'is good'
        counter = counter + 1
    else:
        print 'Number',counter,'is no good'
        counter = counter + 1
print ' '
counter = 1        
for num in intlist2:
    if num <= 255 and num >= 0:
        print 'Number',counter,'is good'
        counter = counter + 1
    else:
        print 'Number',counter,'is no good'
        counter = counter + 1