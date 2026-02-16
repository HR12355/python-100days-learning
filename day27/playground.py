# 無制限の位置引数　*
def add(*args):
    num = 0
    for n in args:
        num += n
    return num

# print(add(1, 2, 3, 4))

def calc(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(2, add=3, multiply=5)
# 25