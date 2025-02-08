import turtle

t = turtle.Turtle()
# ตั้งค่าความเร็วในการวาด (1 ช้า - 10 เร็ว, 0 คือเร็วสุด)
t.speed(5)
# วาดสี่เหลี่ยมจัตุรัส
for _ in range(4):  # ทำซ้ำ 4 รอบ
    t.forward(100)  # เดินหน้าตรงไป 100 หน่วย
    t.right(90)  

turtle.done()

