R1 = 3
R2 = 4
R3 = 5
R4 = 6
R5 = 7
R6 = 8

def Find_rt_parallel(r1, r2=None, r3=None):
    if r3 is None or r3 is None:  # ถ้ามีแค่ r1 และ r2
        return (r1 * r2) / (r1 + r2)
    return 1 / (1/r1 + 1/r2 + 1/r3)

def Find_r1_parallel(rt, r2=None, r3=None):
    if r3 is None or r3 is None:  # ถ้ามีแค่ r1 และ r2
        r1 = (r2 * rt) / (r2 - rt)
    else:  # ถ้ามี r1, r2, r3
        r1 = 1 / ((1 / rt) - (1 / r2) - (1 / r3))
    return r1

def Find_rt_series(r1, r2=None, r3=None):
    if r3 is None or r3 is None:  # ถ้ามีแค่ r1 และ r2
        return r1 + r2
    else:  # ถ้ามี r1, r2, r3
        return r1 + r2 + r3

def Find_r1_series(rt, r2=None, r3=None):
    if r3 is None or r3 is None:  # ถ้ามีแค่ r1 และ r2
        return rt - r2
    else:  # ถ้ามี r1, r2, r3
        return rt - r2 - r3

# Test cases

print("Find_rt_parallel(5, 3, 4):", Find_rt_parallel(5, 3, 4))  # Output ความต้านทานรวมในวงจรขนาน

print("Find_rt_parallel(R1, R2, R3):", Find_rt_parallel(R1, R2, R3))  # Output ความต้านทานรวมในวงจรขนานจากตัวแปร

print(Find_rt_series(R3, R4))

# คำนวณความต้านทานรวมในวงจรอนุกรม โดยคำนวณค่าความต้านทานจากการรวมผลของวงจรขนานและวงจรอนุกรม
ex1 = Find_rt_series(R1, R2, Find_rt_parallel(Find_rt_series(R3, R4), R5, R6))
print("ex1 (Find_rt_series):", ex1)
