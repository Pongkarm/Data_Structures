# ฟังก์ชัน ccw คำนวณการหมุน
def ccw(A, B, C):
    cross_product = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if cross_product > 0:
        return 1  # counterclockwise
    elif cross_product < 0:
        return -1  # clockwise
    else:
        return 0  # collinear (เส้นตรง)

# ฟังก์ชันตรวจสอบ polygon ว่าเป็น convex หรือไม่
def is_convex_polygon(P):
    sz = len(P)
    if sz < 3:
        return False  # ต้องมีอย่างน้อย 3 จุด

    # คำนวณทิศทางการหมุนแรก
    firstTurn = ccw(P[0], P[1], P[2])

    # วนลูปตรวจสอบทิศทางการหมุนทั้งหมด
    for i in range(1, sz - 1):
        tmp = 1 if (i + 2 == sz) else i + 2
        if ccw(P[i], P[i + 1], P[tmp]) != firstTurn:
            return False  # ถ้าทิศทางไม่เหมือนกัน ไม่ใช่ convex

    return True  # ทิศทางเหมือนกันหมด เป็น convex polygon

# ทดสอบด้วยข้อมูลตัวอย่าง
P_convex = [(0, 0), (4, 0), (4, 4), (0, 4)]  # Convex (สี่เหลี่ยม)
P_non_convex = [(0, 0), (4, 0), (2, 2), (4, 4), (0, 4)]  # Non-convex

print("P_convex is convex:", is_convex_polygon(P_convex))  # ควรได้ True
print("P_non_convex is convex:", is_convex_polygon(P_non_convex))  # ควรได้ False
