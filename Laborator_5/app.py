import utils


def do_until_read_q():
    x = input('Enter a number: ')
    while x != 'q':
        print(utils.process_item(int(x)))
        x = input('Enter a number: ')
