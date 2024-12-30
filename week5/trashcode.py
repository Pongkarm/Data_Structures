    # def lookway(self):
    #     if self.maze[self.ply.y-1][self.ply.x] == " ":
    #         self.move_up()
    #     elif self.maze[self.ply.y+1][self.ply.x] == " ":
    #         self.move_down() 
    #     elif self.maze[self.ply.y][self.ply.x-1] == " ":
    #         self.move_left()
    #     elif self.maze[self.ply.y][self.ply.x+1] == " ":
            # self.move_right()
            
# old = self.maze[self.ply.y][self.ply.x]
#             self.move_up()
#             if self.maze[self.ply.y+1][self.ply.x] == old:
#                 stack.push('p')
#             self.move_down()
#             if self.maze[self.ply.y-1][self.ply.x] == old:
#                 stack.push('p')
#             self.move_left()
#             if self.maze[self.ply.y][self.ply.x+1] == old:
#                 stack.push('p')
#             self.move_right()
#             if self.maze[self.ply.y][self.ply.x-1] == old:
#                 stack.push('p')
#             return stack
            
            # if self.maze[self.ply.y-1][self.ply.x] != "X" and stack.pop() != 'p':
            #     self.move_up()
            #     stack.push('p')
            # elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.pop() != 'p':
            #     self.move_down()
            #     stack.push('p')
            # elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.pop() != 'p':
            #     self.move_right()
            #     stack.push('p')
            # elif self.maze[self.ply.y][self.ply.x-1] != "X" and stack.pop() != 'p':
            #     self.move_left()
            #     stack.push('p')
            # return stack


    # stack.push(pk.ply)
    # def lookway(self,stack):
    #     if self.maze[self.ply.y-1][self.ply.x] != "X" and stack.peek().y != pk.ply.y-1 :
    #         stack.push(self.ply)
    #         self.move_up()
    #     elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.peek().y != pk.ply.y+1 :
    #         stack.push(self.ply)
    #         self.move_down()
    #     elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.peek().x != pk.ply.x+1 :
    #         stack.push(self.ply)
    #         self.move_right()
    #     elif self.maze[pk.ply.y][self.ply.x-1] != "X" and stack.peek().x != pk.ply.x-1:
    #         stack.push(self.ply)
    #         self.move_left()
    #     else:
    #         stack.pop()


#  def lookway(self,stack):
#         if self.maze[self.ply.y-1][self.ply.x] != "X" and stack.peek() != 'o' :
#             stack.push('o')
#             self.move_up()
#         elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.peek()!= 'o' :
#             stack.push('o')
#             self.move_down()
#         elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.peek()!= 'o' :
#             stack.push('o')
#             self.move_right()
#         elif self.maze[pk.ply.y][self.ply.x-1] != "X" and stack.peek()!= 'o':
#             stack.push('o')
#             self.move_left()
#         else:
#             pass

    # def lookway(self,stack):
    #     if self.maze[self.ply.y-1][self.ply.x] != "X" and self.maze[self.ply.y-1][self.ply.x] != 'o' and self.maze[self.ply.y-1][self.ply.x] != 'i':
    #         stack.push('i')
    #         self.move_up()
    #     elif self.maze[pk.ply.y][self.ply.x-1] != "X" and self.maze[self.ply.y][self.ply.x-1] != 'o'and self.maze[self.ply.y][self.ply.x-1] != 'i':
    #         stack.push('i')
    #         self.move_left()
    #     elif self.maze[self.ply.y][self.ply.x+1] != "X" and self.maze[self.ply.y][self.ply.x+1] != 'o' and self.maze[self.ply.y][self.ply.x+1] != 'i':
    #         stack.push('i')
    #         self.move_right()
    #     elif self.maze[self.ply.y+1][self.ply.x] != "X" and self.maze[self.ply.y+1][self.ply.x] != 'o' and self.maze[self.ply.y+1][self.ply.x] != 'i':
    #         stack.push('i')
    #         self.move_down()
    #     else:
    #         if self.maze[self.ply.y-1][self.ply.x] == 'i' or self.maze[self.ply.y-1][self.ply.x] == 'E':
    #             next_move = pos(self.ply.y-1, self.ply.x)
    #             self.maze[next_move.y][next_move.x] = 'P'
    #             self.maze[self.ply.y][self.ply.x] = 'o'
    #         elif self.maze[pk.ply.y][pk.ply.x-1] == 'i' or self.maze[pk.ply.y][pk.ply.x-1] == 'E':
    #             next_move = pos(self.ply.y, self.ply.x-1)
    #             self.maze[next_move.y][next_move.x] = 'P'
    #             self.maze[pk.ply.y][pk.ply.x] = 'o'
    #         elif self.maze[pk.ply.y][pk.ply.x+1] == 'i' or self.maze[pk.ply.y][pk.ply.x+1] == 'E':
    #             next_move = pos(self.ply.y, self.ply.x+1)
    #             self.maze[next_move.y][next_move.x] = 'P'
    #             self.maze[pk.ply.y][pk.ply.x] = 'o'
    #         elif self.maze[pk.ply.y+1][pk.ply.x] == 'i' or self.maze[pk.ply.y+1][pk.ply.x] == 'E':
    #             next_move = pos(self.ply.y+1, self.ply.x)
    #             self.maze[next_move.y][next_move.x] = 'P'
    #             self.maze[pk.ply.y
    #                       ][pk.ply.x] = 'o'
    
    # git conflict resolve
    #bug look way
    #
    
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         return 'i am kuy'
    
