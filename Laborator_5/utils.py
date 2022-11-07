def process_item(x):
    prime = 1
    x += 1
    while prime==1:
        for i in range(2, int(x ** 0.5) + 2):
            if x % i == 0:
                prime=0
                break
        if prime == 0:
            prime = 1
            x += 1
        else:
            return x
