#David Guerrero
#Long word counter

word ='PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS'
value = str(len(word))
print "The amount of letters in",word,"is",value
print "The first five letters in",word,"is",word[0:5]
vowels = "aeiou"
for v in vowels:
    print v, word.lower().count(v)