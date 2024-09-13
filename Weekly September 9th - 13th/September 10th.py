#continued project 
#goal is for user to input correct order of steps to make cookies 
#hopefully I can adjust the program to tell the user when the user puts one of the numbers in the correct order
#but for today I just kept it simple 

cookie_pick = input("a or b").lower()
#temp for easy reading


answer_partone = [4, 3, 1, 2, 5]
answer_partwo = [6, 5, 1, 2, 3, 4, 7, 8]
answer1 = ""
answer2 = ""
question = ""
if cookie_pick == "a":
    print("""
    ~ Alright in the last segment you chose option a!
    ~ Which is the Chocolate Swirl Cookie.
    ~ You have to find out the correct order of steps to make this cookie """)
    
    print("""
    This is the written recipe --> 
    Part one: 
    To make the chocolate swirl cookie you must brown two sticks of butter.
    Then measure out brown sugar and white sugar! 
    I'll be using 1 cups of brown sugar and 1/2 cups of white sugar. 
    Afterword mix the sugars, butters, and 2 eggs. 
    The egg is a binder for this cookie! 
    I like to add vanilla extract but this step is optional.
    
     """)

    print(""""
    
    Use the written recipe above to solve the puzzle!
    
    Here are part 1 of the steps, NOT in order
    1) Measure out 1/2 cup of white sugar 
    2) Mix in browned butter, sugars and 2 eggs in a bowl
    3) Measure out 1 cups of brown sugar
    4) Brown 2 sticks of butter
    5) Add in some vanilla extract

    """)
    give_up = ""
    while answer1 != answer_partone:
        answer1 = my_list = [int(n) for n in input("Your answer (ex. 1 2 3 4 5) make sure to add spaces between the numbers!").split()]
        if answer1 != answer_partone: 
            print("Wrong! ")
            give_up = input("Try again? if so type [ yes ] if not type [ no ] ").lower()
        if give_up == "no":
            answer1 = answer_partone
        if answer1 == answer_partone:
            print("Great job you've completed part 1!")
    
    question = input("Would you like to move to part 2? If so type [ yes ] if not [ no ]")

    if question == "yes":
        print("""
         ~ Alright in the last segment you solved part one!
         ~ Now is part two (Its harder to solve be careful!) 
         ~ You have to find out the correct order of steps to make this cookie 
         
         The written recipe -->
         Part two: Second is the dry ingredients.
         I'm going to start with 1 1/2 cups of flour and than 3/4 cup of coco powder. 
         Personally I add some instant coffee for richer chocolate taste. 
         Now I'm adding in the baking soda and baking powder to spread and rise our cookies! 
         Also remeber to add some salt (around 1 tsp) and cornstarch for a deeper flavor and a softer cookie.
         Now that the dry ingredients are ready lets mix the wet ingredients and the dry ingredients.
         We will add on the swirled marshmellow fluff before baking. 
         For now set your dough to rest for at least an hour. 
         When its about time to take out your dough, preheat the oven to 375 and start shaping your cookies. 
         Set the cookie dough balls on a sheet tray with parchment paper. 
         Dollap some marshmellow fluff on and bake for 13 - 14 minutes! """)
  

        print("""

        Use the written recipe above to solve the puzzle!
    
        1) Measure out 1 tsp of baking soda, 1/2 tsp of baking powder 

        2) 1 tsp of salt and 2 tbsp of cornstarch

        3) Mix dry and wet ingredients 

        4) Let dought rest for 2 hours

        5)To new bowl add in 3/4 cup of coco powder and 1 to 2 tsp of instant coffee

        6) Stir well and in seperate bowl measure out 1 1/2 cups of flour (240g)

        7) Seperate dough into 3 tbsp sized cookies and preheat oven to 375 degrees

        8) dollap marshmellow fluff ontop and bake 
        
         """)  


        give_up = ""
        while answer2 != answer_partwo:
            answer2 = my_list = [int(n) for n in input("Your answer (ex. 1 2 3 4 5) make sure to add spaces between the numbers!").split()]
            if answer2 != answer_partwo: 
                print("Wrong! ")
                give_up = input("Try again? if so type [ yes ] if not type [ no ] ").lower()
            if give_up == "no":
                answer2 = answer_partwo
            if answer2 == answer_partwo:
                print("Great job you've completed part 2!")
