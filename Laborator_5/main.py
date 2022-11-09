# FII Tablan Andrei Razvan - Lab 5
# exercise 1
import utils
import app


def exercise_1():
    print("------Exercise 1------")
    print("a)")
    x = int(input('Enter a number: '))
    print(utils.process_item(x))
    print("b)")
    app.do_until_read_q()


# exercise 2
def function_sum(*args, **kwargs):
    sum = 0;
    for value in kwargs.values():
        sum = sum + value
    anonymous = lambda *args: sum(*args)

    return sum


def exercise_2():
    print("------Exercise 2------")
    print(function_sum(0, 1, c=3, d=4))


# exercise 3
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return_list = []
    for character in s:
        if character in vowels:
            return_list.append(character)
    return return_list


def function_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    anonymous = lambda s: [character for character in s if character in vowels]
    list_comprehensions_and_filter = list(filter(lambda x: x in "aeiou", s))
    return (return_vowels(s), anonymous(s), list_comprehensions_and_filter)


def exercise_3():
    print("------Exercise 3------")
    print(function_vowels("Programming in Python is fun"))


# exercise 4
def my_function4(*args, **kwargs):
    list_to_return = []
    for value in args:
        if type(value) is dict and len(value.keys()) >= 2:
            for key in value:
                if isinstance(key, str) and len(key) >= 3:
                    list_to_return.append(value)
    for value in kwargs.values():
        if type(value) is dict and len(value.keys()) >= 2:
            for key in value:
                if isinstance(key, str) and len(key) >= 3:
                    list_to_return.append(value)
    return list_to_return


def exercise_4():
    print("------Exercise 4------")
    print(my_function4(
        {1: 2, 3: 4, 5: 6},
        {'a': 5, 'b': 7, 'c': 'e'},
        {2: 3},
        [1, 2, 3],
        {'abc': 4, 'def': 5},
        3764,
        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
        test={1: 1, 'test': True}
    ))


# exercise 5
def my_function5(list):
    list_to_return = [number for number in list if isinstance(number, (int, float))]
    return list_to_return


def exercise_5():
    print("------Exercise 5------")
    print(my_function5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


# exercise 6
def function_odd_even(list):
    list_to_return = []
    even_numbers = []
    odd_numbers = []
    for element in list:
        if element % 2 == 0:
            even_numbers.append(element)
        else:
            odd_numbers.append(element)
    for index in range(0, len(list) // 2):
        tuple = (even_numbers[index], odd_numbers[index])
        list_to_return.append(tuple)
    return list_to_return


def exercise_6():
    print("------Exercise 6------")
    print(function_odd_even([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))


# exercise 7
def sum_digits(x):
    return sum(map(int, str(x)))


def fibonacci_list(number):
    first = 0
    second = 1
    fibonacci = []
    if number < 1:
        return
    for x in range(1, number):
        fibonacci.append(second)
        third = first + second
        first = second
        second = third
    return fibonacci


def process(**kwargs):
    fibonacci = fibonacci_list(10)
    if 'filters' in kwargs.keys():
        filters = kwargs.get('filters')
        for value in fibonacci:
            if value in filters:
                fibonacci.remove(value)
    if 'offset' in kwargs.keys():
        if kwargs.get('offset') > len(fibonacci):
            return "wrong offset"
        del fibonacci[0:kwargs.get('offset')]

    if 'limit' in kwargs.keys():
        if kwargs.get('limit') > len(fibonacci):
            return "wrong limit"
        del fibonacci[kwargs.get('limit'):len(fibonacci)]
    return fibonacci


def exercise_7():
    print("------Exercise 7------")
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
                  limit=2,
                  offset=2))


# exercise 8
def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def function_to_return(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)

    return function_to_return


def multiply_by_three(x):
    return x * 3


def multiply_output(function):
    def function_to_return(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return function_to_return


def augment_function(function, decorators):
    def function_to_return(*args, **kwargs):
        #for decorator in decorators:
            #function=decorator(function)
        return function(*args, **kwargs)
    return function_to_return


def exercise_8():
    print("------Exercise 8------")
    print("------a)--------------")

    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)  # this will print: Arguments are: (10,), {} and will return 20.
    print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.
    print(x)

    print("------b)--------------")
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
    print(x)
    print("------c)--------------")
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])

    x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))
    print(x)


# exercise 9
def f9(**kwargs):
    result = []
    for element1, element2 in kwargs.get("pairs"):
        dictionary = dict()
        dictionary['sum'] = element1 + element2
        dictionary['prod'] = element1 * element2
        dictionary['pow'] = element1 ** element2
        result.append(dictionary)
    return result


def exercise_9():
    print("------Exercise 9------")
    print(f9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))


if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8() # not finished c
    exercise_9()
