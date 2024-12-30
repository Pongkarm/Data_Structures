import timeit
start_time = timeit.default_timer()

def QuickSort(a_list, start, end):

    if start < end:

        pIndex = QuickSort_partition(a_list, start, end)
        
  
        QuickSort(a_list, start, pIndex - 1)
        
        
        QuickSort(a_list, pIndex + 1, end)
    
    return a_list

def QuickSort_partition(a_list, start, end):
    pivot = a_list[end]
    pIndex = start  

    for i in range(start, end):
        if a_list[i] <= pivot:
            # Swap elements
            temp = a_list[i]
            a_list[i] = a_list[pIndex]
            a_list[pIndex] = temp
            pIndex += 1

    temp = a_list[pIndex]
    a_list[pIndex] = a_list[end]
    a_list[end] = temp

    return pIndex
a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]
QuickSort(a, 0, len(a) - 1)
print(a)

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")