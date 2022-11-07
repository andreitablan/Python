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


def exercise_2():
    print("------Exercise 2------")


if __name__ == '__main__':
    exercise_1()
    exercise_2()
