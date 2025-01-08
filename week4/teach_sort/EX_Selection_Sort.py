import timeit
start_time = timeit.default_timer()
def Selection_sort(a_list):
    n = len(a_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

    return a_list

a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]
sorted_list = Selection_sort(a)
print("Sorted list:", sorted_list)

print(a)
print(Selection_sort(a))

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")

#เริ่มที่ line 5 
a = [4, 7, 9, 2]
# รอบที่ 1
# i = 0 
# min_index = 0
#j = 1 loop j จะวนจนกว่าจะถึง n โดยเริ่มที่ i+1   (line 7)
#ตรวจสอบเงื่อนไข a[j](ตำแหน่งที่1) < a[min_index](ตำแหน่งที่0) ในครั้งนี้หมายความว่า ถ้า 7<4 เป็นจริงจึงทำ if (line 8)
#เปลียน min_index เป็น j ซึ่งคือ 1
#min_index = 1 
#จากนั้นเริ่มloopใหม่ j+1 = 2
#ตรวจสอบเงื่อนไข a[j](ตำแหน่งที่2) < a[min_index](ตำแหน่งที่1) หมายความว่า ถ้า 9<7 ซึ่งไม่จริงก็เริ่มลูปใหม่ต่อไป
# j+1 = 3
#min_index = 1 
#ตรวจสอบเงื่อนไข a[j](ตำแหน่งที่3) < a[min_index](ตำแหน่งที่1) หมายความว่า ถ้า 2<7 เป็นจริงจึงทำ if (line 8)
#เปลียน min_index เป็น j ซึ่งคือ 3
#min_index = 3
#จบ for loop j เพราะถึง n แล้ว
#จากน้้นสลับค่าน้อยที่สุดใน min_index มาไว้ใน ช่องตำแหน่ง i(ตำแหน่งที่0) และแทนที่ i(ตำแหน่งที่0)คืนไปใน ตำแหน่ง min_index
#เปลี่ยนตำแหน่ง i = 0 min_index = 3
#ใน list จะเป็นอย่างงี้ [4, 7, 9, 2] >> [2, 7, 9, 4]
# รอบที่ 2 จะทำวนไปเรื่องๆเหมือนเดิม ทุกครั้งจบ for loop i จะได้ค่าน้อยที่สุดของที่เหลือมาสลับ ^-^

#เข้าใจแล้วใช่ไหม..... ถ้าคุณไม่เข้าใจ  ใช้ถูกแล้วผมก็งงเหมือนกันว่ากุเขียนเหี้ยอะไรลงไป 555 เดินมาถามๆของอยางงี้มันเขียนอธิบายให้เข้าใจยากสู้ๆครับ