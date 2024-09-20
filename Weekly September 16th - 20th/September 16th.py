n = input("name ")
def abbrev_name(name):
    names = name.split()
    first = names[0]
    first_letter = first[0]
    second = names[1]
    second_letter = second[0]
    print(first_letter.upper() + "." + second_letter.upper() + ".")

abbrev_name(n)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def repeat_str(repeat, string):
    return string * repeat

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sen = input("jo")

def get_count(sentence):
    answer = 0
    letter_count_a = ""
    letter_count_e = ""
    letter_count_i = ""
    letter_count_o = ""
    letter_count_u = ""
    if "a" in sentence:
        letter_count_a = sentence.count("a")
        answer += letter_count_a
    if "e" in sentence:
        letter_count_e = sentence.count("e")
        answer += letter_count_e
    if "i" in sentence:
        letter_count_i = sentence.count("i")
        answer += letter_count_i
    if "o" in sentence:
        letter_count_o = sentence.count("o")
        answer += letter_count_o
    if "u" in sentence:
        letter_count_u = sentence.count("u")
        answer += letter_count_u
    print(answer)

get_count(sen)