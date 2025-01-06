import os
import time
import keyboard
from Stack import Stack


class maze:
    def __init__(self):
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "E"],
            ["X", "X", "X", "X", "X", "X", "X"],
        ]
        self.ply = pos(5, 1)  # เริ่มต้นที่ตำแหน่ง (5,1)
        self.end = pos(5, 6)  # ปลายทางที่ตำแหน่ง (5,6)
        self.maze[self.ply.y][self.ply.x] = "P"  # ตำแหน่งผู้เล่น
        self.maze[self.end.y][self.end.x] = "E"  # ตำแหน่งปลายทาง

    def isInBound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congratulation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move(self, dy, dx):
        next_move = pos(self.ply.y + dy, self.ply.x + dx)
        if self.isInBound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
        return True

    def lookway(self, stack):
        way = 0
        len_maze_x = len(self.maze[0])
        len_maze_y = len(self.maze)
        ply_x = self.ply.x
        ply_y = self.ply.y

        # ดึงตำแหน่งที่เคยผ่านมาแล้ว
        previous_pos = stack.peek() if not stack.isEmpty() else None

        # up
        if ply_y - 1 >= 0 and (self.maze[ply_y - 1][ply_x] == " " or self.maze[ply_y - 1][ply_x] == "E"):
            if not previous_pos or pos(ply_y - 1, ply_x) != previous_pos:
                way += 1
        # left
        if ply_x - 1 >= 0 and (self.maze[ply_y][ply_x - 1] == " " or self.maze[ply_y][ply_x - 1] == "E"):
            if not previous_pos or pos(ply_y, ply_x - 1) != previous_pos:
                way += 1
        # right
        if ply_x + 1 < len_maze_x and (self.maze[ply_y][ply_x + 1] == " " or self.maze[ply_y][ply_x + 1] == "E"):
            if not previous_pos or pos(ply_y, ply_x + 1) != previous_pos:
                way += 1
        # down
        if ply_y + 1 < len_maze_y and (self.maze[ply_y + 1][ply_x] == " " or self.maze[ply_y + 1][ply_x] == "E"):
            if not previous_pos or pos(ply_y + 1, ply_x) != previous_pos:
                way += 1

        return way

    def go_to_way(self, way, stack):
        # มี 1 ทางที่ไปได้
        if way == 1:
            self.move_one_way(stack)
        elif way >= 2:
            self.move_two_way(stack)
        elif way == 0:
            stack.pop()
        return stack

    def move_one_way(self, stack):
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # [up, left, right, down]
        for dy, dx in directions:
            next_move = pos(self.ply.y + dy, self.ply.x + dx)
            if self.isInBound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] != "X":
                stack.pop()
                stack.push(self.ply)
                self.move(dy, dx)
                break

    def move_two_way(self, stack):
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # [up, left, right, down]
        for dy, dx in directions:
            next_move = pos(self.ply.y + dy, self.ply.x + dx)
            if self.isInBound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] != "X":
                stack.push(self.ply)
                self.move(dy, dx)
                break


class pos:
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


if __name__ == "__main__":
    pk = maze()
    stack = Stack()
    print("Press Enter to start")
    while True:
        if keyboard.is_pressed("enter"):
            pk.print()
            break
    stack.push(pk.ply)
    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        way = pk.lookway(stack)
        stack = pk.go_to_way(way, stack)
        pk.print()
