from animals import Dog
from animals import Cat
from animals import Bird

fo = open('animals.csv','r')
theline = fo.readlines()
print('line =\n',theline)
fo.close()

myclasses = []
names = []
dobs = []
colours = []
breeds = []

for line in theline:
    splitline = line.split(',')
    myclasses.append(splitline[0])
    names.append(splitline[1])
    dobs.append(splitline[2])
    colours.append(splitline[3])
    breeds.append(splitline[4])

for i in range(len(myclasses)):
    print('Animal', myclasses[i],'= ' , myclasses[i],' ,',names[i],' ,',dobs[i], ' ,', colours[i],' ,',breeds[i], '\n')
#print('splitlines= ',splitline)
'''
dude = Dog('dude', '1/1/2011', 'Brown', 'Jack Russell')
oogs = Cat('Oogie', '1/1/2006', 'Grey', 'Fluffy')
bbird = Bird('Big Bird', '1/1/1969', 'Yellow', 'Canary')

dude.printit()
oogs.printit()
bbird.printit()
'''
#print(garfield)
