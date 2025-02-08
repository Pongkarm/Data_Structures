from collections import deque
import turtle  # นำเข้าโมดูล turtle สำหรับการแสดงผลกราฟิก

# กำหนดค่าต่าง ๆ สำหรับการแสดงสถานะของตำแหน่งในเขาวงกต
PART_OF_PATH = 'O'  # ส่วนของเส้นทางที่ถูกต้อง
TRIED = '.'         # ตำแหน่งที่ลองเดินแล้ว
OBSTACLE = '+'      # สิ่งกีดขวาง
DEAD_END = '-'      # เส้นทางตัน

class Maze:
    def __init__(self, maze_file_name):
        """โหลดเขาวงกตจากไฟล์และกำหนดค่าเริ่มต้น"""
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []  # รายการสำหรับเก็บข้อมูลเขาวงกต
        maze_file = open(f'week9/homework/{maze_file_name}', 'r')  # เปิดไฟล์เขาวงกตจากเส้นทางที่กำหนด
        rows_in_maze = 0
        for line in maze_file:
            row_list = []  # สร้างรายการใหม่สำหรับแต่ละแถว
            col = 0
            for ch in line[:-1]:  # อ่านแต่ละตัวอักษร ยกเว้นตัวสุดท้าย (\n)
                row_list.append(ch)  # เพิ่มตัวอักษรในรายการของแถว
                if ch == 'S':  # ถ้าเจอจุดเริ่มต้น
                    self.start_row = rows_in_maze  # บันทึกแถวของจุดเริ่มต้น
                    self.start_col = col  # บันทึกคอลัมน์ของจุดเริ่มต้น
                col = col + 1
            rows_in_maze = rows_in_maze + 1  # นับจำนวนแถว
            self.maze_list.append(row_list)  # เพิ่มแถวในรายการเขาวงกต
            columns_in_maze = len(row_list)  # บันทึกจำนวนคอลัมน์
        self.rows_in_maze = rows_in_maze  # เก็บจำนวนแถวทั้งหมด
        self.columns_in_maze = columns_in_maze  # เก็บจำนวนคอลัมน์ทั้งหมด
        self.x_translate = -columns_in_maze / 2  # คำนวณการแปลงค่าแกน X
        self.y_translate = rows_in_maze / 2  # คำนวณการแปลงค่าแกน Y
        self.t = turtle.Turtle()  # สร้างวัตถุ turtle สำหรับการวาด
        self.t.shape('turtle')  # กำหนดรูปร่างของ turtle เป็นรูปเต่า
        self.wn = turtle.Screen()  # สร้างหน้าจอสำหรับการแสดงผล
        self.wn.setworldcoordinates(- (columns_in_maze - 1) / 2 - .5,
                                    - (rows_in_maze - 1) / 2 - .5,
                                    (columns_in_maze - 1) / 2 + .5,
                                    (rows_in_maze - 1) / 2 + .5)  # ตั้งค่าขอบเขตของหน้าจอ

    def draw_maze(self):
        """วาดเขาวงกตบนหน้าจอด้วย turtle"""
        self.t.speed(0)  # ตั้งความเร็วในการวาดเป็นระดับสูงสุด
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:  # ถ้าเป็นสิ่งกีดขวาง
                    self.draw_centered_box(x + self.x_translate,
                                           -y + self.y_translate, 'red')  # วาดกล่องสี่เหลี่ยมสีส้ม
        self.t.color('black')  # ตั้งสีปากกาเป็นสีดำ
        self.t.fillcolor('blue')  # ตั้งสีเติมเป็นสีน้ำเงิน

    def draw_centered_box(self, x, y, color):
        """วาดกล่องสี่เหลี่ยมที่ตำแหน่ง (x, y)"""
        self.t.up()
        self.t.goto(x - .5, y - .5)  # ย้าย turtle ไปยังมุมซ้ายล่างของกล่อง
        self.t.color(color)  # ตั้งสีของเส้นเป็นสีที่กำหนด
        self.t.fillcolor(color)  # ตั้งสีเติมเป็นสีที่กำหนด
        self.t.setheading(90)  # ตั้ง turtle ให้หันขึ้นด้านบน
        self.t.down()
        self.t.begin_fill()  # เริ่มเติมสี
        for i in range(4):
            self.t.forward(1)  # เดินไปข้างหน้า 1 หน่วย
            self.t.right(90)  # หมุนขวา 90 องศา
        self.t.end_fill()  # สิ้นสุดการเติมสี

    def move_turtle(self, x, y):
        """เลื่อน turtle ไปยังตำแหน่ง (x, y)"""
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))  # ตั้งทิศทาง
        self.t.goto(x + self.x_translate, -y + self.y_translate)  # ย้ายไปยังตำแหน่งเป้าหมาย

    def drop_bread_crumb(self, color):
        """วางจุดที่ตำแหน่งปัจจุบันด้วยสีที่กำหนด"""
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        """อัปเดตตำแหน่งของ turtle และสถานะในเขาวงกต"""
        if val:
            self.maze_list[row][col] = val  # เปลี่ยนสถานะของช่องในเขาวงกต
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'  # เส้นทางที่ถูกต้องเป็นสีเขียว
        elif val == OBSTACLE:
            color = 'red'  # สิ่งกีดขวางเป็นสีแดง
        elif val == TRIED:
            color = 'black'  # ช่องที่ลองแล้วเป็นสีดำ
        elif val == DEAD_END:
            color = 'red'  # เส้นทางตันเป็นสีแดง
        else:
            color = None
        if color:
            self.drop_bread_crumb(color)  # วาง breadcrumb ด้วยสีที่กำหนด

    def is_exit(self, row, col):
        """ตรวจสอบว่าตำแหน่งปัจจุบันคือทางออกหรือไม่"""
        return (row == 0 or row == self.rows_in_maze - 1 or col == 0 or col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        """คืนค่าแถวของเขาวงกต"""
        return self.maze_list[idx]

def search_from(maze, start_row, start_column):
    """ค้นหาเส้นทางออกจากเขาวงกตโดยใช้การเรียกซ้ำ (Recursion)"""
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False  # เจอสิ่งกีดขวาง
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END:
        return False  # เจอช่องที่เคยลองแล้ว
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True  # เจอทางออก
    maze.update_position(start_row, start_column, TRIED)
    found = (search_from(maze, start_row-1, start_column) or  # เหนือ
             search_from(maze, start_row+1, start_column) or  # ใต้
             search_from(maze, start_row, start_column-1) or  # ซ้าย
             search_from(maze, start_row, start_column+1))    # ขวา
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found

def bfs_shortest_path(maze, start_row, start_col):
    """ค้นหาเส้นทางที่สั้นที่สุดโดยใช้ Breadth-First Search (BFS)"""
    queue = deque([(start_row, start_col, [])])  # เก็บ (row, col, เส้นทางที่เดินผ่านมา)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # ทิศทาง: เหนือ, ใต้, ซ้าย, ขวา
    
    while queue:
        row, col, path = queue.popleft()  # ดึงตำแหน่งปัจจุบันและเส้นทางที่เดินผ่านมา
        if maze[row][col] == OBSTACLE or maze[row][col] == TRIED:
            continue  # ข้ามสิ่งกีดขวางหรือจุดที่เคยเดินมาแล้ว
        
        maze.update_position(row, col, TRIED)  # ทำเครื่องหมายตำแหน่งนี้ว่าเคยเดินแล้ว
        
        if maze.is_exit(row, col):  # ถ้าเจอทางออก
            for r, c in path + [(row, col)]:
                maze.update_position(r, c, PART_OF_PATH)  # ทำเครื่องหมายเส้นทางที่สั้นที่สุด
            return True
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < maze.rows_in_maze and 0 <= new_col < maze.columns_in_maze:
                queue.append((new_row, new_col, path + [(row, col)]))  # เพิ่มตำแหน่งใหม่พร้อมเส้นทางที่เดินผ่านมา
    
    return False  # ถ้าไม่เจอทางออก

# เริ่มต้นโปรแกรม
my_maze = Maze('maze_1.txt')  # โหลดไฟล์ maze1.txt
my_maze.draw_maze()  # วาดเขาวงกต
my_maze.update_position(my_maze.start_row, my_maze.start_col)  # อัปเดตตำแหน่งเริ่มต้น
# search_from(my_maze, my_maze.start_row, my_maze.start_col)  # ค้นหาเส้นทางออกจากเขาวงกต
bfs_shortest_path(my_maze, my_maze.start_row, my_maze.start_col)  # ค้นหาเส้นทางที่สั้นที่สุด
print('out')  # แสดงข้อความเมื่อหาทางออกสำเร็จ
