import re
import pandas as pd
filename = "./data/products.txt"

def list_menu():
    try:
        while (1):
            print('********************* Product Management *********************')
            print("[1]. Show Products ")
            print("[2]. Add Product")
            print("[3]. Edit Product ")
            print("[4]. Delete Product")
            print("[x]. Go to main menu")
            menu = input("Please select menu   => ")

            if menu == '1':
                show_product()
            elif menu == '2':
                add_product()
            elif menu == '3':
                edit_product()
            elif menu == '4':
                delete_product()
            elif menu == 'x':
                break
            else:
                print("Incorrect menu.")
    except Exception as e:
        print("Something wrong on product.py -> list_menu")

def get_products(isShowOnlyAvailable = False):
    try:
        productList = []
        with open(filename, "r") as f:
            products = f.readlines()
            for product in products:
                if (product == ''):
                    continue
                productData = product.strip().split(",")

                if(isShowOnlyAvailable == True) :
                    if(productData[3] == 'D'):
                       continue

                productList.append({
                    'code': productData[0],
                    'name': productData[1],
                    'price': productData[2],
                    'status': productData[3],
                })
        return productList
    except Exception as e:
        print("Something wrong on product.py -> get_products")

def get_product(code):
    data = {}
    for product in get_products():
        if(product['code'] == code):
            data['code'] = product['code']
            data['name'] = product['name']
            data['price'] = product['price']
            break
    return data

def get_product_codes():
    try:
        codes = []
        for product in get_products():
            codes.append(product['code'])
        return codes
    except Exception as e:
        print("Something wrong on product.py -> get_product_codes")

def show_product(isShowOnlyAvailable = False):
    try:
        productList = []
        indexes = []
        for product in get_products(isShowOnlyAvailable):
            indexes.append(product['code'])
            productList.append({
                 'Product': product['name'],
                 'Price': product['price'],
                 'Status': product['status'],
            })

        df = pd.DataFrame(productList, index=indexes)
        df.sort_index(inplace=True)
        print("********************* Product *********************")
        print(df)
    except Exception as e:
        print("Something wrong on product.py -> show_product")

def write_data(txt):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(txt)
        file.close()
    except Exception as e:
        print("Something wrong on product.py -> write_data")

def re_write_products(products):
    open(filename, "w").close()
    for product in products:
        write_data(product['code'] + "," + product['product'] + "," + product['price']+ "," + product['status'] + "\n")

def add_product():
    try:
        code = input_code()
        name = input_name()
        price = input_price()
        write_data(code + "," + name + "," + price + ",A\n")
    except Exception as e:
        print("Something wrong on product.py -> add_product")

def edit_product():

    existingCodes = get_product_codes()
    try:
        while (1):
            show_product()
            code = input('Enter product code to "update" or [x] to exit: ')
            if(code == 'x') :
                break

            if (code not in existingCodes):
                print('Not found the product code', code)
                continue

            name = input_name()
            price = input_price()

            products = []
            for product in get_products():

                if(product['code'] == code) :
                    products.append({
                        'code': code,
                        'product': name,
                        'price': price,
                        'status':product['status']
                    })
                else :
                    products.append({
                        'code': product['code'],
                        'product': product['name'],
                        'price': product['price'],
                        'status': product['status']
                    })
            re_write_products(products)

    except Exception as e:
        print("Something wrong on product.py -> edit_product")


def delete_product():
    existingCodes = get_product_codes()
    try:
        while (1):
            show_product()
            code = input('Enter product code to "delete" or [x] to exit: ')
            if (code == 'x'):
                break

            if (code not in existingCodes):
                print('Not found the product code', code)
                continue

            products = []
            for product in get_products():

                if (product['code'] != code):
                    products.append({
                        'code': product['code'],
                        'product': product['name'],
                        'price': product['price'],
                        'status': product['status'],
                    })
                else:
                    products.append({
                        'code': product['code'],
                        'product': product['name'],
                        'price': product['price'],
                        'status': 'D',
                    })

            re_write_products(products)
    except Exception as e:
        print("Something wrong on product.py -> delete_product")

def input_code():

    existingCodes = get_product_codes()
    while (1):
        code = input("Enter the code (accept only number with 3 digit example 001) => ")

        if(code in existingCodes) :
            print('The code is using by some product already!')
            continue

        if (re.match('^[0-9]{3}$', code)):
            break
    return  code

def input_name():
    while (1):
        name = input("Enter the product name => ")
        if (re.match('\w', name)):
            break
    return  name

def input_price():
    while (1):
        price = input("Enter the product price => ")
        if (re.match('^[1-9][0-9]*$', price)):
            break
    return  price
