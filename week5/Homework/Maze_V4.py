import os
import time
import keyboard
from Stack import Stack


class maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", "X", "X", " ", "X", " ", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = pos(10, 1)
        self.end = pos(5, 6)
        # self.ply = pos(5, 1)  # ตำแหน่งเริ่มต้น (5,1)
        # self.end = pos(5, 6)  # ตำแหน่งปลายทาง (5,6)
        self.visited = set()  # เก็บตำแหน่งที่เคยเดินผ่านแล้ว

    def isInBound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print(self):
        os.system("cls" if os.name == "nt" else "clear")
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                if self.ply.y == y and self.ply.x == x:
                    print("P", end=" ")  # แสดงตำแหน่งผู้เล่น
                elif self.end.y == y and self.end.x == x:
                    print("E", end=" ")  # แสดงตำแหน่งปลายทาง
                else:
                    print(col, end=" ")
            print()
        print("\n")

    def printEND(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n>>>>> Congratulations!!! <<<<<\n\n")
        keyboard.wait("")

    def move(self, dy, dx):
        next_move = pos(self.ply.y + dy, self.ply.x + dx)
        if self.isInBound(next_move.y, next_move.x):
            if next_move.y == self.end.y and next_move.x == self.end.x:
                self.printEND()
                return False
            if (next_move.y, next_move.x) not in self.visited and self.maze[next_move.y][next_move.x] == " ":
                self.ply = next_move
                self.visited.add((self.ply.y, self.ply.x))
                time.sleep(0.1)
        return True

    def lookway(self):
        way = 0
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for dy, dx in directions:
            next_move = pos(self.ply.y + dy, self.ply.x + dx)
            if self.isInBound(next_move.y, next_move.x) and \
               (next_move.y, next_move.x) not in self.visited and \
               self.maze[next_move.y][next_move.x] in [" ", "E"]:
                way += 1
        return way

    def go_to_way(self, way, stack):
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        if way >= 1:
            for dy, dx in directions:
                next_move = pos(self.ply.y + dy, self.ply.x + dx)
                if self.isInBound(next_move.y, next_move.x) and \
                   (next_move.y, next_move.x) not in self.visited and \
                   self.maze[next_move.y][next_move.x] in [" ", "E"]:
                    stack.push(self.ply)
                    self.move(dy, dx)
                    break
        elif way == 0:
            if not stack.isEmpty():
                self.ply = stack.pop()
        return stack


class pos:
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


if __name__ == "__main__":
    pk = maze()
    stack = Stack()
    pk.visited.add((pk.ply.y, pk.ply.x))  # เพิ่มตำแหน่งเริ่มต้นใน visited
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
        way = pk.lookway()
        stack = pk.go_to_way(way, stack)
        pk.print()