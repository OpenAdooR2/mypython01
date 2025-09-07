def showProgramName():
    print('-----------------------------------------')
    print('   Calculate of circle')
    print('-----------------------------------------')

def inputRadius():
    radius = float(input('ป้อนรัศมี : '))
    return radius
    
def calAndshow():
    r = inputRadius()
    print('-----------------------------------------')
    print(f'พื้นที่วงกลม : {3.1416*r*2:,.2f}')
    print(f'เส้นรอบวงกลม : {2*3.14*r:,.2f}')
    print('-----------------------------------------')

showProgramName()
calAndshow()
print('Bye Bye')
