#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#..................Reading Parts of a Files......................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#***********************************#
#           Projects             #
#***********************************#

data = open("example.txt", "r")
words = file.read(data)
split = words.split( )
print(len(split))
words.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

data = open("example.txt", "r")
words = file.read(data)
length = len(data.readlines())
print(length)
words.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#................Append a Line to a Text File...................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
NOTES
two ways to append lines in python 

1 appended
2 is overwrite 

open (specifies what you are doing with the file)
ex:
file = open("example.txt", "r")

r = read
a = append
w = write

to append you do this

file = open("example.txt", "a")

to add new line do this 

file = open("example.txt", "a")
file.write("This is a new line")
file.close 

file should look like this:
hello skill struck students. 
This is a new line

file = open("example.txt", "a")
file.write("I love programming!")
file = open("example.txt", "r")
print(file.read())
file.close()

#***********************************#
#           Projects             #
#***********************************#