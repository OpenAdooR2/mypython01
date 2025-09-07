# 4. function ที่มี parameter และมี return

def calSqareArea(width , longs):
    return width * longs

def func_info (id , name):
    print('Hi')
    return f'สวัสดี {id} คุณ {name}'
print(f'พท.กว้าง 20 ยาว 30 มีพื้นที่ {calSqareArea(20,30)}')
