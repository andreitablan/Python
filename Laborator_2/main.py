# FII - Tablan Andrei - Python - Lab2

# exercise_1
def fibonacci_list(number):
    first = 0
    second = 1
    fibonacci = [0]
    if number < 1:
        return
    for x in range(1, number):
        fibonacci.append(second)
        third = first + second
        first = second
        second = third
    return fibonacci


def exercise_1():
    print('-------------Exercise 1----------------')
    number = 10
    print(fibonacci_list(number))


# exercise_2
def is_prime(number):
    if number < 1: return False
    if number == 2 or number == 1: return True
    for index in range(3, number // 2):
        if number % index == 0:
            return False
    return True


def list_of_prime_numbers(list):
    list_1 = []
    for index in range(0, len(list)):
        if is_prime(list[index]):
            list_1.append(list[index])
    return list_1


def exercise_2():
    print('-------------Exercise 2----------------')
    list = [1, 78, 90, 3, 7, 16, 15, 9, 23]
    print(list_of_prime_numbers(list))


# exercise_3
def operations_with_lists(a, b):
    a_or_b = list(set().union(a, b))
    a_and_b = [x for x in a if x in b]
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]
    return a_or_b, a_and_b, a_minus_b, b_minus_a


def exercise_3():
    print('-------------Exercise 3----------------')
    a = [1, 78, 90, 3, 7, 16, 15, 9, 23]
    b = [1, 7, 8, 9, 10, 11, 68]
    print(operations_with_lists(a, b))


# exercise_4
def compose(notes, moves, begin):
    list_of_song = [notes[begin]]
    current_position = begin
    for move in moves:
        if move + current_position < len(notes):
            list_of_song.append(notes[move + current_position])
            current_position = move + current_position
        else:
            list_of_song.append(notes[-(len(notes) - current_position) + move])
            current_position = len(notes) - current_position + move
    return list_of_song


def exercise_4():
    print('-------------Exercise 4----------------')
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    begin = 2
    print(compose(notes, moves, begin))


# exercise_5
def replace_in_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if i > j:
                matrix[i][j] = 0;
    return matrix


def exercise_5():
    print('-------------Exercise 5----------------')
    matrix = [[1, 2, 3, 6], [4, 5, 6, 6], [8, 9, 10, 12], [11, 12, 24, 53]]

    matrix = replace_in_matrix(matrix, 4)
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=" ")
        print()


# exercise_6
def return_list(list_of_lists, number):
    list_to_return = []
    freq = {}
    for list in list_of_lists:
        for item in list:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
    for item in freq:
        if freq[item] == number:
            list_to_return.append(item)

    return list_to_return


def exercise_6():
    print('-------------Exercise 6----------------')
    list_of_lists = [[1, 2, 3, 3, 4], [1, 1, 2, 3, 7, 19, 20], [7, 7, 2, 20, 19], [19, 20]]
    print(return_list(list_of_lists, 3));


# exercise_7
def palindrome(number):
    if str(number)[::-1] == str(number):
        return True
    return False


def work_with_palindromes(list):
    list_of_palindromes = []
    for item in list:
        if palindrome(item) == True:
            list_of_palindromes.append(item)
    length = len(list_of_palindromes)
    max_number = max(list_of_palindromes)
    tuple = (length, max_number)
    return tuple


def exercise_7():
    print('-------------Exercise 7----------------')
    list = [111, 131, 189, 923, 42, 909, 10001, 2992]
    print(work_with_palindromes(list))


# exercise_8
def verify_ASCII_code(number, ch):
    if ord(ch) % number == 0:
        return True
    else:
        return False


def work_with_ASCII(number, list_of_strings, flag):
    list_of_lists = []
    for string in list_of_strings:
        list = []
        for character in string:
            if verify_ASCII_code(number, character) == flag:
                list.append(character)
        list_of_lists.append(list)
    return list_of_lists


def exercise_8():
    print('-------------Exercise 8----------------')
    x = 2
    list_of_strings = ["test", "hello", "lab002"]
    flag = False
    list_of_lists = work_with_ASCII(x, list_of_strings, flag)
    print(list_of_lists)


# exercise_9
def who_cannot_see(field, n, m):
    list_of_tuples = []
    for i in range(0, n):
        for j in range(0, m):
            for k in range(0, i):
                if field[i][j] <= field[k][j]:
                    list_of_tuples.append((i, j))
                    break
    return list_of_tuples


def exercise_9():
    print('-------------Exercise 9----------------')
    field = [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 7, 2],
             [5, 5, 2, 5, 6, 4],
             [6, 6, 7, 6, 7, 5]]
    print(who_cannot_see(field, 4, 5))


# exercise_10
def working_with_lists(input_list):
    number_of_tuples = max(len(x) for x in input_list)
    list_of_tuples = []
    for index in range(0, number_of_tuples):
        list_for_tuple = []
        for list in input_list:
            if len(list) <= index:
                list_for_tuple.append(None)
            else:
                list_for_tuple.append(list[index])

        new_tuple = tuple(list_for_tuple)
        list_of_tuples.append(new_tuple)
    return list_of_tuples


def exercise_10():
    print('-------------Exercise 10----------------')
    input_lists = [[1, 2, 3], [5, 6, 7], ["a", "b"]]
    print(working_with_lists(input_lists))


# exercise_11
def sort_tuples(tuples):
    length = len(tuples)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if (tuples[j][1][2] > tuples[j + 1][1][2]):
                temp = tuples[j]
                tuples[j] = tuples[j + 1]
                tuples[j + 1] = temp
    return tuples


def exercise_11():
    print('-------------Exercise 11----------------')
    tuples = [('abc', 'bcd'), ('abc', 'zza')]
    print(sort_tuples(tuples))


# exercise_12
def group_by_rhyme(list_of_words):
    list_of_groups = []
    freq = {}
    for word in list_of_words:
        key = word[-2:]
        if key not in freq:
            freq[key] = list()
        freq[key].append(word)
    for key in freq:
        list_of_groups.append(freq[key])
    return list_of_groups


def exercise_12():
    print('-------------Exercise 12----------------')
    list_of_words = ['ana', 'banana', 'carte', 'arme', 'parte']
    print(group_by_rhyme(list_of_words))


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
    exercise_11()
    exercise_12()