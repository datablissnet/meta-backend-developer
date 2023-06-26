def divide_by(a, b):
    return a/b


try:
    print(divide_by(5, 0))
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "Something went wrong")
