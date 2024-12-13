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

