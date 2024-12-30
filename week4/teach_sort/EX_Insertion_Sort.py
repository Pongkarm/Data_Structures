import timeit
start_time = timeit.default_timer()

def Insertion_sort(a_list):
    n = len(a_list)
    for i in range(1, n):
        temp = a_list[i]
        hole = i
        while hole > 0 and a_list[hole - 1] > temp:
            a_list[hole] = a_list[hole - 1]
            hole -= 1
        a_list[hole] = temp
    return a_list

a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

print("Original list:", a)
print("Sorted list:", Insertion_sort(a))


elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")