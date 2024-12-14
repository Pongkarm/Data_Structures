import timeit
start_time = timeit.default_timer()

# def lnsertion_sort_revers(a_list):
#     n = len(a_list)
#     flag = 1
#     for i in range(1, n):
#         temp = a_list[i]
#         hole = i
#         while hole > 0 and a_list[hole - 1] < temp:
#             a_list[hole] = a_list[hole - 1]
#             hole -= 1
#             flag = 0
#         a_list[hole] = temp
#         if flag == 0:
#             break
#     return a_list

def lnsertion_sort_revers(a_list):
    n = len(a_list)
    for i in range(1, n):
        temp = a_list[i]
        hole = i
        while hole > 0 and a_list[hole - 1] < temp:
            a_list[hole] = a_list[hole - 1]
            hole -= 1
        a_list[hole] = temp
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
list_reversed = lnsertion_sort_revers(list_file)
# แสดงผล
output_file = f'week4/Result_Sort/{file}_lnsertion_.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")
#วิธี lnsertion
#amphoe ประมาณ 0.02 วินาที
#province ประมาณ 0.0008 วินาที
#tambol ประมาณ 2.3 วินาที
#mm ประมาณ 1.3 วินาที