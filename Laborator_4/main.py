import os
import glob
import sys


# FII Tablan Andrei Razvan - Lab 4

# exercise 1
def return_extensions(directory):
    list_of_terminations = []
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            terminations = os.path.splitext(filename)[1]
            list_of_terminations.append(terminations)

    return sorted(list_of_terminations)


def exercise_1():
    print("------------Exercise 1---------------")
    print(return_extensions(os.getcwd()))


# exercise 2
def write_paths_in_file(directory, file):
    list_for_lines = []
    for filename in os.listdir(directory):
        if filename.startswith('A'):
            list_for_lines.append(os.path.abspath(filename) + '\n')
    with open(file, 'w') as f:
        f.writelines(list_for_lines)
    return "Check the file"


def exercise_2():
    print("------------Exercise 2---------------")
    print(write_paths_in_file(os.getcwd(), 'ex2_fisier.txt'))


# exercise 3
def file_or_directory(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'r') as file:
            data = file.read()
            return data[-20:]
    elif os.path.isdir(my_path):
        list_to_return = []
        dict_of_extensions = {}
        for filename in glob.iglob(my_path + '**/**', recursive=True):
            if os.path.isfile(filename):
                terminations = os.path.splitext(filename)[1]
                print(terminations)
                if not terminations[1] in dict_of_extensions:
                    dict_of_extensions[terminations[1]] = 1
                else:
                    dict_of_extensions[terminations[1]] += 1
        for key, value in dict_of_extensions.items():
            list_to_return.append((key, value))
        list_to_return.sort(key=lambda x: x[1], reverse=True)
        return sorted(list_to_return)


def exercise_3():
    print("----------------Exercise 3----------------")
    print(file_or_directory("ex2_fisier.txt"))
    print(file_or_directory(os.getcwd()))


# exercise 4
def exercise_4():
    print("----------------Exercise 4----------------")
    print(return_extensions(sys.argv))


# exercise 5
def return_list_of_files(target, to_search):
    list_of_files_to_return = []
    try:
        if os.path.isfile(target):
            with open(target, 'r') as file:
                data = file.read()
            if data.find(to_search) != -1:
                list_of_files_to_return.append(target)
        elif os.path.isdir(target):
            for root, dirs, files in os.walk(target, topdown=False):
                for file in files:
                    try:
                        a_file = open(file, 'r')
                        data = a_file.read()
                        if data.find(to_search) != -1:
                            list_of_files_to_return.append(file)
                    except IOError:
                        print("Could not open file.")
        return list_of_files_to_return
    except ValueError as exception:
        raise ValueError("Could not open file.") from exception


def exercise_5():
    print("----------------Exercise 5----------------")
    print("A file: ")
    print(return_list_of_files("ex5.txt", "ana"))
    print("A directory: ")
    print(return_list_of_files(os.getcwd(), "ana"))


# exercise 6
def callback(error_type):
    if error_type == IOError:
        return "Could not open file."
    elif error_type == ValueError:
        return "The input was wrong"
    return


def return_list_of_files_with_callback(target, to_search, callback_function):
    list_of_files_to_return = []
    try:
        if os.path.exists(target):
            if os.path.isfile(target):
                with open(target, 'r') as file:
                    data = file.read()
                if data.find(to_search) != -1:
                    list_of_files_to_return.append(target)
            elif os.path.isdir(target):
                for root, dirs, files in os.walk(target, topdown=False):
                    for file in files:
                        try:
                            a_file = open(file, 'r')
                            data = a_file.read()
                            if data.find(to_search) != -1:
                                list_of_files_to_return.append(file)
                        except IOError:
                            print(callback_function(IOError))
            return list_of_files_to_return
    except ValueError as exception:
        raise ValueError(callback_function(ValueError)) from exception


def exercise_6():
    print("----------------Exercise 6----------------")
    print("A file: ")
    print(return_list_of_files_with_callback("ex5.txt", "ana", callback))
    print("A directory: ")
    print(return_list_of_files_with_callback(os.getcwd(), "ana", callback))
    print("Not a valid to_search: ")
    print(return_list_of_files_with_callback(os.getcwd(), "not_valid", callback))
    print("Not a valid target: ")
    print(return_list_of_files_with_callback("not_valid", "", callback))


# exercise 7
def return_dict(file):
    dict = {}
    dict["full_path"] = os.path.abspath(file)
    dict["file_size"] = os.path.getsize(file)
    dict["file_extension"] = os.path.splitext(file)[1]
    f = open(file, "r")
    dict["can_read"] = f.readable()
    f = open(file, "w")
    dict["can_write"] = f.writable()

    return dict


def exercise_7():
    print("----------------Exercise 7----------------")
    print(return_dict("ex5.txt"));


# exercise 8
def return_list_of_absolute_paths(dir_path):
    list_to_return = []
    for root, subFolders, files in os.walk(dir_path):
        for folder in subFolders:
            list_to_return.append(os.path.abspath(folder))
        for file in files:
            list_to_return.append(os.path.abspath(file))
    return list_to_return


def exercise_8():
    print("----------------Exercise 8----------------")
    print(return_list_of_absolute_paths(os.getcwd()))


if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
