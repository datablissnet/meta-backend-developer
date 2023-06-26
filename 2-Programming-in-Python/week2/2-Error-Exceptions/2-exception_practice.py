# Starter code
# Task 1
items = [1, 2, 3, 4, 5]
# item = items[6]
# print(item)
# solution
# try:
#     item = items[6]
#     print(item)
# except Exception as e:
#     print(e, "The index does not exist in the list.")

# TAsk 2
# Starter code


# def divide_by(a, b):
#     return a / b


# ans = divide_by(40, 0)
# print(ans)

def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')


ans = divide_by(10, 0)
print(ans)

# Task 3
# Starter code
# with open('file_does_not_exist.txt', 'r') as file:
#     print(file.read())


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")
