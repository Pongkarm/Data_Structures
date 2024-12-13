a = [4, 7, 9, 2, 6, 8, 9, 4, 7, 9, 2, 6, 8, 9, 1]

def Bubble_sort(a_list):
    n = len(a_list)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            #swap
            if a_list[j] > a_list[j+1] :
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                flag = 1
        if flag == 0:
            break
    return a_list

print(a)
print(Bubble_sort(a))