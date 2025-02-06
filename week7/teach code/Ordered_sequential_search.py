#ตรวจดูว่ามีของที่หาหรือเปล่าเท่านั้น คืนค่าเป็น True false และของที่เอามาเช็คต้อง sort แล้ว
def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        #flat
        elif a_list[pos] > item:
            stop = True
        else:
            pos = pos + 1
    return found

if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(ordered_sequential_search(test_list, 3)) #False
    print(ordered_sequential_search(test_list, 13)) #True