#code reprogram in previous versions the code would not tell user which inputs are correct
#but now when the user input an incorrect answer (ex. 43215) the program tells them which are in the correct order (ex. 4 is in the right, place 3 is in the right place, 5 is in the right place)


cookie_pick = "a"

answer_partone = [4, 3, 1, 2, 5]
answer_partwo = [6, 5, 1, 2, 3, 4, 7, 8]
answer1 = ""
answer2 = ""
question = ""
if cookie_pick == "a":
give_up = ""
    while answer1 != answer_partone:
        answer1 = my_list = [int(n) for n in input("Your answer (ex. 1 2 3 4 5) make sure to add spaces between the numbers!").split()]

        if answer1 != answer_partone: 
            print("Wrong! ")
            for index in range(len(answer_partone)): 
                if answer1[index] == answer_partone[index]: 
                    print(" {} is in the right place".format(answer1[index]))

            while True:
                give_up = input("Try again? if so type [ yes ] if not type [ no ] ").lower()
                if give_up in ["yes", "no"]:
                    print(give_up)
                    break
                else:
                    print("please type [ yes ] or [ no ]")
                        

        if give_up == "no":
            answer1 = answer_partone
            print("Good try")
        if answer1 == answer_partone and give_up != "no":
            print("Great job you've completed part 1!")
    