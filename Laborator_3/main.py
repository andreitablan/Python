def operations_with_lists(a, b):
    a_or_b = [1]
    a_and_b = [2]
    a_minus_b = [3]
    b_minus_a = [4]
    return a_or_b, a_and_b, a_minus_b, b_minus_a


def exercise_1():
    print('-------------Exercise 3----------------')
    a = [1, 78, 90, 3, 7, 16, 15, 9, 23]
    b = [1, 7, 8, 9, 10, 11, 68]
    print(operations_with_lists(a, b))

if __name__ == '__main__':
    exercise_1()

