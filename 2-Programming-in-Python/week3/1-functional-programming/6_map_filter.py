menu = ['Espresso', 'Latte', 'Cappucino', 'Macchiato', 'Americano', 'Decaf']


def find_coffee(coffee):
    if coffee.lower().startswith('c'):
        # if coffee[0].lower() == 'c':
        return coffee


# map_coffee = map(find_coffee, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)
