#type hints
import sys

def numele_functiei(a:int,b: int) -> int:
    return a+b
if __name__ == '__main__':
    a = "Someone!"
    b = 17
    c = 3.14
    d = False
    e = True
    # aici e un comentariu
    print(b + c)
    print(d + int(c))
    print('HelloWorld')
    print("hello" + a)
    print(f"Rezultatul functiei este: {numele_functiei(7,8)}")
    print(sys.argv)