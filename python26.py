# 3. function ที่ไม่มี parameter และมี return
# มี return คือ มีคำสั่ง return ในตัวฟังก์ชันพร้อมกับข้อมูลที่จะส่งกลับไปยังจุดเรียกใช้ฟังก์ชั่น

def funcWow( ) :
    return 'Wow Wow Wow'

def funcHi( ) :
    print('Hi...')
    return 'สวัสดี'

print(funcWow( ))
dti= (funcWow( ))
print(dti,dti,dti)

print(f'{funcHi( )}สมชาย')