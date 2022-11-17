import re


# exercise 1
def return_all_words(string):
    reg = re.findall("\w+", string)
    return reg


def exercise_1():
    print("-----Exercise 1-----")
    print(return_all_words("Ana are mere1"))


# exercise 2
def return_matching_espresion(regex, string, x):
    list_to_return = []
    reg = re.findall(regex, string)
    if reg:
        for i in range(0, len(reg)):
            if len(reg[i]) == x:
                list_to_return.append(reg[i])
        return list_to_return
    else:
        return None


def exercise_2():
    print("-----Exercise 2-----")
    print(return_matching_espresion("\w+", "Ana are mere", 3))


# exercise 3
def at_least_one(string, list_regular_exrpesions):
    list_to_return = []
    for expresion in list_regular_exrpesions:
        reg = re.findall(expresion, string)
        if reg:
            for i in range(0, len(reg)):
                list_to_return.append(reg[i])
    return list_to_return


def exercise_3():
    print("-----Exercise 3-----")
    print(at_least_one("Ana are 289 mere", ["\w+", "\d+"]))


# exercise 4
def return_items(path, arrts):
    list_to_return = []
    # with open(path,"r") as file:


def exercise_4():
    print("-----Exercise 4-----")
    attrs = {"class": "url", "name": "url-form", "data-id": "item"}
    print("", attrs)


# exercise 5
def exercise_5():
    print("-----Exercise 5-----")


# exercise 6
def censorship(string):
    string_to_return = ''
    for index in range(0, len(string)):
        if index % 2 != 0:
            string_to_return = string_to_return + '*'
        else:
            string_to_return = string_to_return + string[index]
    return string_to_return


def censures_words(text):
    text_to_return = ''
    regex = re.compile("^([aeiouAEIOU]).+([aeiouAEIOU])$")
    words = text.split(" ")
    for word in words:
        if regex.match(word):
            text_to_return = text_to_return + censorship(word)
            text_to_return = text_to_return + " "
        else:
            text_to_return = text_to_return + word
            text_to_return = text_to_return + " "

    return text_to_return


def exercise_6():
    print("-----Exercise 6-----")
    print(censures_words("Ana are mere si pere dar nu are afine"))


# exercise 7
def exercise_7():
    print("-----Exercise 7-----")
    reg = re.compile("[1256]\d{12}$")
    if reg.match("5011201909090"):
        print("Valid CNP")
    else:
        print("not valid CNP")


# exercise 8
def display_from_dictionary(dict, expression):
    reg = re.compile(expression)
    for key in dict:
        both = False
        if reg.match(key):
            if reg.match(dict[key]):
                print(">>", key, dict[key])
            else:
                print(key)


def exercise_8():
    display_from_dictionary({'ana': 'are', '89': 'avar'}, "\w+")


if __name__ := 'main/py':
    exercise_1()
    exercise_2()
    exercise_3()
    #exercise_4()
    #exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
