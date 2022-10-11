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
    number = int(input('How many numbers of the Fibonacci sequence do you want to see?'))
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
    a_or_b = [1]
    a_and_b = [2]
    a_minus_b = [3]
    b_minus_a = [4]
    return a_or_b, a_and_b, a_minus_b, b_minus_a


def exercise_3():
    print('-------------Exercise 3----------------')
    a = [1, 78, 90, 3, 7, 16, 15, 9, 23]
    b = [1, 7, 8, 9, 10, 11, 68]
    print(operations_with_lists(a, b))


# exercise_4
def exercise_4():
    print('-------------Exercise 4----------------')


# exercise_5
def exercise_5():
    print('-------------Exercise 5----------------')


# exercise_6
def exercise_6():
    print('-------------Exercise 6----------------')


# exercise_7
def exercise_7():
    print('-------------Exercise 7----------------')


# exercise_8
def exercise_8():
    print('-------------Exercise 8----------------')


# exercise_9
def exercise_9():
    print('-------------Exercise 9----------------')


# exercise_10
def exercise_10():
    print('-------------Exercise 10----------------')


# exercise_11
def exercise_11():
    print('-------------Exercise 11----------------')


# exercise_12
def exercise_12():
    print('-------------Exercise 12----------------')


if __name__ == '__main__':
    # exercise_1()
    # exercise_2()
    exercise_3()
    '''
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
    exercise_11()
    exercise_12()
    '''
