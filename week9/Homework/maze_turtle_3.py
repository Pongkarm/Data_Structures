import turtle
import time  # ใช้สำหรับหน่วงเวลาในการเดิน

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        """โหลดเขาวงกตจากไฟล์และกำหนดค่าเริ่มต้น"""
        self.maze_list = []
        self.start_row = None
        self.start_col = None
        maze_file = open(f'week9/Homework/{maze_file_name}', 'r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line.strip():
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze  # บันทึกแถวที่เจอ 'S'
                    self.start_col = col  # บันทึกคอลัมน์ที่เจอ 'S'
                col += 1
            self.maze_list.append(row_list)
            rows_in_maze += 1

        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = max(len(row) for row in self.maze_list)
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.t.speed(1)
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-0.5, -self.rows_in_maze + 0.5, self.columns_in_maze - 0.5, 0.5)

    def draw_maze(self):
        """วาดเขาวงกตบนหน้าจอด้วย turtle"""
        self.t.speed(0)
        self.t.penup()
        for y in range(self.rows_in_maze):
            for x in range(len(self.maze_list[y])):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_square(x, y, 'orange')
        self.t.speed(0)

    def draw_square(self, x, y, color):
        """วาดกล่องสี่เหลี่ยมที่ตำแหน่ง (x, y) ด้วยสีที่กำหนด"""
        self.t.up()
        self.t.goto(x - 0.5, -y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        self.t.up()

    def move_turtle(self, x, y):
        """ย้าย Turtle ไปยังตำแหน่ง (x, y) ทีละก้าว"""
        self.t.setheading(self.t.towards(x, -y))
        self.t.goto(x, -y)
        time.sleep(0.1)

    def update_position(self, row, col, val=None):
        """อัปเดตตำแหน่งของ Turtle และ mark จุดด้วยสีต่าง ๆ"""
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'  # เส้นทางที่ถูกต้อง
        elif val == TRIED:
            color = 'black'  # จุดที่เคยลองแล้ว
        elif val == DEAD_END:
            color = 'red'  # จุดที่เป็นทางตัน
        else:
            color = None
        if color:
            self.t.dot(10, color)  # mark จุดด้วยจุดสีที่กำหนด

    def is_exit(self, row, col):
        """ตรวจสอบว่าตำแหน่งนี้คือทางออกหรือไม่"""
        return row == 0 or row == self.rows_in_maze - 1 or col == 0 or col == self.columns_in_maze - 1

    def __getitem__(self, idx):
        """คืนค่าแถวของเขาวงกต"""
        return self.maze_list[idx]

# def search_from(maze, row, col):
#     """ค้นหาเส้นทางออกจากเขาวงกตโดยใช้ DFS (ทีละก้าว)"""
#     if maze[row][col] == OBSTACLE or maze[row][col] == TRIED or maze[row][col] == DEAD_END:
#         return False
#     maze.update_position(row, col, TRIED)

#     if maze.is_exit(row, col):
#         maze.update_position(row, col, PART_OF_PATH)
#         return True

#     found = (search_from(maze, row-1, col) or  # เหนือ
#              search_from(maze, row+1, col) or  # ใต้
#              search_from(maze, row, col-1) or  # ซ้าย
#              search_from(maze, row, col+1))    # ขวา

#     if found:
#         maze.update_position(row, col, PART_OF_PATH)
#         return True
#     else:
#         maze.update_position(row, col, DEAD_END)
#         return False

def in_bounds(maze, row, col):
    """ตรวจสอบว่า row และ col อยู่ในขอบเขตของเขาวงกตหรือไม่"""
    return 0 <= row < maze.rows_in_maze and 0 <= col < len(maze[row])

def search_from(maze, row, col):
    """ค้นหาเส้นทางออกจากเขาวงกตโดยใช้ DFS (ทีละก้าว)"""
    if not in_bounds(maze, row, col):  # ตรวจสอบขอบเขตก่อน
        return False
    if maze[row][col] == OBSTACLE or maze[row][col] == TRIED or maze[row][col] == DEAD_END:
        return False

    maze.update_position(row, col, TRIED)  # ให้ Turtle เดินไปยังตำแหน่งนี้และ mark จุดนี้ว่าเคยเดินแล้ว

    if maze.is_exit(row, col):  # ตรวจสอบว่าเจอทางออกหรือไม่
        maze.update_position(row, col, PART_OF_PATH)
        print("Found the exit!")
        return True

    # ลองเดินไปในแต่ละทิศทาง: เหนือ, ใต้, ซ้าย, ขวา
    found = (search_from(maze, row-1, col) or  # เหนือ
             search_from(maze, row+1, col) or  # ใต้
             search_from(maze, row, col-1) or  # ซ้าย
             search_from(maze, row, col+1))    # ขวา

    if found:
        maze.update_position(row, col, PART_OF_PATH)
        return True
    else:
        maze.update_position(row, col, DEAD_END)
        print(f"Dead end at: ({row}, {col})")
        return False


# เริ่มต้นโปรแกรม
my_maze = Maze('maze_1.txt')
my_maze.draw_maze()
search_from(my_maze, my_maze.start_row, my_maze.start_col)
print('out')
