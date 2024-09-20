cookie_pick = "a"
answer_partone = [4, 3, 1, 2, 5]
answer_partwo = [6, 5, 1, 2, 3, 4, 7, 8]
answer1 = ""
answer2 = []
question = ""
cleaned_give_up = ""
if cookie_pick == "a":
    give_up = ""
    while answer2 != answer_partwo:
        answer2 = my_list = [int(n) for n in input("Your answer (ex. 1 2 3 4 5) make sure to add spaces between the numbers!").split()]

        if answer2 != answer_partwo: 
            print("Wrong! ")
            for index in range(len(answer_partwo)): 
                if answer2[index] == answer_partwo[index]: 
                    print(" {} is in the right place".format(answer2[index]))

            while True:
                give_up = input("Try again? if so type [ yes ] if not type [ no ] ").lower()
                cleaned_give_up = give_up.replace(" ", "")
                if cleaned_give_up in ["yes", "no"]:
                    print(cleaned_give_up)
                    break
                else:
                    print("please type [ yes ] or [ no ]")
                        

        if give_up == "no":
            answer2 = answer_partwo
            print("Good try")
        if answer2 == answer_partwo and cleaned_give_up != "no":
            print("Great job you've completed part 2!")
