def showHeader():
    print('-----------------------------------------')
    print('   เครื่องคิดเลข')
    print('-----------------------------------------')

def shoqMenu():
    print('1. บวก')
    print('2. ลบ')
    print('3. คูณ')
    print('4. หาร')
    menu = int(input('ป้อนเมนูที่ต้องการ : '))
    print('-----------------------------------------')
    return menu
def calculate():
    num1 = float(input('ป้อนจํานวนที่ 1 : '))
    num2 = float(input('ป้อนจํานวนที่ 2 : '))
    print('-----------------------------------------')
    if menu == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif menu == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif menu == 3:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif menu == 4:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('เมนูไม่ถูกต้อง')

showHeader()
menu = shoqMenu()
calculate()