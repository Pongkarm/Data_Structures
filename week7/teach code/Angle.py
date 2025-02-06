import math

def angle(a, b, c):
    """
    Calculates the angle (in radians) between vectors BA and BC.
    
    :param a: Tuple (x1, y1) - Point A
    :param b: Tuple (x2, y2) - Point B
    :param c: Tuple (x3, y3) - Point C
    :return: Angle in radians between the vectors BA and BC
    """
    # Vector BA
    ba_x = a[0] - b[0]
    ba_y = a[1] - b[1]
    
    # Vector BC
    bc_x = c[0] - b[0]
    bc_y = c[1] - b[1]
    
    # Dot product of BA and BC
    dot_product = (ba_x * bc_x) + (ba_y * bc_y)
    
    # Norms (lengths) of vectors BA and BC
    norm_ba = math.sqrt(ba_x**2 + ba_y**2) #ขนาด |b|
    norm_bc = math.sqrt(bc_x**2 + bc_y**2)
    
    # Avoid division by zero
    if norm_ba == 0 or norm_bc == 0:
        return 0.0
    
    # Calculate cosine of the angle
    cos_theta = dot_product / (norm_ba * norm_bc)
    
    # Clamp cos_theta to the range [-1, 1] to handle floating-point inaccuracies
    cos_theta = max(-1.0, min(1.0, cos_theta))
    
    # Calculate and return the angle in radians
    return math.acos(cos_theta)


# ฟังก์ชัน angle ใช้สำหรับคำนวณ มุมระหว่างเวกเตอร์สองเส้น ที่เชื่อมจุด a,b,c

a = [0, 5]
b = [2, 0]
c = [6, 3]

theta_radians = angle(a, b, c)
theta_degrees = math.degrees(theta_radians)

print(f"Angle (radians): {theta_radians}")
print(f"Angle (degrees): {theta_degrees}")


