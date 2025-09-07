def showHeader():
    print('-----------------------------------------')
    print('   เครื่องคิดเลข')
    print('-----------------------------------------')

def showMenu():
    print('1. บวก')
    print('2. ลบ')
    print('3. คูณ')
    print('4. หาร')
    menu = int(input('ป้อนเมนูที่ต้องการ : '))
    print('-----------------------------------------')
    return menu


def inputnum1():
    num1 = float(input('ป้อนจํานวนที่ 1 : '))
    return num1

def inputnum2():
    num2 = float(input('ป้อนจํานวนที่ 2 : '))
    print('-----------------------------------------')
    return num2 

def calculate(menu, num1, num2):
    if menu == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif menu == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif menu == 3:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif menu == 4:
        if num2 != 0:
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print('ไม่สามารถหารด้วยศูนย์ได้')
    else:
        print('เมนูไม่ถูกต้อง')
    print('-----------------------------------------')

showHeader()
menu = showMenu()
num1 = inputnum1()  
num2 = inputnum2() 
calculate(menu, num1, num2)