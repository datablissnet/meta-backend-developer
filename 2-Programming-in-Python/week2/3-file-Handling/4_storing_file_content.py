import random
with open("./petnames.txt", "r") as file:
    data = file.read().split()
print(data)


print(random.choice(data))
