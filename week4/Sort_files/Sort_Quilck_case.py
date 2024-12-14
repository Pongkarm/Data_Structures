
import timeit

start_time = timeit.default_timer()

def Quilck_sort_revers(a_list, start, end):

    if start < end:

        pIndex = QuickSort_partition(a_list, start, end)
        
  
        Quilck_sort_revers(a_list, start, pIndex - 1)
        
        
        Quilck_sort_revers(a_list, pIndex + 1, end)
    
    return a_list
def QuickSort_partition(a_list, start, end):
    pivot = a_list[end]
    pIndex = start  

    for i in range(start, end):
        if a_list[i] >= pivot:
            # Swap elements
            temp = a_list[i]
            a_list[i] = a_list[pIndex]
            a_list[pIndex] = temp
            pIndex += 1

    temp = a_list[pIndex]
    a_list[pIndex] = a_list[end]
    a_list[end] = temp

    return pIndex

#เปลี่ยนชื่อไฟล์เอาได้เลย

# week/amphoe.txt
# week4/mm.txt
# week4/province.txt
# week4/tambol.txt
#      VVVVVVV
file = 'tambol'
list_file = []
with open(f'week4/{file}.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        
#เริ่ม

list_reversed = Quilck_sort_revers(list_file, 0, len(list_file) - 1)
# แสดงผล
output_file = f'week4/Result_Sort/{file}_Quilck.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")
#วิธี Quilc
#amphoe ประมาณ 0.017 วินาที
#province ประมาณ 0.0008 วินาที
#tambol ประมาณ ---  maximum recursion depth exceeded
#mm ประมาณ ---   maximum recursion depth exceeded
