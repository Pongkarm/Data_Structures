import numpy as np

def cross_product(A, B, P):
    """คำนวณ Cross Product เพื่อตรวจสอบว่าจุดอยู่ด้านใดของเส้น"""
    return (B[0] - A[0]) * (P[1] - A[1]) - (B[1] - A[1]) * (P[0] - A[0])

def interpolate(p1, p2, t):
    """คำนวณตำแหน่งจุดตัดด้วย Linear Interpolation"""
    return (1 - t) * np.array(p1) + t * np.array(p2)

def cut_polygon_with_line(polygon, pt1, pt2, epsilon=1e-9):
    """ตัดรูปหลายเหลี่ยมด้วยเส้นที่กำหนดโดยจุด pt1 และ pt2"""
    result = []
    n = len(polygon)
    
    for i in range(n):
        current = polygon[i]
        next_point = polygon[(i + 1) % n]
        
        left1 = cross_product(pt1, pt2, current)
        left2 = cross_product(pt1, pt2, next_point)
        
        # เพิ่มจุดปัจจุบันถ้าอยู่ด้านซ้ายของเส้น
        if left1 > -epsilon:
            result.append(current)
        
        # เพิ่มจุดตัดถ้าเส้นขอบตัดกับเส้นตรง
        if left1 * left2 < -epsilon:
            t = left1 / (left1 - left2)
            intersection = interpolate(current, next_point, t)
            result.append(intersection.tolist())
    
    return result

# ตัวอย่างการใช้งาน
polygon = [[1, 1], [5, 1], [5, 6], [1, 6]]  # รูปสี่เหลี่ยมจัตุรัส
pt1 = [3, 0]
pt2 = [3, 7]

cut_polygon = cut_polygon_with_line(polygon, pt1, pt2)
print("รูปหลายเหลี่ยมที่ถูกตัด:", cut_polygon)
