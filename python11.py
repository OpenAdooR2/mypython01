# สร้างโปรแกรมคำนวณผลรวมคะแนนโดยป้อนรหัส น.ศ. ชื่อ น.ศ.  คะแนนกลางภาค ปลายภาค เก็บทางแป้นพิมพ์
# และแสดงผลข้อมูลที่ป้อนและคะแนนรวมที่คำนวณได้

print('+++++++++++++++++++++++')
print('โปรแกรม score Total')
print('+++++++++++++++++++++++')
stu_ID = input('ป้อนรหัส นศ.: ')
stu_name = input('ป้อนชื่อ นศ.: ')
mid_SCORE = input('ป้อนคะแนนกลางภาค.: ')
final_score = input('ป้อนคะแนนปลายภาค.: ')
quize_score = input('ป้อนคะแนนเก็บ.: ')

sum_score = float(mid_SCORE) + float(final_score) + float (quize_score)

print(f'รหัส น.ศ. {stu_ID } ชื่อ {stu_name}')
print(f'กลางภาค {mid_SCORE} ปลายภาค {final_score} คะแนนเก็บเก็บ {quize_score} รวมเป็น {sum_score} คะแนน')

print('รหัส น.ศ.',stu_ID,'ชื่อ',stu_name)
print('กลางภาค' ,mid_SCORE, 'ปลายภาค' ,final_score, 'คะแนนเก็บ' ,quize_score, 'รวมเป็น' ,sum_score,)
print('+++++++++++++++++++++++')
print('รหัส น.ศ. '+stu_ID+' ชื่อ '+stu_name)
print('กลางภาค '+str(mid_SCORE)+ ' ปลายภาค '+str(final_score)+ ' คะแนนเก็บ ' +str(quize_score)+ ' รวมเป็น ' +str(sum_score))
print('+++++++++++++++++++++++')
print('รหัส น.ศ. {} ชื่อ {}'.format(stu_ID, stu_name))
print('กลางภาค {0} ปลายภาค {1} คะแนนเก็บ {2} รวมเป็น {3}' .format(mid_SCORE,final_score,quize_score,sum_score) )
print('+++++++++++++++++++++++')