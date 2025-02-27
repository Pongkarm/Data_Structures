# def coutdown(n):
#     if n <= 0:
#         print('done')
#         return
#     print(n)
#     coutdown(n - 1)
    
# coutdown(5)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # ถ้าอาร์เรย์มี 1 ตัวหรือน้อยกว่า ให้ return เลย

    pivot = arr[0]  # เลือก pivot เป็นตัวแรก
    left = [x for x in arr[1:] if x < pivot]  # ค่าที่น้อยกว่า pivot
    right = [x for x in arr[1:] if x >= pivot]  # ค่าที่มากกว่าหรือเท่ากับ pivot

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [5, 2, 9, 1, 5, 6]
sorted_arr = quick_sort(arr)
print(sorted_arr)

arr.sort()