# class Dog(Animal):
#     def speak(self):
#         return 'woof woof'
    
# my_pet = Dog()
# print(my_pet.speak())

# arr = [3,5,6,7]
# arr = arr.sort()
# print(arr.sort())

#Maze
#6710301007
#6710301009


#can not use
# import os
# import time
# import keyboard
# from Stack import Stack

# class maze:
#     def __init__(self) -> None:
#         # self.maze = [
#         #             ["X", "X", "X", "X", "X", "X", "X"],
#         #             ["X", " ", " ", " ", "X", " ", "X"],
#         #             ["X", " ", "X", " ", "X", " ", " "],
#         #             ["X", " ", "X", " ", "X", " ", "X"],
#         #             ["X", " ", "X", " ", " ", " ", "X"],
#         #             ["X", " ", "X", "X", "X", "X", "X"],
#         #             ]
#         # self.ply = pos(5, 1)
#         # self.end = pos(2, 6)
#         # self.end = pos(5, 1)
#         # self.ply = pos(2, 6)
#         # self.maze = [
#         #             ["X", "X", "X", "X", "X", "X", "X"],
#         #             ["X", " ", " ", " ", "X", " ", "X"],
#         #             ["X", " ", "X", " ", "X", " ", "X"],
#         #             ["X", " ", "X", " ", "X", " ", "X"],
#         #             ["X", " ", "X", " ", " ", " ", "X"],
#         #             ["X", " ", "X", " ", "X", " ", " "],
#         #             ["X", " ", "X", " ", "X", " ", "X"],
#         #             ["X", "X", "X", " ", "X", " ", "X"],
#         #             ["X", " ", " ", " ", "X", " ", "X"],
#         #             ["X", " ", "X", " ", "X", " ", "X"],
#         #             ["X", " ", "X", "X", "X", "X", "X"],
#         #             ]
#         # self.ply = pos(10, 1)
#         # self.end = pos(5, 6)
#         # self.end = pos(10, 1)
#         # self.ply = pos(5, 6)
#         self.maze = [
#                     ["X", "X", "X", "X", "X", "X", "X", " ", "X"],
#                     ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
#                     ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
#                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
#                     ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
#                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
#                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
#                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
#                     ["X", " ", " ", " ", "X", " ", " ", " ", "X"],
#                     ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
#                     ["X", " ", "X", "X", "X", "X", "X", "X", "X"],
#                     ]
#         self.ply = pos(10, 1)
#         self.end = pos(0, 7)
#         self.maze[self.ply.y][self.ply.x] = "P"
#         self.maze[self.end.y][self.end.x] = "E"
#     #เช็คว่าอยู่ในบอร์ดอยู่หรือเปล่า
#     def isInBound(self, y, x):
#         if y>=0 and x>=0 and y<=len(self.maze) and x<=len(self.maze[0]):
#             return True
#         else:
#             return False
    
