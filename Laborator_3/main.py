# FII Tablan Andrei Razvan - Lab 3

# exercise 1
def operations_with_lists(a, b):
    a_or_b = a + b
    a_and_b = list(set(a) & set(b))
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]
    list_to_return = []
    list_to_return.append(a_or_b)
    list_to_return.append(a_and_b)
    list_to_return.append(a_minus_b)
    list_to_return.append(b_minus_a)
    return list_to_return


def exercise_1():
    print('-------------Exercise 1----------------')
    a = [1, 78, 90, 3, 7, 16, 15, 9, 23]
    b = [1, 7, 8, 9, 10, 11, 68]
    print(operations_with_lists(a, b))


# exercise 2
def dictionary_from_string(string):
    dictionary = dict()
    for ch in string:
        if ch not in dictionary:
            dictionary[ch] = 1
        else:
            dictionary[ch] += 1
    return dictionary


def exercise_2():
    print('-------------Exercise 2----------------')
    string = "AnaAreMere"
    print(dictionary_from_string(string))


# exercise 3
def compare_dictionary(dictionary1, dictionary2):
    if len(dictionary1) != len(dictionary2):
        return False
    else:
        flag = 0
        for i in dictionary1:
            if dictionary1.get(i) != dictionary2.get(i):
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False


def exercise_3():
    print('-------------Exercise 3----------------')
    dictionary1 = {
        'number': 1,
        'list': ['one', 'two']
    }
    dictionary2 = {
        'list': ['one', 'two'],
        'number': 1
    }
    dictionary3 = {
        'list': ['one', 'three'],
        'number': 1
    }
    print(compare_dictionary(dictionary1, dictionary2))
    print(compare_dictionary(dictionary1, dictionary3))


# exercise 4
def build_xml_element(tag, content, **kwargs):
    string = '<' + tag + "\n"

    for k, v in kwargs.items():
        string += ''.join(f'{k}={v}')

    string += content + "</" + tag + ">"
    return string


def exercise_4():
    print('-------------Exercise 4----------------')
    keywords = {'herf': "http://python.org", 'class': "my-link", 'id': "someid "}

    print(build_xml_element(tag="a", content="Hello there", **keywords))


# exercise 5
def validate_dict(dictionary, rule):
    for tuple in rule:
        if tuple[0] in dictionary:
            middle = dictionary[tuple[0]][len(tuple[1]):-len(tuple[3])]

            if dictionary[tuple[0]].startswith(tuple[1]) and middle == tuple[2] and dictionary[tuple[0]].endswith(
                    tuple[3]):
                return True
        else:
            return False


def exercise_5():
    print('-------------Exercise 5----------------')

    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    print(validate_dict(d, s))


# exercise 6
def unique_not_unique(list):
    dict = {}
    a = 0
    b = 0
    for element in list:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] += 1
    for key in dict:
        if dict[key] == 1:
            a += 1
        else:
            b += 1
    return a, b


def exercise_6():
    print('-------------Exercise 6----------------')

    list = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8]
    print(unique_not_unique(list))


# exercise 7
def return_dictionary(*args):
    dictionary = {}
    for element_1 in args:
        for element_2 in args:
            if element_1 != element_2:
                a = element_1
                b = element_2
                a_or_b = a | b
                a_and_b = a & b
                a_minus_b = a - b
                b_minus_a = b - a

                construction_key = str(element_1) + '|' + str(element_2)
                dictionary.setdefault(construction_key, a_or_b)

                construction_key = str(element_1) + '&' + str(element_2)
                dictionary.setdefault(construction_key, a_and_b)

                construction_key = str(element_1) + '-' + str(element_2)
                dictionary.setdefault(construction_key, a_minus_b)

                construction_key = str(element_2) + '-' + str(element_1)
                dictionary.setdefault(construction_key, b_minus_a)

    return dictionary


def exercise_7():
    print('-------------Exercise 7----------------')

    print(return_dictionary({1, 2}, {2, 3}))


# exercise 8
def loop(mapping):
    current_value = mapping['start']
    list_of_keys = []
    list_of_keys.append(current_value)
    while current_value in mapping:
        current_value = mapping[current_value]
        if current_value in list_of_keys:
            return list_of_keys
        list_of_keys.append(current_value)
    return list_of_keys


def exercise_8():
    print('-------------Exercise 8----------------')

    dict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    print(loop(dict))


# exercise 9
def my_function(*args, **kwargs):
    count = 0
    print(args)
    print(kwargs)
    for element in kwargs:
        if kwargs[element] in args:
            count += 1
    return count


def exercise_9():
    print('-------------Exercise 9----------------')

    print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))


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
