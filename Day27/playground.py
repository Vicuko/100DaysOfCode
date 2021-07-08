def add(*args):
    # args is a tuple:
    print(type(args))
    added_nums = sum(args)
    return added_nums

result = add(1,2,3,4,5,6)
print (result)

def calculate(**kwargs):
    # kwargs is a dictionary:
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key} : {value}")


calculate(add=3, multiply=5)