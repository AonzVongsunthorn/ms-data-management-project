import re
import random
import string
from datetime import date

def random_password() :
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))

def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)

def generate_wifi_key():

    try:
        id = input_id_card()
        if(id == 'x') :
            return
        mobileNumber = input_mobile_number()
        if (mobileNumber == 'x'):
            return
        password = random_password()
        today = date.today()

        with open('./data/wifi.txt', 'a', encoding='utf-8') as file:
            file.write(id+','+mobileNumber+','+password+','+today.strftime("%d/%m/%Y")+'\n')
        file.close()

        border_msg(" password: "+password+" ")

    except Exception as e:
        print("Something wrong on product.py -> write_data", + str(e))

def input_id_card():
    while (1):
        id = input("Enter the Thai ID Card or [x] to exit => ")

        if(id == 'x'):
            break

        if (re.match('^[1-9]{1}[0-9]{12}$', id)):
            break
    return id

def input_mobile_number():
    while (1):
        id = input("Enter the mobile number or [x] to exit => ")

        if (id == 'x'):
            break

        if (re.match('^[0]{1}[1-9]{1}[0-9]{8}$', id)):
            break
    return id
