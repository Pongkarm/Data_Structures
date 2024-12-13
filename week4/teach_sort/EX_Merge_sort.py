import timeit
start_time = timeit.default_timer()

def MergeSort(a_list):
    n = len(a_list)
    
    # Base case: If the list has 1 or no elements, it's already sorted
    if n < 2:
        return a_list

    # Split the list into two halves
    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    # Recursively sort both halves
    MergeSort(left)
    MergeSort(right)

    # Merge the sorted halves
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list
    k = 0  # Pointer for the merged list

    # Merge elements from left and right into a_list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_list[k] = left[i]
            i += 1
        else:
            a_list[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left list
    while i < len(left):
        a_list[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right list
    while j < len(right):
        a_list[k] = right[j]
        j += 1
        k += 1

    return a_list

a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

print(MergeSort(a))

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")