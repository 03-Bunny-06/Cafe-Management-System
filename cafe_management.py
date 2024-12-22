menu = {
    'Cappuccino': 140,
    'Latte': 120,
    'Americano': 150,
    'Espresso': 130,
    'Hot Chocolate': 200,
    'Milkshake': 150,
    'Pizza': 250,
    'French Fries': 90
}

print('---Welcome to Magic Cafe---')
print('1. Cappuccino Rs:140\n2. Latte Rs:120\n3. Americano Rs:150\n4. Espresso Rs:130\n5. Hot Chocolate Rs:200\n6. Milkshake Rs:150\n7. Pizza Rs:250\n8. French Fries Rs:90 ')

lis =[]
def item_order():
    item = input('Enter the name of the item you want to order: ')
    if item in menu:
        lis.append(menu[item])
        print(f'Your item {item.upper()} has been added to your order.')
    else:
        print(f'The item {item.upper()} you ordered is not available.')

item_order()

while True:
    order_again = input('Want to add another item? (Yes/No): ').lower()
    if(order_again == 'yes'):
        item_order()
    else:
        print(f'The total amount of items to pay is Rs.{sum(lis)}')
        break