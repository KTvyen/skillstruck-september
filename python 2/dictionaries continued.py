#when counta=ing the items in a list (like pylist) the counting length stars at 1

#example of this 
#classmates = {"Hello" : 0, "Jleo" : 7, "kal" : 9, "welxcome" :10}
#print(len(classmates))
#will print 4 becasue thats the number of items in the list if its starts countaing at 1

#you can also check for a key in a vaule (reminer (key: value))


#dino = {"t rex" : 50, "long neck" : 100, "raptor" : 15, "triceratops"  : 30}

#if "t rex" in dino: 
    #print("t rex is in youe dictionary")

#checks for t rex and will only print that staement if it is in the dictionary

#you can also he opposite 


#dino = {"t rex" : 50, "long neck" : 100, "raptor" : 15, "triceratops"  : 30}

#if "rhino" not in dino: 
    #print("rhino is not in your dictionary")

#will print rhino is not in your dictinary 


#you can convert a py list to a py dictionary 

#example 

#garden = ["pumkin", "squash",  "corn", "tomatoes"] 
#garden_dictionary = dict.fromkeys(garden, "Harvested")
#break down the code (set a dictionary ) with dict, name the list (garden) use fromkeys uses the list to set a vaule to all  the keys (garden, "vaule") in he second place is the vaule that will be set to all keys in the dictionary 
#print(garden_dictionary)

#coins = {"pennies" : .01, "nickels" : .05 , "dimes" : .1, "quarters" : .25}
#coins["silvar dollar"] = 1
#coins.pop("pennies")
#print(coins)
#print(len(coins))

#dictionary = { 1: "bicycle", 2: "soccer balls", 3: "piano books", 4 : "", 5 : "" , 6 : ""}

#num4 = input("an item you have")
#num5 = input("an item you have")
#num6 = input("an item you have")

#dictionary[4] = num4
#dictionary[5] = num5
#dictionary[6] = num6

#print(dictionary)

#work = { "Monday" : 3, "Tuesday" : 5, "Wednesday" : 0, "Thursday" : 2, "Friday" : 1}

#work["Saturday"] = 4
#work.pop("Wednesday")
#print(len(work))
#if "Friday" in work:
    #print("Friday is in the dictionary")

#my_list = [str(n) for n in input().split()]
#seen = {}
#for x in my_list:
    #if x not in seen:
        #seen[x] = 1
    #else:
        #seen[x] += 1
    #print(seen[x])

#have_fruit = { "apples" : 5, "bananas" : 7, "strawberries" : 3}

#apples_num = int(input("how many apples do you need? "))
#bananas_num = int(input("how many bananas do you need?"))
#strawberries_num = int(input("how many strawberries do you need?"))

#shopping = {}

#if have_fruit["apples"] < apples_num:
    #shopping["apples"] = apples_num - have_fruit["apples"]
#if have_fruit["bananas"] < bananas_num:
    #shopping["bananas"] = bananas_num - have_fruit["bananas"]
#if have_fruit["strawberries"] < strawberries_num:
    #shopping["strawberries"] = strawberries_num - have_fruit["strawberries"]

#print(shopping)

#permission = [str(n) for n in input("Input a list of names separated by spaces").split()]

#permission_dictionary = dict.fromkeys(permission, "yes")

#if "George" in permission_dictionary:
   # permission_dictionary["George"] = "no"
#if "Veronica" in permission_dictionary:
   # permission_dictionary.pop("Veronica")

#print(permission_dictionary)

print("stay")