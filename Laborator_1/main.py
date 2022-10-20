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
        if i > 1:
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
    result = [my_string[0].lower()]
    for ch in my_string[1:]:
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result.append('_')
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)


def exercise_4():
    print('-------------Exercise 4----------------')
    word = input("Enter a string using UpperCamelCase: ")
    print('The converted string in lowercase_with_underscores is: ', change_case(word))


# exercise_5
def spiral_order(matrix, size):
    top = 0
    bottom = size - 1
    left = 0
    right = size - 1
    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                print(matrix[top][i], end="")

            top += 1
            direction = 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                print(matrix[i][right], end="")

            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end="")
            bottom -= 1
            direction = 3

        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end="")

            left += 1
            direction = 0


def exercise_5():
    print('-------------Exercise 5----------------')
    size = int(input("What size is the matrix of characters?"))
    matrix = []
    for index in range(size):
        text = input()
        matrix.append(text)
    spiral_order(matrix, size)


# exercise_6
def palindrome(number):
    if str(number)[::-1] == str(number):
        return 'Yes, it is palindrome'
    return 'No, it it not palindrome'


def exercise_6():
    print('-------------Exercise 6----------------')
    number = input("Enter a number in order to verify if it is palindrome: ")
    print(palindrome(number))


# exercise_7
def extract_number(text):
    for iterator in range(len(text)):
        if text[iterator].isnumeric():
            number = text[iterator]
            for iterator1 in range(iterator + 1, len(text)):
                if text[iterator1].isnumeric():
                    number = number + text[iterator1]
                else:
                    return number
    return number


def exercise_7():
    print('-------------Exercise 7----------------')
    text = input("Enter a text containing a number: ")
    print(extract_number(text))


# exercise_8
def how_many_bits(number):
    bin_number = bin(int(number))
    number_of_1 = bin_number.count('1')
    return number_of_1


def exercise_8():
    print('-------------Exercise 8----------------')
    number = input("Enter a number to see how many values of 1 it has in binary form: ")
    print('The number has ', how_many_bits(number), ' values of 1 in the binary representation')


# exercise_9
def common_character(text):
    frequency = {}
    text.replace(' ', '')

    for i in text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return max(frequency, key=frequency.get)


def exercise_9():
    print('-------------Exercise 9----------------')
    text = input("Enter a text to see the most common character: ")
    print('The most common character is: ', common_character(text))


# exercise_10
def how_many_words(text):
    words = text.split(' ')
    return len(words)


def exercise_10():
    print('-------------Exercise 10----------------')
    text = input("Enter a text: ")
    print('The text <', text, '> has ', how_many_words(text), 'words')


if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
