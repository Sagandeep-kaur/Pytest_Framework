def my_func(sagan):

    def inner_func():
        print("first")
        sagan()
        print("wrapper")

    return inner_func()



@my_func
def orange():
    print("orange")

@my_func
def banana():
    print("banana")

@my_func
def kiwi():
    print("kiwi")

orange()
banana()
kiwi()