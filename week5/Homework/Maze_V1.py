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
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x): #ถ้าเป็นจริง
            if self.maze[next_move.y][next_move.x] == " ": #ถ้าช่องต่อไปว่าง
                self.maze[self.ply.y][self.ply.x] = " " #แทนที่ก่อนหน้าเป็นช่องว่าง
                self.maze[next_move.y][next_move.x] = "P" #แทนที่ต่อไปด้วย P
                self.ply = next_move #เซตค่าปัจจุบันเป็นข้างหน้า
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def lookway(self,stack):
        if self.maze[pk.ply.y][self.ply.x-1] != "X" and stack.peek().x != pk.ply.x-1:
            stack.push(pk.ply)
            self.move_left()
        elif self.maze[self.ply.y-1][self.ply.x] != "X" and stack.peek().y != pk.ply.y-1 :
            stack.push(pk.ply)
            self.move_up()
        elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.peek().x != pk.ply.x+1 :
            stack.push(pk.ply)
            self.move_right()
        elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.peek().y != pk.ply.y+1 :
            stack.push(pk.ply)
            self.move_down()
        else:
            stack.pop()
            if self.maze[pk.ply.y][self.ply.x-1] != "X" and stack.peek().x != pk.ply.x-1:
                self.move_left()
                self.maze[pk.ply.y][self.ply.x+1] = "X"
            elif self.maze[self.ply.y-1][self.ply.x] != "X" and stack.peek().y != pk.ply.y-1 :
                self.move_up()
                self.maze[self.ply.y+1][self.ply.x] = "X"
            elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.peek().x != pk.ply.x+1 :
                self.move_right()
                self.maze[self.ply.y][self.ply.x-1] = "X"
            elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.peek().y != pk.ply.y+1 :
                self.move_down()
                self.maze[self.ply.y-1][self.ply.x] = "X"
        
        return stack
#class pos ผมขอแก้ใขให้ดูง่ายขคี้นกว่าเดิมนะครับ
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

    stack.push(pk.ply)
    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        stack = pk.lookway(stack)
        pk.print()
        time.sleep(0.1)

    # stack.push(pk.ply)
    
    # print(stack.peek().x)
    # print(stack.peek().y)
    # pk.move_up()
    # stack.push(pk.ply)
    # print(stack.peek().x)
    # print(stack.peek().y)
    # stack.pop()
    # print(stack.peek().x)
    # print(stack.peek().y)