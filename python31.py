

def inputRadius():
    print('-----------------------------------------')
    print('   Calculate of circle')
    print('-----------------------------------------')
    radius = float(input('ป้อนรัศมี : '))
    return radius

def calculateArea(r):
    return 3.1416 * r * r

def calline(r):
    return 2 * 3.1416 * r

def showAreaAndCalline(area, calline):
    print(f'พื้นที่วงกลม : {area:,.2f}')
    print(f'เส้นรอบวงกลม : {calline:,.2f}')
    

readius = inputRadius()
print('-----------------------------------------')
area = calculateArea(readius)
line = calline(readius)
showAreaAndCalline(area,line)
print('-----------------------------------------')