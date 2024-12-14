
import timeit

start_time = timeit.default_timer()
def Selection_sort_revers(a_list):
    n = len(a_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a_list[j] > a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

    return a_list

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
list_reversed = Selection_sort_revers(list_file)
# แสดงผล
output_file = f'week4/Result_Sort/{file}_Selection.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")
#วิธี Selection
#amphoe ประมาณ 0.019 วินาที
#province ประมาณ 0.0006 วินาที
#tambol ประมาณ 1.2 วินาที
#mm ประมาณ 0.69 วินาที