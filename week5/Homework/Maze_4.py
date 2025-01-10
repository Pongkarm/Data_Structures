#Maze
#6710301007
#6710301009
# ออกเขาวงกตแบบไม่ทำสัญลักษณ์ (ส่งครู)
import os
import time
import keyboard
from Stack import Stack
from itertools import permutations
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
        #             ["X", " ", "X", " ", " ", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", "X", "X", " ", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", "X", "X", "X", "X"],
        #             ]
        # self.ply = pos(10, 1)
        # self.end = pos(5, 6)
        # self.end = pos(10, 3)
        # self.end = pos(10, 5)
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
        
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X"],
                    ["X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"],
                    ["X", "X", "X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X", " ", " "],
                    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", " ", "X", "X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(14, 1)
        self.end = pos(11, 12)
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
        #เช็คทาง ถ้าทางที่ไปไม่เป็น X และไม่เป็ทางที่พึ่งเดินมา
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
    def more_one_way(self, stack, htw):
        peek_y_back = stack.peek().y
        peek_x_back = stack.peek().x
        now_y = self.ply.y
        now_x = self.ply.x
        if htw == 25:
            htw = 99
            
        #คำสั่งวิเศษจะช่วยให้เราเปลี่ยนเส้นทางแบบทุกรูปแบบ 24 แบบ บน ซ้าย ขวา ล่าง, ล่าง ขวา ซ้าย บน...
        # choices = ['1', '2', '3', '4'] 
        choices = ['บน', 'ซ้าย', 'ขวา', 'ล่าง'] 
        permutations_result = list(permutations(choices, 4))
        #ในส่วนตรงนี้ไม่สามารถอธิบายด้วย comment ได้ถ้าดูเองไม่เข้าใจให้โทรมาถาม
        for idex, choidce in enumerate(permutations_result, start=1):
            if idex == htw:
                if choidce[0] == 'บน':
                    if not loopstack(stack, pos(self.ply.y-1, self.ply.x)):      
                        if (self.maze[self.ply.y-1][self.ply.x] == " " and self.ply.y-1 != peek_y_back) or self.maze[self.ply.y-1][self.ply.x] == 'E':
                            stack.push(self.ply)
                            self.move_up()
                if choidce[1] == 'ซ้าย':
                    if not loopstack(stack, pos(self.ply.y, self.ply.x-1)):
                        if (self.maze[self.ply.y][self.ply.x-1] == " " and self.ply.x-1 != peek_x_back) or self.maze[self.ply.y][self.ply.x-1] == 'E':
                            stack.push(self.ply)
                            self.move_left()
                if choidce[2] == 'ขวา':
                    if not loopstack(stack, pos(self.ply.y, self.ply.x+1)):
                        if (self.maze[self.ply.y][self.ply.x+1] == " " and self.ply.x+1 != peek_x_back) or self.maze[self.ply.y][self.ply.x+1] == 'E':
                            stack.push(self.ply)
                            self.move_right()
                if choidce[3] == 'ขวา':
                    if not loopstack(stack, pos(self.ply.y+1, self.ply.x)):
                        if (self.maze[self.ply.y+1][self.ply.x] == " " and self.ply.y+1 != peek_y_back) or self.maze[self.ply.y+1][self.ply.x] == 'E':
                            stack.push(self.ply)
                            self.move_down()

        # เมื่อเจอทางตัน(เราอยู่ที่เดิม)
        if now_y == self.ply.y and now_x == self.ply.x:
            #รีเซตstack
            stack = popstackuntil_0(stack)
            htw += 1
        return stack, htw
    def go_to_way(self, way, stack, htw):
        if way == 1:
            stack = self.one_way(stack)
        elif way >= 2:
            stack, htw = self.more_one_way(stack, htw)
        elif way == 0:
            stack.pop()
            stack.push(pos(0,0))

        return stack, htw
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

def loopstack(stack, pos):
    for pos_in_stack in checkStack(stack):
        #ถ้าตำแหน่งของเรามีอยู่ในstackที่เก็บไว้
        if pos.x == pos_in_stack.x and pos.y == pos_in_stack.y:
           return True
    return False
