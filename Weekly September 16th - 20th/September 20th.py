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

file = open("letter.txt", "a")
file.write("From your Pen Pal")
print(file.read())
file.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

file = open("Gandhi.txt", "a")
file.write("Quote was said by Gandhi")
print(file.read())
file.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

response = input("what would you like to add? ")
file = open("report.txt", "a")
file.write(response)
print(file.read())
file.close

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#........................File Write Mode.........................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
NOTES
before we learned about appending and how it can add to a file 
this time for write mode we completely overwrite it and replace it with a new sentence 

its similar to appending file 

file = open("example.txt", "w")  #notice "w" instead of "a" or "r"
file.write("This line will replace everything in the file")
print(file.read())
file.close()

did you know both apppend and write mode can create a new file?

this is how

file = open("new_document.txt", "w") #(THE NEW_DOCUMENT is going to make a file names tha since it dosen't exist)

file2 = open("report.txt", "w")
file2.write("In short, I love to code!")
print(file2.read())
file2.close()

file1 = open("porcupine.txt", "w")


#***********************************#
#           Projects             #
#***********************************#

file2 = open("email.txt", "w")
file2.write("Never mind")
print(file2.read())
file2.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

answer = input("what do you want to say?")
file2 = open("report.txt", "w")
file2.write(answer)
print(file2.read())
file2.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#........................Nested For Loops........................#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
NOTES
nested loops are for when you use a for loop inside of another loop 
this is hat we did in a previous lesson to creat a 1D list 


the code example
n = 5 
list = []
for i in range(n):
    list.append(i)
print(list)

output = [0, 1, 2, 3, 4]

to creat a 2D list use this code
2D list is a list inside a list 

#two list "rows" and "cols"

#also an empty list that is named list1

#the i in row
rows = 5
cols = 5
list1 = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(j)
    list1.append(col)
print(list1)
#***********************************#
#           Projects             #
#***********************************#