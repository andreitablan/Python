# FII Tablan Andrei Razvan - Lab 3

# exercise_1
def operations_with_lists(a, b):
    a_or_b = list(set().union(a, b))
    a_and_b = [x for x in a if x in b]
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]
    return a_or_b, a_and_b, a_minus_b, b_minus_a


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
            dictionary[ch]=1
        else:
            dictionary[ch]+=1
    return dictionary


def exercise_2():
    print('-------------Exercise 2----------------')
    string = "AnaAreMere"
    print(dictionary_from_string(string))

#exercise_3
def compare_dictionary(dictionary1,dictionary2):
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
    print(compare_dictionary(dictionary1,dictionary2))
    print(compare_dictionary(dictionary1,dictionary3))

#exercise_4
def build_xml_element(tag, content,href,_class,id):
    string='<'+tag+" herf= "+href+"\_class= "+_class+"'\id="+id+"\>"+content+"</"+tag+">"
    return string

def exercise_4():
    print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
    #< a href =\"http://python.org \ "_class = \" my-link \ " id = \" someid \ " > Hello there < / a >

def validate_dict(dictionary,rule):
    for tuple in rule:
        for element in tuple:
            return True
def exercise_5():
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    print(validate_dict(d,s))

if __name__ == '__main__':
    # exercise_1()
    # exercise_2()
    # exercise_3()
    #exercise_4()-not ok
    exercise_5()#not finished


