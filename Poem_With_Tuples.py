#Working with tuples, printing out Emily Dickinson, extraordinary American poet, was born on 10 December 1830, in Amherst, Massachusetts.
#David Guerrero

poet = ('Dickinson', 'Emily', 'December 10, 1830', 'Amherst, Massachusetts', 'extraordinary American poet')
lastname, firstname, birthdate, birthplace, description = ('Dickinson', 'Emily', 'December 10, 1830', 'Amherst, Massachusetts', 'extraordinary American poet')
fullname = poet[1] + " " + poet[0]

date = birthdate
date = date.replace(',','')
date = date.split()
month,day,year = date
date = day,month,year


print fullname + ',',description + ', ' + 'was born on',day,month,year + ', in',birthplace+ '.'