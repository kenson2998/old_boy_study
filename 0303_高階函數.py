def func1(a, b, f):
    return f(a) + f(b)


print(func1(3, -7, abs))