def popstackuntil_0(stack):
        try:
            while stack:
               stack.pop()
        except:
            return stack
        stack.push(pos(0,0)) 
        return stack
    
class pos: 
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
#ออกด้วยวิธีการทำสัญลักษณ์บนแผนที่
if __name__ == '__main__':
    pk = maze()
    stack = Stack() # Stackในครั้งนี้เราจะเก็บจุด x,y ของก่อนทางแยก และเก็บทางที่เราพึ่งจะเดินทางมา สองเงื่อนไขเท่านั้น
    print('Press Enter to start')
    htw = 1 #วิธีการมองและเดิน
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
        stack, htw = pk.go_to_way(way, stack, htw)
        if htw > 99:
            break
        pk.print()
        kong = checkStack(stack)
        #เช็คดูข้อมูลในstack
        # for i in kong:
        #     print(i.y ,i.x)
        #     print(htw)
        time.sleep(0.04)
    if htw > 99:
        print('แผนที่นี้ไม่มีทางออก')

#เวอร์ชั่นนี้แก้จาก maze3 
#maze3 มีบัคทีตัวเราไม่ย้อนกลับไปเวลาเจอทางตันทั้งหมด(ไม่ผ่านแยกที่เคยผ่านมาแล้ว)
#เวอร์ชั่นนี้จึงแก้โดยการเมื่อเจอทางตันทุกทางแล้วจะให้ลบข้อมูลทางที่มาหมดและเปลี่ยนวิธีการเดิน


#ก็โปรเจคนี้ใช้เวลาประมาณ 2 อาทิตเลยนะกว่าจะได้สมบูรณ์แบบนี้กว่าจะออกมาได้ซัดไป 4 version เลย
#รวมหัวสมองอันน้อยนิดระหว่าง programmer ดรัณภพ(6710301007) และ อภิสักก์ (6710301009)
#ถามว่ามีถามแชท GPT ไหม ก็มีนะแค่ 3 แบบคือ 
# ถามแนวคิดฟั่งก์ชั่น loopstack (line265)
# ถามการคิดทิศทาง4ทิศแบบไม่ซ้ำ(line209-213)
# ถามแนวคิดฟั่งก์ชั่น popstackuntil_0 (line270)
#ที่เหลือนอกจากนี้คิดเองหมดสดสด
#ก็ขออวยพรให้ทุกคนอ่านโค้ดพวกเราด้วยความสนุกและไม่งงนะบั๊ยบายย ^-^
#ปล.ใครไม่เชื่อว่าเขียนเองให้ไปถาม อภิสักก์ (6710301009)ได้เลย ถามโค้ดส่วนไหนก็ได้เขาจะอธิบายให้คุณฟังได้

#ก็น่าจะออกได้ทุกทางนะโค้ดนี้ จริงๆมี bug ในกรณีที่ไม่เจอทางออกเลย+ไม่เจอทางแยก อันนั้ก็จะติด bug inf loop ผมรู้แหละแต่ช่างมันเถอะคงไม่เจอหรอกใครจะไปสร้างด่านแบบนั้นวะ   และถ้าถามว่าทำไมตัวเรามันเดินไปเจอ E แล้วทำไมมันไม่เข้าเลย...เราก็รู้ครับแต่เราขี้เกียจแก้55 มันก็ออกได้เหมือนกันไหมล่ะรออีกหน่อยไม่ได้หรอ
#แมพที่บัค inf loop ไม่น่าได้เจอหรอก
        # self.maze = [
        #             ["X", " ", "X", " ", "X", "E", "X"],
        #             ["X", "X", "X", "X", "X", " ", "X"],
        #             ["X", " ", " ", " ", "X", " ", "X"],
        #             ["X", " ", "X", " ", "X", " ", "X"],
        #             ["X", " ", "X", "X", "X", "X", "X"],
        #             ]
        # self.ply = pos(4, 1)
        
#ถ้ามีบัคอะไรแจ้งได้นะครับ issues ไว้ได้เลย
# https://github.com/Pongkarm/Data_Structures/issues