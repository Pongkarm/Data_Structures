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
        # # self.ply = pos(2, 6)
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
        # self.maze = [
        #             ["X", "X", "X", "X", "X", "X", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", "X", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", " ", " ", "X"],
        #             ["X", " ", " ", " ", " ", " ", "X", " ", "X"],
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
                self.maze[self.ply.y][self.ply.x] = " "
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
                self.maze[self.ply.y][self.ply.x] = " "
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
                self.maze[self.ply.y][self.ply.x] = " " #แทนที่ก่อนหน้าเป็นช่องว่าง
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
        #up
        if ply_y-1 >= 0:  #ต้องไม่ให้น้อบกว่า 0
            if (self.maze[self.ply.y-1][self.ply.x] == " " and self.ply.y-1 != stack.peek().y) or self.maze[self.ply.y-1][self.ply.x] == "E":
                way += 1        
        #left
        if ply_x-1 >= 0 :
            if (self.maze[self.ply.y][self.ply.x-1] == " " and self.ply.x-1 != stack.peek().x) or self.maze[self.ply.y][self.ply.x-1] == "E":
                way += 1 
        #right
        if ply_x < len_maze_x-1: #ตรวจว่าแถวมีพอที่จะ +1 y หรือเปล่า ป้องกันerror จากการเลย // -1 len เพราะเอาตำแหน่งเอาเทียบกับจำนวน ซึ่งมันนับไม่เหมือนกัน หาตำแหน่งเริ่มจาก 0 แต่นับจำนวนนับจาก 1 เลยต้อง -1 ให้พอดีกัน
            if (self.maze[self.ply.y][self.ply.x+1] == " " and self.ply.x+1 != stack.peek().x) or self.maze[self.ply.y][self.ply.x+1] == "E":
                way += 1 
        #down
        if ply_y < len_maze_y-1: 
            if (self.maze[self.ply.y+1][self.ply.x] == " " and self.ply.y+1 != stack.peek().y) or self.maze[self.ply.y+1][self.ply.x] == "E":
                way += 1

                           
        return way
    def one_way(self, stack):
        #up
        if self.maze[self.ply.y-1][self.ply.x] != "X" and self.ply.y-1 != stack.peek().y:
            stack.pop()
            stack.push(self.ply)
            self.move_up()
            
        #left
        elif self.maze[self.ply.y][self.ply.x-1] != "X" and self.ply.x-1 != stack.peek().x:
            stack.pop()
            stack.push(self.ply)
            self.move_left() 
        #right
        elif self.maze[self.ply.y][self.ply.x+1] != "X" and self.ply.x+1 != stack.peek().x:
            stack.pop()
            stack.push(self.ply)
            self.move_right()
        #down
        elif self.maze[self.ply.y+1][self.ply.x] != "X" and self.ply.y+1 != stack.peek().y:
            stack.pop()
            stack.push(self.ply)
            self.move_down() 

            
        return stack
    def two_way(self, stack):
        peek_y_back = stack.peek().y
        peek_x_back = stack.peek().x
        kong = checkStack(stack)
        #up
        if self.maze[self.ply.y-1][self.ply.x] != "X" and (i.y != self.ply.y-1 for i in kong) and self.ply.y-1 != peek_y_back:
            stack.push(self.ply)
            self.move_up()
        #left
        elif self.maze[self.ply.y][self.ply.x-1] != "X" and (i.x != self.ply.x-1 for i in kong) and self.ply.x-1 != peek_x_back:
            stack.push(self.ply)
            self.move_left() 
        #right
        elif self.maze[self.ply.y][self.ply.x+1] != "X" and (i.x != self.ply.x+1 for i in kong) and self.ply.x+1 != peek_x_back:
            stack.push(self.ply)
            self.move_right()
        #down
        elif self.maze[self.ply.y+1][self.ply.x] != "X" and (i.y != self.ply.y+1 for i in kong) and self.ply.y+1 != peek_y_back:
            stack.push(self.ply)
            self.move_down() 
        return stack
    def go_to_way(self, way, stack):
        #มี 1 ทางที่ไปได้
        if way == 1:
            stack = self.one_way(stack)
        elif way >= 2:
            stack = self.two_way(stack)
        elif way == 0:
            stack.pop()
            # stack.push(pos(0,0))
        return stack
def checkStack(stack):
    temp_stack = Stack()
    kong = []
    # อ่านข้อมูลใน stack โดยไม่ทำให้ข้อมูลหาย
    while not stack.isEmpty():
        top = stack.peek()  # อ่านค่าด้านบนสุด
        kong.append(top)
        temp_stack.push(stack.pop())  # เก็บข้อมูลชั่วคราว

    # คืนค่าข้อมูลกลับไปยัง stack เดิม
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
    return kong
class pos: 
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x

#ออกด้วยวิธีการทำสัญลักษณ์บนแผนที่
if __name__ == '__main__':

    pk = maze()
    stack = Stack()
    print('Press Enter to start')
    while True:
        if keyboard.is_pressed("enter"):
            pk.print()
            break
    stack.push(pos(0, 0))
    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        way = pk.lookway(stack)
        stack = pk.go_to_way(way, stack)
        pk.print()
        time.sleep(0.04)

#Bug fixes looking first way
#bug ถ้าเจอทางแยกมากกว่า 3ทางแก็ไม่ได้
#bug ทางวนซ้ายออกไม่ได้
#bug ทางตันระยะไกล้ (<1ช่อง)

