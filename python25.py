# 2. function ที่มี parameter และไม่มี return
# มี parameter คือ มีอะไรในวงเล็บหลังชื่อฟังชั่น
# parameter ถือว่าเป็นตัวแปรประเภทหนึ่งแต่จะใช้ได้เฉพาะในฟังชั่นนั้น เท่านั้น
# ไม่มี return คือ ไม่มีคำสั่ง return ในตัวฟังก์ชั่น

def sumNumber (aa,bb): #อย่าลืม colon
    print(f'ผลรวมของ {aa} และ {bb} เท่ากับ {aa+bb}')
    print('ok นะ')

def averageNumber (n1,n2,n3,n4): #อย่าลืม colon
    print(f'ค่าเฉลี่ยของ {n1},{n2},{n3},{n4} คือ {(n1+n2+n3+n4)/4}')
    print('เขาใจตรงกันนะ')

sumNumber(10, 20 )  #ข้อมูลที่ส่งให้พารามิเตอร์ เรียก Argument
sumNumber(111, 222 )
print('------------------')
averageNumber(10, 20, 32, 10)
print('------------------')
print('     ^_^')