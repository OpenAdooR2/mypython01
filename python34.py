
for a in range(2):
    def showHeader():
        print('*****************************************')
        print('****              BMI Program                ****')
        print('*****************************************')
    def inputName():
        name = input('ป้อนชื่อ : ')
        return name

    def inputYear():
        year = input('ป้อนปี พ.ศ. เกิด : ')
        return year

    def inputWeight():
        weight = float(input('ป้อนน้ำหนัก : '))
        return weight

    def inputHeight():
        height = float(input('ป้อนส่วนสูง : '))
        return height

    def calculateBMI(weight, height):
        BMI = weight / (height/100)**2
        return BMI
    def prapra ():
        print('*****************************************')
        return prapra
    def showPerson(name, year, weight, height):
        print(f'คุณ{name} เกิดปี พ.ศ. {year} อายุ {2568 - int(year)} ปี')
        print(f'น้ำหนัก {weight} กิโลกรัม ส่วนสูง {height} เซนติเมตร')

    def showBMI(BMI):
        print(f'ค่า BMI ที่คำนวณได้ คือ {BMI:.2f}')
        if BMI < 18.5:
            print('แปลค่าค่า BMI ที่คำนวณได้ คือ น้ำหนักน้อยไป')
        elif BMI >= 18.5 and BMI < 22.99:
            print('แปลค่าค่า BMI ที่คำนวณได้ คือ น้ำหนักปกติ')
        elif BMI >= 23 and BMI < 24.99:
            print('แปลค่าค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (ท้วม)')
        elif BMI >= 25 and BMI < 29.99:
            print('แปลค่าค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (อ้วนระยะเริ่มต้น)')
        elif BMI >= 30 and BMI < 39.99:
            print('แปลค่าค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (อ้วนมาก)')
        else:
            print('แปลค่าค่า BMI ที่คำนวณได้ คือ น้ำหนักเกิน (อ้วนระดับรุนแรงมาก)')
        print('*****************************************')

    showHeader()
    name = inputName()
    year = inputYear()
    weight = inputWeight()
    height = inputHeight()
    prapra()
    showPerson(name, year, weight, height)
    BMI = calculateBMI(weight, height)
    showBMI(BMI)