import turtle
import time

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        """โหลดเขาวงกตจากไฟล์และกำหนดค่าเริ่มต้น"""
        self.maze_list = []
        self.visited = set()  # ใช้สำหรับเก็บตำแหน่งที่เคยเดิน
        maze_file = open(f'week9/homework/{maze_file_name}','r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            for ch in line.strip():
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = len(row_list) - 1
                if ch == 'E':
                    self.end_row = rows_in_maze
                    self.end_col = len(row_list) - 1
            self.maze_list.append(row_list)
            rows_in_maze += 1
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = max(len(row) for row in self.maze_list)
        self.t = turtle.Turtle()
        self.t.shape('turtle')
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
                if self.maze_list[y][x] == self.maze_list[self.end_row][self.end_col]:
                    self.draw_square(x, y, 'green')
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
        time.sleep(0.01)

    def update_position(self, row, col, val=None):
        """อัปเดตตำแหน่งของ Turtle และ mark จุดด้วยสีต่าง ๆ"""
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        if color:
            self.t.dot(10, color)

    def is_in_bounds(self, row, col):
        """ตรวจสอบว่า row และ col อยู่ในขอบเขตของเขาวงกตหรือไม่"""
        return 0 <= row < self.rows_in_maze and 0 <= col < len(self.maze_list[row])

    def is_walkable(self, row, col):
        """ตรวจสอบว่า row และ col เป็นตำแหน่งที่เดินได้หรือไม่"""
        return self.maze_list[row][col] != OBSTACLE

    def solve(self):
        """เริ่มต้นการค้นหาเส้นทางจากจุดเริ่มต้นไปยังจุดสิ้นสุด"""
        print(f"Starting position: {self.start_row}, {self.start_col}")
        print(f"Ending position: {self.end_row}, {self.end_col}")
        path = self.find_path(self.start_row, self.start_col)
        if path:
            for step in path:
                self.update_position(step[0], step[1], PART_OF_PATH)
            time.sleep(1.5)
            print("\n>>>>> Maze Solved <<<<<\n")
        else:
            print("No solution found.")

    def find_path(self, row, col):
        """ค้นหาเส้นทางจากตำแหน่งปัจจุบันไปยังทางออก"""
        if not self.is_in_bounds(row, col) or (row, col) in self.visited or not self.is_walkable(row, col):
            return None
        if (row, col) == (self.end_row, self.end_col):
            return [(row, col)]

        self.visited.add((row, col))
        self.update_position(row, col, TRIED)

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # ลองเดินในแต่ละทิศทาง
            path = self.find_path(row + dr, col + dc)
            if path:
                return [(row, col)] + path  # ถ้าเจอทางออกให้คืนเส้นทางกลับ

        self.update_position(row, col, DEAD_END)  # mark ว่าเป็นทางตัน
        return None
    
my_maze = Maze('maze1.txt')  # โหลดเขาวงกตจากไฟล์ maze1.txt
my_maze.draw_maze()  # วาดเขาวงกตด้วย Turtle
my_maze.solve()  # เริ่มต้นการหาทางออก

#ในแผนที่ต้องมีจุดเริ่มต้น S และจุดสิ้นสุด E ด้วยไม่งั้นจะ error
# ++++++++++++++++++++
# +S  +           +  +
# + + + +++   +++ +  +
# + +     +       +  +
# + ++++  + + +++++  +
# + +  +  + +     +  +
# + ++ +  + + +++ + E+
# +    +  +   + + +  +
# ++++ +++++++ + +++ +