#classmates = { "Bob" : 2, "Sydney" : 3, "Joan" : 7, "Lindsey" : 9, "Tim" : 10}

#for x in classmates:
    #print(x)

#classmates = { "Bob" : 2, "Sydney" : 3, "Joan" : 7, "Lindsey" : 9, "Tim" : 10}

#for x in classmates.values():
    #print(x)

#x = key . y = value
#but only applies when printing both 

#classmates = { "Bob" : 2, "Sydney" : 3, "Joan" : 7, "Lindsey" : 9, "Tim" : 10}

#for x,y in classmates.items():
    #print(x,y)

#measurement = {"length" : 9, "width" : 10, "depth" : 8}
#for x in measurement.values():
    #print(x)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#group = { "Fred" : 12, "Jackson" : 15, "Sophie" : 20, "Amanda" : 0, "Jane" : 0,}
#Jane and Amanda group's are currently unknown

#Amanda_group = int(input("How many people are in Amanda's group? "))
#Jane_group = int(input("How many people are in Jane's group? "))

#program ask user for amount of poeple in their groups 

#group["Amanda"] = Amanda_group
#group["Jane"] = Jane_group

#total = 0

#for x in group.values():
    #total += x 

#print(total)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#number = int(input("choose a number between 0 and 100 "))
#value = int(input("choose a number between 0 and 100 "))

#group = { 3 : 10, 5 : 3, 10 : 6, 4 : 30, "first" : "second" }

#group.pop("first")
#group[number] = value

#product = 0

#for x,y in group.items():
    #product += x*y

#print(product)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#group = { "box1" : 5, "box2" : 2, "box3" : 10, "box4" : 3, "box5" : 0 }

#box_five = int(input("choose a number between 1 and 10"))

#group["box5"] = box_five

#total_volume = 0

#for x in group.values():
    #total_volume += x * 25

#print(total_volume)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#group = { "Sally" : 10, "Cameron" : 3, "Spencer" : 6, "random" : 0 }

#name = input("Type in a name")
#pairs = int(input("input a number from 1 to 10"))

#group.pop("random")
#group[name] = pairs

#for x,y in group.items():
    #answer = "{} has {} pairs of shoes.".format(x,y)
    #print(answer)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#group = { 4: "Jared", 5: "McKann", 6: "Kyle", 7: "Summer", 8: "replace", }

#name = input("choose a random name")

#group[8] = name
#for x in group:
    #group[x] = group[x] + " Nelson" 
#print(group)

print("stay")