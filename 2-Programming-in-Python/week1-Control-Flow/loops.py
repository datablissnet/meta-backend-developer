# Starter Code
favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
else:
    print('No sorry, that dessert is not on my list')


# Starter Code
favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break
else:
    print('No sorry, not a dessert on my list')

# Starter Code
favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

# Starter Code
favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)
