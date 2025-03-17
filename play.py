def fun1(x=None):
    if x is None:
        raise TypeError
    try:
        y = int(x) + 1
        print(y)
    except ValueError:
        print("ValueError")
    print("Goodbye from fun1()")


def fun2():
    try:
        fun1()
    except:
        raise
    print("Goodbye from fun2()")


fun2("hi")
