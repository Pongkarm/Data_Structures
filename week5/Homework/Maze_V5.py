#Maze
#6710301007
#6710301009
# ออกเขาวงกตแบบไม่ทำสัญลักษณ์ (ส่งครู)
import os
import time
import keyboard
from Stack import Stack
import timeit

start_time = timeit.default_timer()
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
        
        # self.maze = [
        #             ["X", "X", "X", "X", "X", "X", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", " "],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", "X", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", "X", "X", "X", "X"],
                    # ]
        # self.ply = pos(10, 1)
        # self.end = pos(5, 6)
        # self.ply = pos(5, 6)
        # self.end = pos(10, 1)
        
        # self.maze = [
        #             ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", " ", " ", " ", " ", "X"],
        #             ["X", " ", "X", "X", "X", "X", "X", "X", "X"],
        #             ]
        # self.ply = pos(10, 1)
        # self.end = pos(0, 7)
        # self.ply = pos(0, 7)
        # self.end = pos(10, 1)
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X", " ", "X", "X", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X", " ", "X"],
                    ["X", "X", "X", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", " ", "X", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(14, 1)
        self.end = pos(0, 3)
        # self.ply = pos(0, 3)
        # self.end = pos(14, 1)
        
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
        print("\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")
    def printNOEND(self):
        print("\n\n\n")
        print(">>>>> There is no way out <<<<<")
        print("\n\n\n")
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
                time.sleep(0.025)
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
                time.sleep(0.025)
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
                time.sleep(0.025)
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
                time.sleep(0.025)
        return True
    
    def lookway(self, stack_i, stack_O):
        way = 0
        len_maze_x = len(self.maze[0])
        len_maze_y = len(self.maze)
        ply_x = self.ply.x
        ply_y = self.ply.y
        #up
        if ply_y-1 >= 0:  #ต้องไม่ให้น้อบกว่า 0
            if self.maze[self.ply.y-1][self.ply.x] == "E":
                way = 1
                return way
            if is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
                if self.maze[self.ply.y-1][self.ply.x] == " ":
                    way += 1   
        #left
        if ply_x-1 >= 0 :
            if self.maze[self.ply.y][self.ply.x-1] == "E":
                way = 1
                return way
            if is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
                if self.maze[self.ply.y][self.ply.x-1] == " ":
                    way += 1 
                
        #right
        if ply_x < len_maze_x-1: 
            if self.maze[self.ply.y][self.ply.x+1] == "E":
                way = 1
                return way
            if is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
                if self.maze[self.ply.y][self.ply.x+1] == " ":
                    way += 1 
        #down
        if ply_y < len_maze_y-1: 
            if self.maze[self.ply.y+1][self.ply.x] == "E":
                way = 1
                return way
            if is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and  is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
                if self.maze[self.ply.y+1][self.ply.x] == " " :
                    way += 1  
        return way
    
    def go_to_way(self, way, stack_i, stack_O):
        if way == 1:
            stack_i, stack_O = self.one_way(stack_i, stack_O)
            
        elif way >= 2:
            stack_i, stack_O = self.more_one_way(stack_i, stack_O)
            
        elif way == 0:
            i = 0
            if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
                i += 1
            if not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
                i += 1
            if not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
                i += 1
            if not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
                i += 1
                
            if i > 1:
                if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)) and stack_i.peek().y == self.ply.y-1:
                    stack_O.push(self.ply)
                    stack_i.push(self.ply)
                    self.move_up()
                elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)) and stack_i.peek().x == self.ply.x-1:
                    stack_O.push(self.ply)
                    stack_i.push(self.ply)
                    self.move_left()
                elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)) and stack_i.peek().x == self.ply.x+1:
                    stack_O.push(self.ply)
                    stack_i.push(self.ply)
                    self.move_right()
                elif not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)) and stack_i.peek().y == self.ply.y+1:
                    stack_O.push(self.ply)
                    stack_i.push(self.ply)
                    self.move_down()
                
            elif i <= 1:
                
                if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
                    stack_O.push(self.ply)
                    self.move_up()
                elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
                    stack_O.push(self.ply)
                    self.move_left()
                elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
                    stack_O.push(self.ply)
                    self.move_right()
                elif not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
                    stack_O.push(self.ply)
                    self.move_down()
                else:
                    print("No path")
                    self.printNOEND()
                    stack_i.push(pos(100, 100))
                    stack_O.push(pos(100, 100))
                    return stack_i, stack_O
                
        return stack_i, stack_O
    def one_way(self, stack_i, stack_O):
        len_maze_x = len(self.maze[0])
        len_maze_y = len(self.maze)
        #เช็คทางถ้าทางที่ไปเป็น E ให้เข้า E เลย
        if self.ply.y-1 >= 0:
            if self.maze[self.ply.y-1][self.ply.x] == "E":
                self.move_up()
        if self.ply.x-1 >= 0:
            if self.maze[self.ply.y][self.ply.x-1] == "E":
                self.move_left()
        if self.ply.x < len_maze_x-1:    
            if self.maze[self.ply.y][self.ply.x+1] == "E":
                self.move_right()
        if self.ply.y < len_maze_y-1:
            if self.maze[self.ply.y+1][self.ply.x] == "E":
                self.move_down()
        #หาทางว่างก่อนเป็นอันดับที่สอง และเป็นทางที่ไม่เคยไปมาก่อน
        if self.maze[self.ply.y-1][self.ply.x] == " " and is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
            stack_i.push(self.ply)
            self.move_up()
        elif self.maze[self.ply.y][self.ply.x-1] == " " and is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
            stack_i.push(self.ply)
            self.move_left()
        elif self.maze[self.ply.y][self.ply.x+1] == " " and is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
            stack_i.push(self.ply)
            self.move_right()
        elif self.maze[self.ply.y+1][self.ply.x] == " " and is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
            stack_i.push(self.ply)
            self.move_down()
        else:
            print('มาได้ไง')
                
        return stack_i, stack_O
    def more_one_way(self, stack_i, stack_O):
        len_maze_x = len(self.maze[0])
        len_maze_y = len(self.maze)
        
        #เช็คทางถ้าทางที่ไปเป็น E ให้เข้า E เลย
        if self.ply.y-1 >= 0:
            if self.maze[self.ply.y-1][self.ply.x] == "E":
                self.move_up()
        if self.ply.x-1 >= 0:
            if self.maze[self.ply.y][self.ply.x-1] == "E":
                self.move_left()
        if self.ply.x < len_maze_x-1:    
            if self.maze[self.ply.y][self.ply.x+1] == "E":
                self.move_right()
        if self.ply.y < len_maze_y-1:
            if self.maze[self.ply.y+1][self.ply.x] == "E":
                self.move_down()
        #หาทางว่างก่อนเป็นอันดับที่สอง และเป็นทางที่ไม่เคยไปมาก่อน
        if self.maze[self.ply.y-1][self.ply.x] == " " and  is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and  is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
            stack_i.push(self.ply)
            self.move_up()
        elif self.maze[self.ply.y][self.ply.x-1] == " " and is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply, self.ply.x-1)):
            stack_i.push(self.ply)
            self.move_left()
        elif self.maze[self.ply.y][self.ply.x+1] == " " and is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply, self.ply.x+1)):
            stack_i.push(self.ply)
            self.move_right()
        elif self.maze[self.ply.y+1][self.ply.x] == " " and is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
            stack_i.push(self.ply)
            self.move_down()
        else:
            print('มาได้ไง')

        return stack_i, stack_O
    