#     def print(self):
#         os.system("cls")
#         print("\n\n\n")
#         for row in self.maze:
#             for col in row:
#                 print(col," ", end="")
#             print("")
#         print("\n\n\n")
    
#     def printEND(self):
#         os.system("cls")
#         print("\n\n\n")
#         print(">>>>> Congraturation!!! <<<<<")
#         print("\n\n\n")
#         keyboard.wait("")

#     def move_up(self):
#         next_move = pos(self.ply.y-1, self.ply.x)
#         if self.isInBound(next_move.y,next_move.x):
#             if self.maze[next_move.y][next_move.x] == "E":
#                 self.printEND()
#                 return False
#             if self.maze[next_move.y][next_move.x] != "X":
#                 self.maze[self.ply.y][self.ply.x] = "X"
#                 self.maze[next_move.y][next_move.x] = "P"
#                 self.ply = next_move
#                 time.sleep(0.25)
#         return True
    
#     def move_down(self):
#         next_move = pos(self.ply.y+1, self.ply.x)
#         if self.isInBound(next_move.y,next_move.x):
#             if self.maze[next_move.y][next_move.x] == "E":
#                 self.printEND()
#                 return False
#             if self.maze[next_move.y][next_move.x] != "X":
#                 self.maze[self.ply.y][self.ply.x] = "X"
#                 self.maze[next_move.y][next_move.x] = "P"
#                 self.ply = next_move
#                 time.sleep(0.25)
#         return True

#     def move_left(self):
#         next_move = pos(self.ply.y, self.ply.x-1)
#         if self.isInBound(next_move.y,next_move.x): #ถ้าเป็นจริง
#             if self.maze[next_move.y][next_move.x] == "E":
#                 self.printEND()
#                 return False
#             if self.maze[next_move.y][next_move.x] != "X": #ถ้าช่องต่อไปว่าง
#                 self.maze[self.ply.y][self.ply.x] = "X" #แทนที่ก่อนหน้าเป็นช่องว่าง
#                 self.maze[next_move.y][next_move.x] = "P" #แทนที่ต่อไปด้วย P
#                 self.ply = next_move #เซตค่าปัจจุบันเป็นข้างหน้า
#                 time.sleep(0.25)
#         return True

#     def move_right(self):
#         next_move = pos(self.ply.y, self.ply.x+1)
#         if self.isInBound(next_move.y,next_move.x):
#             if self.maze[next_move.y][next_move.x] == "E":
#                 self.printEND()
#                 return False
#             if self.maze[next_move.y][next_move.x] != "X":
#                 self.maze[self.ply.y][self.ply.x] = "X"
#                 self.maze[next_move.y][next_move.x] = "P"
#                 self.ply = next_move
#                 time.sleep(0.25)
#         return True

#     def lookway(self):
#         #left
#         if self.maze[pk.ply.y][self.ply.x-1] != "X":
#             pk.move_left()
#         #up
#         elif self.maze[self.ply.y-1][self.ply.x] != "X":
#             pk.move_up()
#         #right
#         elif self.maze[self.ply.y][self.ply.x+1] != "X":
#             pk.move_right()
#         #down
#         elif self.maze[self.ply.y+1][self.ply.x] != "X":
#             pk.move_down()  
#         else:
#             pass

# class pos: 
#     def __init__(self, y=None, x=None):
#         self.y = y
#         self.x = x


# if __name__ == '__main__':

#     pk = maze()
#     print('Press Enter to start')
#     while True:
#         if keyboard.is_pressed("enter"):
#             pk.print()
#             break
#     while True:
#         if keyboard.is_pressed("q"):
#             print("Quit Program")
#             break
#         pk.lookway()
#         pk.print()
#         time.sleep(0.1)

# #เดินซ้ายอย่างเดียว no stack mark in map