# break และ continue ใน loop
# break ใน loop ทำงานเมื่อใด ให้หยุดการทำงานใน loop ทันที
# continue ใน loop  ทำงานเมื่อใด ถือว่าจบรอบน้ำแล้วและให้ข้ามไปทำงานรอบถัดไป

for a in range(10):
    print(f'{a+1} Hi...')
    if a == 3:
        # break
        continue
    print(f'{a+1} Hello...')