class pos: 
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
        
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

def is_in_loopstack(stack, pos):
    for pos_in_stack in checkStack(stack):
        #ถ้าตำแหน่งของเรามีอยู่ในstackที่เก็บไว้
        if pos.x == pos_in_stack.x and pos.y == pos_in_stack.y:
           return False
    return True

#ออกด้วยวิธีการทำสัญลักษณ์บนแผนที่
if __name__ == '__main__':
    pk = maze()
    stack_i = Stack() # Stackในครั้งนี้เราจะเก็บจุด x,y ของก่อนทางแยก และเก็บทางที่เราพึ่งจะเดินทางมา ของ i (ทางที่เคยเดิน)
    stack_O = Stack() # Stackในครั้งนี้เราจะเก็บจุด x,y ของก่อนทางแยก และเก็บทางที่เราพึ่งจะเดินทางมา ของ O (ทางที่ตัน)
    print('Press Enter to start')    
    while True:
        if keyboard.is_pressed("enter"):
            pk.print()
            break
    stack_i.push(pos(99, 99)) #เป็นสารตั้งต้นเอาไว้ก่อน
    stack_O.push(pos(99, 99))
    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        way = pk.lookway(stack_i, stack_O)
        print(way)
        stack_i, stack_O = pk.go_to_way(way, stack_i, stack_O)
        if stack_i.peek().x == 100 and stack_O.peek().x == 100:
            break
        pk.print()
        time.sleep(.05)

elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")

#อันนี้จะเป็น version สุดท้ายที่จะทำละต้องแก้ได้ทุกแมพแน่นอน

#ก็โปรเจคนี้ใช้เวลาประมาณ 2 อาทิตเลยนะกว่าจะได้สมบูรณ์แบบนี้กว่าจะออกมาได้ซัดไป 5 version เลย
#รวมหัวสมองอันน้อยนิดระหว่าง programmer ดรัณภพ(6710301007) และ อภิสักก์ (6710301009)
#ถามว่ามีถามแชท GPT ไหม ก็มีนะแค่ 2 แบบคือ 
# ถามแนวคิดฟั่งก์ชั่น loopstack (line 374)
# def checkStack (line 333)
#ที่เหลือนอกจากนี้คิดเองหมดสดสด ถ้าเป็นไปได้เราก็ไม่อยากใช้แชทไง
#ก็ขออวยพรให้ทุกคนอ่านโค้ดพวกเราด้วยความสนุกและไม่งงนะบั๊ยบายย ^-^
#ปล.ใครไม่เชื่อว่าเขียนเองให้ไปถาม อภิสักก์ (6710301009)ได้เลย ถามโค้ดส่วนไหนก็ได้เขาจะอธิบายให้คุณฟังได้

#ถ้ามีบัคอะไรแจ้งได้นะครับ issues ไว้ได้เลย
# https://github.com/Pongkarm/Data_Structures/issues
