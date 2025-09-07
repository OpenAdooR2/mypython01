print('-----------------------------------------')
print('            โปรแกรมคิดเงินทอน')
print('-----------------------------------------')
for a in range(9999999999999):
    print(f'รายการที่  {a+1}')
    price = float(input(f'\nราคาสินค้า :  '))
    paid = float(input('รับเงินมา  :  '))

    while paid < price:
        print(f'เงินไม่พอ จ่ายเพิ่มอีก :',abs(paid - price), 'บาท')
        more = float(input('จำนวนเงินที่จ่ายเพิ่ม  : '))
        paid += more


    change = paid - price
    print(f'\nเงินทอนทั้งหมด: {change:,.2f} บาท')


    denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    for d in denominations:
        count = int(change // d)
        change = round(change % d, 2)
        if count > 0:
            if d >= 20:
                print(f'แบงค์   {d}  บาท : {count} ใบ')
            else:
                print(f'เหรียญ  {d}    บาท : {count} เหรียญ')

    end = input(f'\nรายการถัดไป ')
    print('-----------------------------------------')
    if end.lower() == 'close':
        print(f'\nทั้งหมด {a+1} รายการ')
        break