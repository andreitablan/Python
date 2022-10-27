import os
import glob


# FII Tablan Andrei Razvan - Lab 4

# exercise 1
def return_extensions(directory):
    list_of_terminations = []
    for filename in os.listdir(directory):
        terminations = filename.split('.')
        list_of_terminations.append(terminations[1])

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
            if (os.path.isfile(filename)):
                terminations = filename.split('.')
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


if __name__ == '__main__':
    # exercise_1()
    # exercise_2()
    # exercise_3()
    exercise_4()
