def sum_recursive(n):
    if n == 1:  # Base case
        return 1
    return n + sum_recursive(n - 1)  # Recursive case

# ตัวอย่างการใช้งาน
num = 5
print(f"ผลรวมของตัวเลขตั้งแต่ 1 ถึง {num} คือ {sum_recursive(num)}")

# sum_recursive(5) = 5 + sum_recursive(4)
# sum_recursive(4) = 4 + sum_recursive(3)
# sum_recursive(3) = 3 + sum_recursive(2)
# sum_recursive(2) = 2 + sum_recursive(1)
# sum_recursive(1) = 1 (Base case)