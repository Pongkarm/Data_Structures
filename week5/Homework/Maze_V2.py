#Maze
#6710301007
#6710301009

import os
import time
import keyboard
from Stack import Stack

class maze:
    def __init__(self) -> None:
        # self.maze = [
        #             ["X", "X", "X", "X", "X", "X", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", " "],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", "X"],
        #             ["X", " ", "X", "X", "X", "X", "X"],
        #             ]
        # self.ply = pos(5, 1)
        # self.end = pos(2, 6)
        # self.end = pos(5, 1)
        # self.ply = pos(2, 6)
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
        # self.end = pos(10, 1)
        # self.ply = pos(5, 6)
        # self.maze = [
        #             ["X", "X", "X", "X", "X", "X", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", " ", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", "X", "X", "X", "X", "X", "X"],
        #             ]
        # self.ply = pos(10, 1)
        # self.end = pos(0, 7)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    #เช็คว่าอยู่ในบอร์ดอยู่หรือเปล่า
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<=len(self.maze) and x<=len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
            if self.maze[next_move.y][next_move.x] != "X":
                self.maze[self.ply.y][self.ply.x] = "i"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
            if self.maze[next_move.y][next_move.x] != "X":
                self.maze[self.ply.y][self.ply.x] = "i"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x): #ถ้าเป็นจริง
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
            if self.maze[next_move.y][next_move.x] != "X": #ถ้าช่องต่อไปว่าง
                self.maze[self.ply.y][self.ply.x] = "i" #แทนที่ก่อนหน้าเป็นช่องว่าง
                self.maze[next_move.y][next_move.x] = "P" #แทนที่ต่อไปด้วย P
                self.ply = next_move #เซตค่าปัจจุบันเป็นข้างหน้า
                time.sleep(0.25)
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
            if self.maze[next_move.y][next_move.x] != "X":
                self.maze[self.ply.y][self.ply.x] = "i"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
        return True

    def lookway(self,stack):
        #up
        if self.maze[self.ply.y-1][self.ply.x] != "X" and self.maze[self.ply.y-1][self.ply.x] != 'o' and self.maze[self.ply.y-1][self.ply.x] != 'i':
            way = 1
        #left
        elif self.maze[self.ply.y][self.ply.x-1] != "X" and self.maze[self.ply.y][self.ply.x-1] != 'o'and self.maze[self.ply.y][self.ply.x-1] != 'i':
            way = 2
        #right
        elif self.maze[self.ply.y][self.ply.x+1] != "X" and self.maze[self.ply.y][self.ply.x+1] != 'o' and self.maze[self.ply.y][self.ply.x+1] != 'i':
            way = 3
        #down
        elif self.maze[self.ply.y+1][self.ply.x] != "X" and self.maze[self.ply.y+1][self.ply.x] != 'o' and self.maze[self.ply.y+1][self.ply.x] != 'i':
            way = 4    
        else:
            way = 5                 
        return stack, way
    def go_to_way(self,stack, way):
        if way == 1:
            self.move_up()
            stack.push('p')
        elif way == 2:
            self.move_left()
            stack.push('p')
        elif way == 3:
            self.move_right()
            stack.push('p')
        elif way == 4:
            self.move_down()
            stack.push('p')
        elif way == 5:
            #return way
            # stack.pop()
            if self.maze[self.ply.y-1][self.ply.x] == "i" or self.maze[self.ply.y-1][self.ply.x] == 'E':
                next_move = pos(self.ply.y-1, self.ply.x)
                self.maze[self.ply.y][self.ply.x] = "o"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
            elif self.maze[self.ply.y][self.ply.x-1] == "i" or self.maze[self.ply.y][self.ply.x-1] == 'E':
                next_move = pos(self.ply.y, self.ply.x-1)
                self.maze[self.ply.y][self.ply.x] = "o"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
            elif self.maze[self.ply.y][self.ply.x+1] == "i" or self.maze[self.ply.y][self.ply.x+1] == 'E' :
                next_move = pos(self.ply.y, self.ply.x+1)
                self.maze[self.ply.y][self.ply.x] = "o"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
            elif self.maze[self.ply.y+1][self.ply.x] == "i" or self.maze[self.ply.y+1][self.ply.x] == 'E':
                next_move = pos(self.ply.y+1, self.ply.x)
                self.maze[self.ply.y][self.ply.x] = "o"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move   
           
        return stack
class pos: 
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x


if __name__ == '__main__':

    pk = maze()
    stack = Stack()
    print('Press Enter to start')
    while True:
        if keyboard.is_pressed("enter"):
            pk.print()
            break

    stack.push('p')
    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        stack, way = pk.lookway(stack)
        stack = pk.go_to_way(stack, way)
        pk.print()
        time.sleep(0.1)

#No chat GPT !!!!!!!!!!!