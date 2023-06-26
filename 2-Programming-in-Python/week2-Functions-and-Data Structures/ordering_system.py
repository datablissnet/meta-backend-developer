menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


def calculate_subtotal(order):
    """Calculates the subtotal of an order

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float: The sum of the prices of the items in the order
    """
    subtotal = sum(item["price"] for item in order)
    return subtotal


def calculate_tax(subtotal):
    """Calculates the tax of an order

    Args:
        subtotal: the price to get the tax of

    Returns:
        float: The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    tax = subtotal * 0.15
    return round(tax, 2)


def summarize_order(order):
    """Summarizes the order

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple: A tuple containing a list of item names and the total amount including tax.
    """
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    names = [item["name"] for item in order]
    return names, round(total, 2)


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(
            f"{selection}. {menu[selection]['name']: <9} | {menu[selection]['price']: >5}")
    print()


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' +
                     str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, total = summarize_order(order)
    print("Items: " + ", ".join(items))
    print("Total: " + str(total))


if __name__ == "__main__":
    main()
