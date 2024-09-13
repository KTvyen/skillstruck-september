#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#.............Looping Through A Dictionary Continued............#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#***********************************#
#           Projects             #
#***********************************#

#looping through a dictionary is already super cool but when combined with other code like and if statement it becomes even more useful !

#for example 
classmates = {
    "Billy" : 8,
    "Vance" : 12,
    "Alice" : 10,
    "Eliza" : 15,
    "Xaxier" : 6,
}

for x in classmates:
    if x == "Eliza":
        print("this person wiches to be annoymous")
    else:
        print(x)