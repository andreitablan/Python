# FII Tablan Andrei Razvan - Lab 3

# exercise_1
def operations_with_lists(a, b):
    a_or_b = list(set().union(a, b))
    a_and_b = list(set().intersection(a, b))
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]
    list = []
    list.append(a_or_b)
    list.append(a_and_b)
    list.append(a_minus_b)
    list.append(b_minus_a)
    return list


def exercise_1():
    print('-------------Exercise 1----------------')
    a = [1, 78, 90, 3, 7, 16, 15, 9, 23]
    b = [1, 7, 8, 9, 10, 11, 68]
    print(operations_with_lists(a, b))


# exercise_2
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


# exercise_3
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
    print('-------------Exercise 2----------------')
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


# exercise_4
def build_xml_element(tag, content, href, _class, id):
    string = '<' + tag + " herf= " + href + "\_class= " + _class + "'\id=" + id + "\>" + content + "</" + tag + ">"
    return string


def exercise_4():
    print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
    # < a href =\"http://python.org \ "_class = \" my-link \ " id = \" someid \ " > Hello there < / a >


# exercise 5
def validate_dict(dictionary, rule):
    for tuple in rule:
        return True
    # str.startswith
    # str.endswith
    # pentru middle -> scot inceput si final, si verific ce ramane.


def exercise_5():
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
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
    list = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8]
    print(unique_not_unique(list))


# exercise 7
def exercise_7():
    return True


# exercise 8
def loop(dictionary):
    return True


def exercise_8():
    dict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    print(loop(dict))


if __name__ == '__main__':
    # exercise_1()
    # exercise_2()
    # exercise_3() -> flatten; 2 dict cheie cu cheie si verificat sa fie in acelasi dictionar
    # exercise_4()-not ok
    # exercise_5()  # not finished
    # exercise_6()
    exercise_7()
    exercise_8()
    # ex 9 -> *args, **Kwargs
