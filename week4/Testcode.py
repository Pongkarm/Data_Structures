a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

def Bubble_sort(a_list):
    n = len(a_list)
    while True:    
        if a_list[j] > a_list[j+1] :
            a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
            flag = 1
    return a_list

print(a)
print(Bubble_sort(a))