import re
from .product import show_product,get_product_codes,get_product
import pandas as pd
from datetime import date

orderFile = "./data/orders.txt"
orderItemsFile = "./data/order_items.txt"

def add_items(items):

    try:
        show_product()
        while (1):
            code = input("Please enter the product code or [x] to exit  => ")
            if (code == 'x'):
                break

            if (code not in get_product_codes()):
                print('Not found the product code', code)
                show_product()
                continue

            while (1):
                qty = input("Please enter the quantity or [x] to exit  => ")
                if (qty == 'x'):
                    break
                if (re.match('^[1-9][0-9]*$', qty)):
                    break

            if (qty == 'x'):
                break

            items.append({
                'product': code,
                'qty': qty
            })

        return items

    except Exception as e:
        print("Something wrong on order.py -> add_items", + str(e))

def remove_item(items):
    try:
        while (1):
            if (len(items) == 0):
                print("No item!")
                return items

            for idx, item in enumerate(items):
                print("["+str(idx)+"]", get_product(item['product'])['name'], item['qty'])
            code = input("Please enter the number of above list to remove or [x] to exit  => ")
            if (code == 'x'):
                break

            try:
                code = int(code)
                if (int(code) <= len(items) - 1):
                    items.pop(code)
                else:
                    print("The number incorrect!")
            except ValueError:
                print('Valid number, please')
                continue
        return items
    except Exception as e:
        print("Something wrong on order.py -> remove_item", + str(e))

def write_data(filename, txt):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(txt)
        file.close()
    except Exception as e:
        print("Something wrong on product.py -> write_data", + str(e))

def save_order(items):
    try:
        if (len(items) == 0):
            print("No item!")
            return
        totalPrice = 0
        for item in items:
            product = get_product(item['product'])
            totalPrice = totalPrice + (int(item['qty']) * int(product['price']))

        with open(orderFile, 'r') as f:
            lines = f.read().splitlines()
            if(len(lines) > 0) :
                lastLine = lines[-1]
                orderData = lastLine.split(',')
                nextId = str(int(orderData[0]) + 1)
            else:
                nextId = '1'

            today = date.today()
            orderText = nextId+','+today.strftime("%d/%m/%Y")+','+str(totalPrice)+'\n'
            write_data(orderFile, orderText)

        for item in items:
            product = get_product(item['product'])
            itemText = nextId+','+item['product']+','+item['qty']+','+product['price']+'\n'
            write_data(orderItemsFile, itemText)

    except Exception as e:
        print("Something wrong on order.py -> save_order", + str(e))

def show_items(items):

    if(len(items) == 0):
        print("No item!")
        return

    itemList = []
    indexes = []
    totalPrice = 0
    for item in items:
        product = get_product(item['product'])
        indexes.append(item['product'])
        itemList.append({
            'Product': product['name'],
            'Price': product['price'],
            'Qty': item['qty'],
            'Total': int(item['qty']) * int(product['price']),
        })
        totalPrice = totalPrice + (int(item['qty']) * int(product['price']))

    itemList.append({
        'Product': '',
        'Price': '',
        'Qty': '',
        'Total': totalPrice,
    })
    indexes.append('Total')
    df = pd.DataFrame(itemList, index=indexes)
    print(df)

def list_menu():

    try:
        items = []
        while (1):
            print('********************* Menu New Order *********************')
            print("[1]. Add Item")
            print("[2]. Show Items")
            print("[3]. Remove Item")
            print("[s]. Save & Exit")
            print("[x]. Cancel")

            menu = input("Please select menu   => ")

            if menu == '1':
                items = add_items(items)
            elif menu == '2':
                show_items(items)
            elif menu == '3':
                items = remove_item(items)
            elif menu == 's':
                save_order(items)
                break
            elif menu == 'x':
                break
            else:
                print("Incorrect menu.")

    except Exception as e:
        print("Something wrong on order.py -> add_items", + str(e))