def cross_product(A, B, P):
    return (B[0] - A[0]) * (P[1] - A[1]) - (B[1] - A[1]) * (P[0] - A[0])

def cut_polygon(polygon, A, B):
    EPS = 1e-9  # ค่าความคลาดเคลื่อน
    result = []
    n = len(polygon)

    for i in range(n):
        current_point = polygon[i]
        next_point = polygon[(i + 1) % n]
        
        left1 = cross_product(A, B, current_point)
        left2 = cross_product(A, B, next_point)
        
        # เพิ่มจุดถ้าจุดนั้นอยู่ด้านซ้ายของเส้น
        if left1 > -EPS:
            result.append(current_point)
        
        # ตรวจสอบว่ามีการตัดกันระหว่างเส้นขอบและเส้นตัด
        if left1 * left2 < -EPS:
            # คำนวณจุดตัด
            dx = next_point[0] - current_point[0]
            dy = next_point[1] - current_point[1]
            t = left1 / (left1 - left2)
            intersection = (
                current_point[0] + t * dx,
                current_point[1] + t * dy
            )
            result.append(intersection)
    
    return result

# ตัวอย่าง
polygon_points = [(0, 0), (4, 0), (4, 4), (0, 4)] #ตำแหน่งของรูป
cut_line_start = (2, -1) #ตำแหน่งของเส้นตัด 1
cut_line_end = (2, 5) #ตำแหน่งของเส้นตัด 2

cut_result = cut_polygon(polygon_points, cut_line_start, cut_line_end)
print("Cut Polygon Result:", cut_result)
