#David Guerrero
#Change all words to lower case, tokenize words, for loop to count and print words and letters, capitalize method
wrd = "Be the change that you wish to see in the world"

print wrd.lower()
nword = wrd.strip()
nnword = wrd.split()
print nnword
count = 0
for word in nnword:
    count += 1
    print word
    print 'Word count =',count
count = 0
aword= 'quindecasyllabic'
letters = aword.split()
for letters in aword:
    count += 1
    print letters
    print 'Letter count =',count

print aword.capitalize()