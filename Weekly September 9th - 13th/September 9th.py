#making a input question that allows users to pick between two options 
#also allows user to change their answer once

choice = input("Would you like to make a cookie?  [ yes or no ] ").lower()

if choice == "no":
    print("goodbye")

name = " "
check = " "
cookie_pick = " "

if choice == "yes":
    print("""That's great! We can make two types of cookies!
    a) Chocolate Swirl
    b) Chocolate Chunk """ )
    cookie_pick = input(" type a or b for you selection ").lower()


if cookie_pick == "a":
        name = "Chocolate Swirl"
        print("Great choice! You chose option " + cookie_pick + ") " + name)
        check = input("Would you like to change cookie option before starting? [ yes or no ] you cannot change your answer after ").lower() 
        if check == "yes":
            cookie_pick = "b"
            name = "Chocolate Chunk"
            print("Great choice! You chose option " + cookie_pick + ") " + name)

elif cookie_pick == "b":
        print("Great choice! You chose option " + cookie_pick + ") " + name)
        name = "Chocolate Chunk"
        print("Great choice! You chose option " + cookie_pick + ") " + name)
        check = input("Would you like to change cookie option before starting? [ yes or no ] you cannot change your answer after ").lower() 
        if check == "yes":
            cookie_pick = "a"
            name = "Chocolate Swirl"
            print("Great choice! You chose option " + cookie_pick + ") " + name)

if cookie_pick == "a":
    print("""
    ~ Alright in the last segment you chose option a!
    ~ Which is the Chocolate Swirl Cookie.
    ~ You have to find out the correct order of steps to make this cookie """)

if cookie_pick == "b":
    print("""
    ~ Alright in the last segment you chose option a!
    ~ Which is the Chocolate Swirl Cookie.
    ~ You have to find out the correct order of steps to make this cookie """)