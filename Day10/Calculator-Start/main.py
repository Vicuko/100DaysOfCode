def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number? "))
for key in operations:
    print(key)
operation = input("Pick an operation from the ones above: ")
num2 = int(input("What's the second number? "))

if operation in operations:
    function = operations[operation]
    answer = function(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
