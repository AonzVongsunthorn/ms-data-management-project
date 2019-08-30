import re
import modules.product as product
import modules.order as order
import modules.wifi as wifi
import modules.report as report

try:
    while (1):
        print("********************* Menu *******************")
        print("[1]. Add Order")
        print("[2]. Product Management")
        print("[3]. Generate WIFI key.")
        print("[4]. Report")
        print("[x]. Exit")
        menu = input("Please select menu   => ")

        if menu == '1':
            order.list_menu()
        elif menu == '2':
            product.list_menu()
        elif menu == '3':
            wifi.generate_wifi_key()
        elif menu == '4':
            report.generate_report()
        elif menu == 'x':
            break
        else:
            print("Incorrect menu.")
    print("Bye!")
except Exception as e:
    print("Something wrong on main.py", + str(e))