# เขียนโปรแกรมคำนวณพื้นที่วงกลม และเส้นรอบวงกลม โดยรับค่ารัศมีทางแป้นพิมพ์ แล้วแสดงผลพื้นที่และเส้นรอบวงกลมที่คำนวณได้ทางหน้าจอ

# รับค่ารัศมี
# คํานวณพื้นที่
# คํานวณเส้นรอบวงกลม
# แสดงผลพื้นที่และเส้นรอบวงกลม
# แสดงชื่อโปรแกรม

def showProgramName():
    print('-----------------------------------------')
    print('   Calculate of circle')
    print('-----------------------------------------')

def inputRadius():
    radius = float(input('ป้อนรัศมี : '))
    return radius

def calculateArea(r):
    return 3.1416 * r * r

def calline(r):
    return 2 * 3.1416 * r

def showAreaAndCalline(area, calline):
    print(f'พื้นที่วงกลม : {area:,.2f}')
    print(f'เส้นรอบวงกลม : {calline:,.2f}')
    
showProgramName()
readius = inputRadius()
print('-----------------------------------------')
area = calculateArea(readius)
line = calline(readius)
showAreaAndCalline(area,line)
print('-----------------------------------------')