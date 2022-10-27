import os


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
def exercise_2():
    print("------------Exercise 2---------------")

if __name__ == '__main__':
    exercise_1()
