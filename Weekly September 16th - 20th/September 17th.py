#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#............Looping Through A Dictionary Continued............#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#***********************************#
#           Projects             #
#***********************************#

words_count = {}
words = input("Create a list of words").split()
for word in words:
	if word not in words_count:
		words_count[word] = 0
	words_count[word] += 1

print(max(words_count, key=words_count.get))

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

n = int(input("How many keys in your dictionary?"))
dictionary = {}
for i in range(n):
    dictionary[i] = i**2

print(dictionary)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

length = int(input("How many pairs do you want in your thesarus? "))
thesarus = {}

for i in range(length):
    key = input("Any real word ")
    value = input("Synonym for {} ").format(key)
    if key not in thesarus:
        thesarus[key] = value
        thesarus[value] = key

print(thesarus[input("Which word do you want the synonym for?")])

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

rounds = int(input("How many data points are there?"))
vote_list = {}

for i in range(rounds):
    candidate = input("Name of candidate? ")
    number_votes = int(input("How many votes for that candidate? "))
    if candidate not in vote_list:
        vote_list[candidate] = number_votes
    else:
        vote_list[candidate] += number_votes

print(vote_list)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#...........................Tuples...............................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
NOTES
Tuples are unchangable 
instruments = ("Clarinet", "Piano", " Drum", "Violin")
print(instruments)
output ( 'Clarinet' , 'Piano' , 'Drum' , 'Violin' )
might look like a list but note the use of parenthesis
acessing Tuple Items
instruments = ("Clarinet", "Piano", " Drum", "Violin")
print(instruments[1])
output ('Piano')
Negative indexing 
instruments = ("Clarinet", "Piano", " Drum", "Violin")
print(instruments[-1])
output ('Violin')
Accessing a range of indexes
instruments = ("Clarinet", "Piano", " Drum", "Violin", "Guitar")
print(instruments[1:3])
output ('Piano', 'Drum')
can't add or remove from tuples
but can check for items
Checking for an Item in tupes
instruments = ("Clarinet", "Piano", " Drum", "Violin", "Guitar")
if "Piano" in instruments:
    print("The tuple contains the value of piano")
else:
    print("The tuples does not contain the value of piano")
output( The tuple contains the value of piano )

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

grades = ( 95, 70, 85, 92, 100 )
print(grades)
print(grades[-2])
print(grades[0:3])

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#***********************************#
#           Projects             #
#***********************************#

friends = (3, 5, 7, 8, 10, 2, 12, 4)
choice = int(input("random number"))

if choice in friends:
    print("Yes")
else:
    print("No")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

tuples = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuples[-3])
print(tuples[5])
print(tuples[0:4])

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

candies = (3, 5, 7, 8, 10, 2, 50, 4, 29, 14)
print(candies[-4:-1])

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#.......................Reading Files............................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
NOTES
Lets say you have been given a large folder with 10,000 text files, and been assigned to change all the names of the text files to 'file1.txt', file2.txt and so on.
With Python, you could write a short, simple program that can make all those changes in a matter of seconds! 

a text file is a file with information inside it. 
they dont take up a lot of space and thus very useful
typically large databases store storage in files to minimize space

file1 = open("example.txt", "r")
# r = read 
# open means as it means > then name the file 
#to print the contents of the file you have to use read() funtion

print(file1.read())

file.close()

#***********************************#
#           Projects             #
#***********************************#

file1 = open("cobra.txt", "r")

print(file1.read())

file1.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

file1 = open("speech.txt", "r")

print(file1.read())

file1.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#..................Reading Parts of a Files......................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
NOTES
file1 = open("example.txt", "r")
#the example file has the alphabet 
#the (5) is telling the code to only print 5 letters

print(file1.read(5))

file1.close()


there is something calle the readline() funtion 
basically telling the code to read entire lines of text in a file 

ex 
Hello, This si a test file for Skill Struck students!
I hope you're enjoying the class so far.
Have you learned anything interesting?
The skills you're gaining are very valuable!

file = open("example.txt", "r")
print(file.readline())

this code opens the file and reads the fist line in that file 
output (Hello, This si a test file for Skill Struck students!)

what if yo has two readline funtions?

file = open("example.txt", "r")
print(file.readline())
print(file.readline())

output(Hello, This si a test file for Skill Struck students!
I hope you're enjoying the class so far.)

to return the lines to the file 
use 

readline(s)  = readlines 
NOT readline (no s)

closing files = file.close()

file = open("example.txt", "r")
print(file1.read(10))
print(file1.readline())
print(file1.readline())
file1.close()

#***********************************#
#           Projects             #
#***********************************#

file = open("example.txt", "r")
choice = int(input("number"))

print(file.read(choice))

file.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
