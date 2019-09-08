import re
import pandas as pd
filename = "./data/members.txt"

def list_menu():
    try:
        while (1):
            print('********************* Member Management *********************')
            print("[1]. Show Members ")
            print("[2]. Add Members")
            print("[3]. Edit Members")
            print("[4]. Delete Members")
            print("[x]. Go to main menu")
            menu = input("Please select menu   => ")

            if menu == '1':
                show_member()
            elif menu == '2':
                add_member()
            elif menu == '3':
                edit_member()
            elif menu == '4':
                delete_member()
            elif menu == 'x':
                break
            else:
                print("Incorrect menu.")
    except Exception as e:
        print("Something wrong on product.py -> list_menu")

def get_members(isShowOnlyAvailable = False):
    try:
        memberList = []
        with open(filename, "r") as f:
            members = f.readlines()
            for member in members:
                if (member == ''):
                    continue

                memberData = member.strip().split(",")
                if (isShowOnlyAvailable == True):
                    if (memberData[3] == 'D'):
                        continue

                memberList.append({
                    'mobileNumber': memberData[0],
                    'name': memberData[1],
                    'email': memberData[2],
                    'status': memberData[3],
                })
        return memberList
    except Exception as e:
        print("Something wrong on member.py -> get_members")

def get_product_codes():
    try:
        codes = []
        for member in get_members():
            codes.append(member['code'])
        return codes
    except Exception as e:
        print("Something wrong on product.py -> get_product_codes")

def show_member(isShowOnlyAvailable = False):
    try:
        productList = []
        indexes = []
        for member in get_members(isShowOnlyAvailable):
            indexes.append(member['mobileNumber'])
            productList.append({
                'Name': member['name'],
                'Email': member['email'],
                'Status': member['status'],
            })

        df = pd.DataFrame(productList, index=indexes)
        df.sort_index(inplace=True)
        print("***************** Member *****************")
        print(df)
    except Exception as e:
        print("Something wrong on product.py -> show_product")

def write_data(txt):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(txt)
        file.close()
    except Exception as e:
        print("Something wrong on member.py -> write_data")

def add_member():
    mobile_number = input_mobile_number()
    if (mobile_number == 'x'):
        return
    email = input_email()
    if(email == 'x'):
        return
    name = input_name()
    if (name == 'x'):
        return
    write_data(mobile_number+','+name+','+email+',A'+'\n')

def get_existing_mobile_number():
    try:
        codes = []
        for member in get_members():
            codes.append(member['mobileNumber'])
        return codes
    except Exception as e:
        print("Something wrong on product.py -> get_product_codes")

def re_write(members):
    open(filename, "w").close()
    for member in members:
        write_data(member['mobileNumber'] + "," + member['name'] + "," + member['email']+ "," + member['status'] + "\n")

def edit_member():
    existingCodes = get_existing_mobile_number()
    try:
        while (1):
            show_member()
            code = input('Enter mobile number to "update" or [x] to exit: ')
            if(code == 'x') :
                break

            if (code not in existingCodes):
                print('Not found the mobile number', code)
                continue

            email = input_email()
            if (email == 'x'):
                return
            name = input_name()
            if (name == 'x'):
                return
            members = []
            for member in get_members():

                if(member['mobileNumber'] == code) :
                    members.append({
                        'mobileNumber': code,
                        'name': name,
                        'email': email,
                        'status':member['status']
                    })
                else :
                    members.append({
                        'mobileNumber': member['mobileNumber'],
                        'name': member['name'],
                        'email': member['email'],
                        'status': member['status']
                    })
            re_write(members)

    except Exception as e:
        print("Something wrong on product.py -> edit_product")

def delete_member():
    existingCodes = get_existing_mobile_number()
    try:
        while (1):
            show_member()
            code = input('Enter mobile number to "delete" or [x] to exit: ')
            if (code == 'x'):
                break

            if (code not in existingCodes):
                print('Not found the mobile number', code)
                continue

            members = []
            for member in get_members():
                if (member['mobileNumber'] == code):
                    members.append({
                        'mobileNumber': member['mobileNumber'],
                        'name': member['name'],
                        'email': member['email'],
                        'status': 'D'
                    })
                else:
                    members.append({
                        'mobileNumber': member['mobileNumber'],
                        'name': member['name'],
                        'email': member['email'],
                        'status': member['status']
                    })
            re_write(members)

    except Exception as e:
        print("Something wrong on product.py -> edit_product")

def input_email():
    while (1):
        email = input("Enter the email or [x] to exit => ")
        if (re.match('^[\w\.]+@([\w-]+\.)+[\w-]{2,4}$', email)):
            break
    return email

def input_name():
    while (1):
        name = input("Enter the name or [x] to exit => ")
        if (name == 'x'):
            break
        if (re.match('\w', name)):
            break
    return  name

def input_mobile_number():
    while (1):
        mobileNumber = input("Enter the mobile number or [x] to exit => ")

        if(mobileNumber in get_existing_mobile_number()) :
            print('Duplicate mobile number!!')
            continue

        if (mobileNumber == 'x'):
            break

        if (re.match('^[0]{1}[1-9]{1}[0-9]{8}$', mobileNumber)):
            break
    return mobileNumber
