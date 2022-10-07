# FII - Tablan Andrei - Python - Lab1

# exercise_1
def cmmdc(number1, number2):
    while number2 != 0:
        rest = number1 % number2
        number1 = number2
        number2 = rest
    return number1


def exercise_1():
    print('-------------Exercise 1----------------')
    numbers = [int(numbers) for numbers in input("Please enter multiple values: ").split()]
    first_cmmdc = cmmdc(numbers[0], numbers[1])
    for i in range(len(numbers)):
        if (i > 1):
            final_cmmdc = cmmdc(first_cmmdc, numbers[i])
    print('The cmmdc of the given values is: ', final_cmmdc)


# exercise_2
def calculate_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    counter = 0
    for index in word.lower():
        if index in vowels:
            counter += 1;
    return counter


def exercise_2():
    print('-------------Exercise 2----------------')
    word = input("Enter a word here: ")
    print('The number of vowels is ', calculate_vowels(word))


# exercise_3
def exercise_3():
    print('-------------Exercise 3----------------')
    word1 = input("Enter first word here: ")
    word2 = input("Enter second word here: ")
    list = word2.split(word1)
    print(len(list) - 1)


# exercise_4
def change_case(my_string):
    res = [my_string[0].lower()]
    for ch in my_string[1:]:
        if ch in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(ch.lower())
        else:
            res.append(ch)
    return ''.join(res)


def exercise_4():
    print('-------------Exercise 4----------------')
    word = input("Enter a string using UpperCamelCase: ")
    print('The converted string in lowercase_with_underscores is: ', change_case(word))


# exercise_6
def palindrome(number):
    if (str)(number)[::-1] == (str)(number):
        return 'Yes, it is palindrome'
    return 'No, it it not palindrome'


def exercise_6():
    print('-------------Exercise 6----------------')
    number = input("Enter a number in order to verify if it is palindrome: ")
    print(palindrome(number))


if __name__ == '__main__':
    ##exercise_1()
    ##exercise_2()
    ##exercise_3()
    ##exercise_4()
    ##exercise_5()
    exercise_6()
    ##exercise_7()
    ##exercise_8()
    ##exercise_9()
    ##exercise_10()
