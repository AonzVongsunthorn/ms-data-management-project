from .product import get_product
import pandas as pd

def generate_product_report():
    try:
        itemList = []
        indexes = []
        with open('./data/order_items.txt', "r") as f:
            orders = f.readlines()
            for order in orders:
                if (order == ''):
                    continue
                orderData = order.strip().split(",")
                indexes.append(orderData[1])
                itemList.append({
                    'Code': orderData[1],
                    'Name': get_product(orderData[1])['name'],
                    'Qty': int(orderData[2]),
                    'Total(฿)': (int(orderData[2]) * int(orderData[3]))
                })

            df = pd.DataFrame(itemList, index=indexes)
            df = df.groupby(['Code','Name'], as_index=False)['Qty', 'Total(฿)'].sum()
            df = df.sort_values('Total(฿)', ascending=False)
            indexes = df['Code']
            del df['Code']
            df = df.set_index(indexes)
            print(df)

    except Exception as e:
        print("Something wrong on report.py -> generate_product_report")


def generate_order_report():
    try:
        orderList = []
        indexes = []
        with open('./data/orders.txt', "r") as f:
            orders = f.readlines()
            for order in orders:
                if (order == ''):
                    continue

                orderData = order.strip().split(",")
                indexes.append(orderData[0])
                orderList.append({
                    'Date': orderData[1],
                    'Total(฿)': float(orderData[4]),
                })

            df = pd.DataFrame(orderList, index=indexes)
            df = df.groupby(['Date'], as_index=True)['Total(฿)'].sum().reset_index()
            # df = df.sort_values('Total(฿)', ascending=False)
            print(df)

    except Exception as e:
        print("Something wrong on report.py -> generate_order_report")


def list_menu():
    try:
        while (1):
            print('********************* Select the menu to get the report. *********************')
            print("[1]. Show by product")
            print("[2]. Show by date")
            print("[x]. Exit")

            menu = input("Please select menu   => ")

            if menu == '1':
                generate_product_report()
            elif menu == '2':
                generate_order_report()
            elif menu == 'x':
                break
            else:
                print("Incorrect menu.")

    except Exception as e:
        print("Something wrong on report.py -> list_menu")
