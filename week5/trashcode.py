# #     # def lookway(self):
# #     #     if self.maze[self.ply.y-1][self.ply.x] == " ":
# #     #         self.move_up()
# #     #     elif self.maze[self.ply.y+1][self.ply.x] == " ":
# #     #         self.move_down() 
# #     #     elif self.maze[self.ply.y][self.ply.x-1] == " ":
# #     #         self.move_left()
# #     #     elif self.maze[self.ply.y][self.ply.x+1] == " ":
# #             # self.move_right()
            
# # # old = self.maze[self.ply.y][self.ply.x]
# # #             self.move_up()
# # #             if self.maze[self.ply.y+1][self.ply.x] == old:
# # #                 stack.push('p')
# # #             self.move_down()
# # #             if self.maze[self.ply.y-1][self.ply.x] == old:
# # #                 stack.push('p')
# # #             self.move_left()
# # #             if self.maze[self.ply.y][self.ply.x+1] == old:
# # #                 stack.push('p')
# # #             self.move_right()
# # #             if self.maze[self.ply.y][self.ply.x-1] == old:
# # #                 stack.push('p')
# # #             return stack
            
# #             # if self.maze[self.ply.y-1][self.ply.x] != "X" and stack.pop() != 'p':
# #             #     self.move_up()
# #             #     stack.push('p')
# #             # elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.pop() != 'p':
# #             #     self.move_down()
# #             #     stack.push('p')
# #             # elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.pop() != 'p':
# #             #     self.move_right()
# #             #     stack.push('p')
# #             # elif self.maze[self.ply.y][self.ply.x-1] != "X" and stack.pop() != 'p':
# #             #     self.move_left()
# #             #     stack.push('p')
# #             # return stack


# #     # stack.push(pk.ply)
# #     # def lookway(self,stack):
# #     #     if self.maze[self.ply.y-1][self.ply.x] != "X" and stack.peek().y != pk.ply.y-1 :
# #     #         stack.push(self.ply)
# #     #         self.move_up()
# #     #     elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.peek().y != pk.ply.y+1 :
# #     #         stack.push(self.ply)
# #     #         self.move_down()
# #     #     elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.peek().x != pk.ply.x+1 :
# #     #         stack.push(self.ply)
# #     #         self.move_right()
# #     #     elif self.maze[pk.ply.y][self.ply.x-1] != "X" and stack.peek().x != pk.ply.x-1:
# #     #         stack.push(self.ply)
# #     #         self.move_left()
# #     #     else:
# #     #         stack.pop()


# # #  def lookway(self,stack):
# # #         if self.maze[self.ply.y-1][self.ply.x] != "X" and stack.peek() != 'o' :
# # #             stack.push('o')
# # #             self.move_up()
# # #         elif self.maze[self.ply.y+1][self.ply.x] != "X" and stack.peek()!= 'o' :
# # #             stack.push('o')
# # #             self.move_down()
# # #         elif self.maze[self.ply.y][self.ply.x+1] != "X" and stack.peek()!= 'o' :
# # #             stack.push('o')
# # #             self.move_right()
# # #         elif self.maze[pk.ply.y][self.ply.x-1] != "X" and stack.peek()!= 'o':
# # #             stack.push('o')
# # #             self.move_left()
# # #         else:
# # #             pass

# #     # def lookway(self,stack):
# #     #     if self.maze[self.ply.y-1][self.ply.x] != "X" and self.maze[self.ply.y-1][self.ply.x] != 'o' and self.maze[self.ply.y-1][self.ply.x] != 'i':
# #     #         stack.push('i')
# #     #         self.move_up()
# #     #     elif self.maze[pk.ply.y][self.ply.x-1] != "X" and self.maze[self.ply.y][self.ply.x-1] != 'o'and self.maze[self.ply.y][self.ply.x-1] != 'i':
# #     #         stack.push('i')
# #     #         self.move_left()
# #     #     elif self.maze[self.ply.y][self.ply.x+1] != "X" and self.maze[self.ply.y][self.ply.x+1] != 'o' and self.maze[self.ply.y][self.ply.x+1] != 'i':
# #     #         stack.push('i')
# #     #         self.move_right()
# #     #     elif self.maze[self.ply.y+1][self.ply.x] != "X" and self.maze[self.ply.y+1][self.ply.x] != 'o' and self.maze[self.ply.y+1][self.ply.x] != 'i':
# #     #         stack.push('i')
# #     #         self.move_down()
# #     #     else:
# #     #         if self.maze[self.ply.y-1][self.ply.x] == 'i' or self.maze[self.ply.y-1][self.ply.x] == 'E':
# #     #             next_move = pos(self.ply.y-1, self.ply.x)
# #     #             self.maze[next_move.y][next_move.x] = 'P'
# #     #             self.maze[self.ply.y][self.ply.x] = 'o'
# #     #         elif self.maze[pk.ply.y][pk.ply.x-1] == 'i' or self.maze[pk.ply.y][pk.ply.x-1] == 'E':
# #     #             next_move = pos(self.ply.y, self.ply.x-1)
# #     #             self.maze[next_move.y][next_move.x] = 'P'
# #     #             self.maze[pk.ply.y][pk.ply.x] = 'o'
# #     #         elif self.maze[pk.ply.y][pk.ply.x+1] == 'i' or self.maze[pk.ply.y][pk.ply.x+1] == 'E':
# #     #             next_move = pos(self.ply.y, self.ply.x+1)
# #     #             self.maze[next_move.y][next_move.x] = 'P'
# #     #             self.maze[pk.ply.y][pk.ply.x] = 'o'
# #     #         elif self.maze[pk.ply.y+1][pk.ply.x] == 'i' or self.maze[pk.ply.y+1][pk.ply.x] == 'E':
# #     #             next_move = pos(self.ply.y+1, self.ply.x)
# #     #             self.maze[next_move.y][next_move.x] = 'P'
# #     #             self.maze[pk.ply.y
# #     #                       ][pk.ply.x] = 'o'
    
# #     # git conflict resolve
# #     #bug look way
# #     #
    
# # # class Animal:
# # #     def __init__(self, name):
# # #         self.name = name
        
# # #     def speak(self):
# # #         return 'i am kuy'
    
# # # class Dog(Animal):
# # #     def speak(self):
# # #         return 'woof woof'
    
# # # my_pet = Dog()
# # # print(my_pet.speak())

# # # arr = [3,5,6,7]
# # # arr = arr.sort()
# # # print(arr.sort())

# # #Maze
# # #6710301007
# # #6710301009


# # #can not use
# # # import os
# # # import time
# # # import keyboard
# # # from Stack import Stack

# # # class maze:
# # #     def __init__(self) -> None:
# # #         # self.maze = [
# # #         #             ["X", "X", "X", "X", "X", "X", "X"],
# # #         #             ["X", " ", " ", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", " ", "X", " ", " "],
# # #         #             ["X", " ", "X", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", " ", " ", " ", "X"],
# # #         #             ["X", " ", "X", "X", "X", "X", "X"],
# # #         #             ]
# # #         # self.ply = pos(5, 1)
# # #         # self.end = pos(2, 6)
# # #         # self.end = pos(5, 1)
# # #         # self.ply = pos(2, 6)
# # #         # self.maze = [
# # #         #             ["X", "X", "X", "X", "X", "X", "X"],
# # #         #             ["X", " ", " ", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", " ", " ", " ", "X"],
# # #         #             ["X", " ", "X", " ", "X", " ", " "],
# # #         #             ["X", " ", "X", " ", "X", " ", "X"],
# # #         #             ["X", "X", "X", " ", "X", " ", "X"],
# # #         #             ["X", " ", " ", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", " ", "X", " ", "X"],
# # #         #             ["X", " ", "X", "X", "X", "X", "X"],
# # #         #             ]
# # #         # self.ply = pos(10, 1)
# # #         # self.end = pos(5, 6)
# # #         # self.end = pos(10, 1)
# # #         # self.ply = pos(5, 6)
# # #         self.maze = [
# # #                     ["X", "X", "X", "X", "X", "X", "X", " ", "X"],
# # #                     ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
# # #                     ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
# # #                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #                     ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
# # #                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #                     ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #                     ["X", " ", " ", " ", "X", " ", " ", " ", "X"],
# # #                     ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
# # #                     ["X", " ", "X", "X", "X", "X", "X", "X", "X"],
# # #                     ]
# # #         self.ply = pos(10, 1)
# # #         self.end = pos(0, 7)
# # #         self.maze[self.ply.y][self.ply.x] = "P"
# # #         self.maze[self.end.y][self.end.x] = "E"
# # #     #เช็คว่าอยู่ในบอร์ดอยู่หรือเปล่า
# # #     def isInBound(self, y, x):
# # #         if y>=0 and x>=0 and y<=len(self.maze) and x<=len(self.maze[0]):
# # #             return True
# # #         else:
# # #             return False
    
# # #     def print(self):
# # #         os.system("cls")
# # #         print("\n\n\n")
# # #         for row in self.maze:
# # #             for col in row:
# # #                 print(col," ", end="")
# # #             print("")
# # #         print("\n\n\n")
    
# # #     def printEND(self):
# # #         os.system("cls")
# # #         print("\n\n\n")
# # #         print(">>>>> Congraturation!!! <<<<<")
# # #         print("\n\n\n")
# # #         keyboard.wait("")

# # #     def move_up(self):
# # #         next_move = pos(self.ply.y-1, self.ply.x)
# # #         if self.isInBound(next_move.y,next_move.x):
# # #             if self.maze[next_move.y][next_move.x] == "E":
# # #                 self.printEND()
# # #                 return False
# # #             if self.maze[next_move.y][next_move.x] != "X":
# # #                 self.maze[self.ply.y][self.ply.x] = "X"
# # #                 self.maze[next_move.y][next_move.x] = "P"
# # #                 self.ply = next_move
# # #                 time.sleep(0.25)
# # #         return True
    
# # #     def move_down(self):
# # #         next_move = pos(self.ply.y+1, self.ply.x)
# # #         if self.isInBound(next_move.y,next_move.x):
# # #             if self.maze[next_move.y][next_move.x] == "E":
# # #                 self.printEND()
# # #                 return False
# # #             if self.maze[next_move.y][next_move.x] != "X":
# # #                 self.maze[self.ply.y][self.ply.x] = "X"
# # #                 self.maze[next_move.y][next_move.x] = "P"
# # #                 self.ply = next_move
# # #                 time.sleep(0.25)
# # #         return True

# # #     def move_left(self):
# # #         next_move = pos(self.ply.y, self.ply.x-1)
# # #         if self.isInBound(next_move.y,next_move.x): #ถ้าเป็นจริง
# # #             if self.maze[next_move.y][next_move.x] == "E":
# # #                 self.printEND()
# # #                 return False
# # #             if self.maze[next_move.y][next_move.x] != "X": #ถ้าช่องต่อไปว่าง
# # #                 self.maze[self.ply.y][self.ply.x] = "X" #แทนที่ก่อนหน้าเป็นช่องว่าง
# # #                 self.maze[next_move.y][next_move.x] = "P" #แทนที่ต่อไปด้วย P
# # #                 self.ply = next_move #เซตค่าปัจจุบันเป็นข้างหน้า
# # #                 time.sleep(0.25)
# # #         return True

# # #     def move_right(self):
# # #         next_move = pos(self.ply.y, self.ply.x+1)
# # #         if self.isInBound(next_move.y,next_move.x):
# # #             if self.maze[next_move.y][next_move.x] == "E":
# # #                 self.printEND()
# # #                 return False
# # #             if self.maze[next_move.y][next_move.x] != "X":
# # #                 self.maze[self.ply.y][self.ply.x] = "X"
# # #                 self.maze[next_move.y][next_move.x] = "P"
# # #                 self.ply = next_move
# # #                 time.sleep(0.25)
# # #         return True

# # #     def lookway(self):
# # #         #left
# # #         if self.maze[pk.ply.y][self.ply.x-1] != "X":
# # #             pk.move_left()
# # #         #up
# # #         elif self.maze[self.ply.y-1][self.ply.x] != "X":
# # #             pk.move_up()
# # #         #right
# # #         elif self.maze[self.ply.y][self.ply.x+1] != "X":
# # #             pk.move_right()
# # #         #down
# # #         elif self.maze[self.ply.y+1][self.ply.x] != "X":
# # #             pk.move_down()  
# # #         else:
# # #             pass

# # # class pos: 
# # #     def __init__(self, y=None, x=None):
# # #         self.y = y
# # #         self.x = x


# # # if __name__ == '__main__':

# # #     pk = maze()
# # #     print('Press Enter to start')
# # #     while True:
# # #         if keyboard.is_pressed("enter"):
# # #             pk.print()
# # #             break
# # #     while True:
# # #         if keyboard.is_pressed("q"):
# # #             print("Quit Program")
# # #             break
# # #         pk.lookway()
# # #         pk.print()
# # #         time.sleep(0.1)

# # # #เดินซ้ายอย่างเดียว no stack mark in map

# # # import os
# # # import time
# # # import keyboard
# # # from Stack import Stack

# # # class maze:
# # #     def __init__(self) -> None:
# # #         self.maze = [
# # #             ["X", "X", "X", "X", "X", "X", "X", " ", "X"],
# # #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
# # #             ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
# # #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #             ["X", " ", " ", " ", "X", " ", "X", " ", "X"],
# # #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #             ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
# # #             ["X", " ", " ", " ", "X", " ", " ", " ", "X"],
# # #             ["X", " ", "X", " ", " ", " ", "X", " ", "X"],
# # #             ["X", " ", "X", "X", "X", "X", "X", "X", "X"],
# # #         ]
# # #         self.ply = pos(10, 1)
# # #         self.end = pos(0, 7)
# # #         self.maze[self.ply.y][self.ply.x] = "P"
# # #         self.maze[self.end.y][self.end.x] = "E"

# # #     def isInBound(self, y, x):
# # #         return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

# # #     def print(self):
# # #         os.system("cls")
# # #         print("\n\n\n")
# # #         for row in self.maze:
# # #             print(" ".join(row))
# # #         print("\n\n\n")

# # #     def printEND(self):
# # #         os.system("cls")
# # #         print("\n\n\n")
# # #         print(">>>>> Congraturation!!! <<<<<")
# # #         print("\n\n\n")
# # #         keyboard.wait("")

# # #     def move(self, dy, dx):
# # #         next_move = pos(self.ply.y + dy, self.ply.x + dx)
# # #         if self.isInBound(next_move.y, next_move.x):
# # #             if self.maze[next_move.y][next_move.x] == "E":
# # #                 self.printEND()
# # #                 return False
# # #             if self.maze[next_move.y][next_move.x] != "X":
# # #                 self.maze[self.ply.y][self.ply.x] = " "
# # #                 self.maze[next_move.y][next_move.x] = "P"
# # #                 self.ply = next_move
# # #                 time.sleep(0.25)
# # #         return True

# # #     def lookway(self, stack):
# # #         way = 0
# # #         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # #         for dy, dx in directions:
# # #             ny, nx = self.ply.y + dy, self.ply.x + dx
# # #             if self.isInBound(ny, nx):
# # #                 if (self.maze[ny][nx] == " " or self.maze[ny][nx] == "E") and (stack.is_empty() or pos(ny, nx) != stack.peek()):
# # #                     way += 1
# # #         return way

# # #     def one_way(self, stack, time):
# # #         directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
# # #         for dy, dx in directions:
# # #             ny, nx = self.ply.y + dy, self.ply.x + dx
# # #             if self.isInBound(ny, nx):
# # #                 if (self.maze[ny][nx] == " " or self.maze[ny][nx] == "E") and (stack.is_empty() or pos(ny, nx) != stack.peek()):
# # #                     stack.push(self.ply)
# # #                     self.move(dy, dx)
# # #                     break
# # #         time += 1
# # #         return stack, time

# # #     def go_to_way(self, way, stack, time):
# # #         if way == 1:
# # #             stack, time = self.one_way(stack, time)
# # #         elif way == 0:
# # #             if not stack.is_empty():
# # #                 self.maze[self.ply.y][self.ply.x] = " "
# # #                 self.ply = stack.pop()
# # #             else:
# # #                 print("No more paths available. Exiting...")
# # #                 exit()
# # #         return stack, time

# # # class pos:
# # #     def __init__(self, y=None, x=None):
# # #         self.y = y
# # #         self.x = x

# # #     def __eq__(self, other):
# # #         return self.y == other.y and self.x == other.x

# # # # Main Program
# # # if __name__ == '__main__':
# # #     pk = maze()
# # #     stack = Stack()
# # #     _time = 0
# # #     print('Press Enter to start')
# # #     while True:
# # #         if keyboard.is_pressed("enter"):
# # #             pk.print()
# # #             break
# # #     stack.push(pk.ply)
# # #     while True:
# # #         if keyboard.is_pressed("q"):
# # #             print("Quit Program")
# # #             break
# # #         way = pk.lookway(stack)
# # #         stack, _time = pk.go_to_way(way, stack, _time)
# # #         pk.print()
# # #         print(f"Time: {_time}, Stack size: {len(stack)}")
# # #         time.sleep(0.4)
# # class Car:
# #     def __init__(self, color, brand, model, year):
# #         self.color = color
# #         self.brand = brand
# #         self.model = model
# #         self.year = year

# # # Create car objects
# # car1 = Car('red', 'ett', 'dfsdsf', 5)
# # car2 = Car('red', 'ett', 'dfsdsf', 6)
# # car3 = Car('red', 'ett', 'dfsdsf', 7)
# # car4 = Car('red', 'ett', 'dfsdsf', 8)

# # # Add cars to a list
# # pk = [car1, car2, car3, car4]

# # # Check if a year exists in the list of car objects
# # a = 5
# # print(any(car.year == a for car in pk))




# # # git reset --soft HEAD~1

# # class Calculator:
# #     # @staticmethod
# #     def add(a, b):
# #         return a + b
    
# # print(Calculator.add(5,10))

# # 
#             # if self.ply.y-1 != stack.peek().y and self.maze[self.ply.y-1][self.ply.x] != "X" and not loopstack(stack, pos(self.ply.y-1, self.ply.x)):
#             #     stack = popstackuntil_0(stack)
#             # elif self.ply.x-1 != stack.peek().x and self.maze[self.ply.y][self.ply.x-1] != "X" and not loopstack(stack, pos(self.ply.y, self.ply.x-1)):
#             #     stack = popstackuntil_0(stack)
#             # elif self.ply.x+1 != stack.peek().x and self.maze[self.ply.y][self.ply.x+1] != "X" and not loopstack(stack, pos(self.ply.y, self.ply.x+1)):
#             #     stack = popstackuntil_0(stack)
#             # elif self.ply.y+1 != stack.peek().y and self.maze[self.ply.y+1][self.ply.x] != "X" and not loopstack(stack, pos(self.ply.y+1, self.ply.x)):
#             #     stack = popstackuntil_0(stack)
#             #บนซ้ายขวา
#             # if not loopstack(stack, pos(self.ply.y-1, self.ply.x)) and not loopstack(stack, pos(self.ply.y, self.ply.x-1)) and not loopstack(stack, pos(self.ply.y, self.ply.x+1)) and self.maze[self.ply.y-1][self.ply.x] != "X" and self.maze[self.ply.y][self.ply.x+1] != "X" and self.maze[self.ply.y][self.ply.x-1] != "X":
#             #     stack = popstackuntil_0(stack)
#             # #ล่าง ขวา ซ้าย
#             # elif not loopstack(stack, pos(self.ply.y, self.ply.x-1)) and not loopstack(stack, pos(self.ply.y, self.ply.x+1)) and not loopstack(stack, pos(self.ply.y+1, self.ply.x)) and self.maze[self.ply.y+1][self.ply.x] != "X" and self.maze[self.ply.y][self.ply.x-1] != "X" and self.maze[self.ply.y][self.ply.x+1] != "X":
#             #     stack = popstackuntil_0(stack)
#             # #บนขวาล่าง
#             # elif not loopstack(stack, pos(self.ply.y-1, self.ply.x)) and not loopstack(stack, pos(self.ply.y, self.ply.x+1)) and not loopstack(stack, pos(self.ply.y+1, self.ply.x)) and self.maze[self.ply.y][self.ply.x+1] != "X" and self.maze[self.ply.y+1][self.ply.x] != "X" and self.maze[self.ply.y-1][self.ply.x] != "X":
#             #     stack = popstackuntil_0(stack)
#             # #บนซ้ายpล่าง
#             # elif not loopstack(stack, pos(self.ply.y-1, self.ply.x)) and not loopstack(stack, pos(self.ply.y, self.ply.x-1)) and not loopstack(stack, pos(self.ply.y+1, self.ply.x)) and self.maze[self.ply.y][self.ply.x-1] != "X" and self.maze[self.ply.y+1][self.ply.x] != "X" and self.maze[self.ply.y-1][self.ply.x] != "X":
#             #     stack = popstackuntil_0(stack)
#             # elif stack.peek().y == 0 and stack.peek().x == 0:
#             #     stack = popstackuntil_0(stack)
#             # else:
#             #     stack.pop()
#             #     stack.push(pos(0,0))
# # def clear_stack(stack):
# #     while stack:
# #         print(f"Popped: {stack.pop()}")
# #     print("Stack is now empty:", stack)

# # # ตัวอย่างการใช้งาน
# # stack = [5, 15, 25, 35]
# # clear_stack(stack)

# from itertools import permutations

# # ตัวเลือกทั้งหมด
# choices = ['บน', 'ซ้าย', 'ขวา', 'ล่าง']

# # สร้าง Permutations (การจัดเรียง) ของ 4 ตัวเลือก
# permutations_result = list(permutations(choices, 4))

# # for i in permutations_result:
# #     print(i[0])

# for idx, perm in enumerate(permutations_result, start=1):
#     print(idx, perm)
# # import random
# # a = random.randint(1, 24)


# self.maze = [
#             ["X", "X", "X", "X", "X", "X", "X", " ", "X", "X", "X", "X", "X"],
#             ["X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
#             ["X", " ", "X", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X"],
#             ["X", " ", "X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
#             ["X", " ", "X", " ", "X", " ", " ", " ", " ", "X", "X", " ", "X"],
#             ["X", " ", " ", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
#             ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
#             ["X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", " ", "X"],
#             ["X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X"],
#             ["X", " ", "X", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X"],
#             ["X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X"],
#             ["X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
#             ["X", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X", " ", "X"],
#             ["X", " ", "X", "X", " ", "X", "X", " ", "X", " ", "X", " ", "X"],
#             ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
#             ]




#             # i = 0
#             # if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
#             #     i += 1
#             # if not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
#             #     i += 1
#             # if not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
#             #     i += 1
#             # if not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
#             #     i += 1
#             # print(i,'jjjjjjjjjjjjjjjjj')
#             # if i > 1:
#             #     stack_i.push(self.ply)
#             #     if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)) and stack_i.peek().y != self.ply.y-1:
#             #         self.move_up()
#             #     elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)) and stack_i.peek().x != self.ply.x-1:
#             #         self.move_left()
#             #     elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)) and stack_i.peek().x != self.ply.x+1:
#             #         self.move_right()
#             #     elif not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)) and stack_i.peek().y != self.ply.y+1:
#             #         self.move_down()
#             #     stack_O.push(self.ply)
#             # elif i <= 1:
#             #     stack_O.push(self.ply)
#             #     if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
#             #         # stack_O.push(self.ply)
#             #         self.move_up()
#             #     elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
#             #         # stack_O.push(self.ply)
#             #         self.move_left()
#             #     elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
#             #         # stack_O.push(self.ply)
#             #         self.move_right()
#             #     elif not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
#             #         # stack_O.push(self.ply)
#             #         self.move_down()
            
#                         # #up
#             # if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
#             #     stack_O.push(self.ply)
#             #     self.move_up()
#             # #left
#             # elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x-1)):
#             #     stack_O.push(self.ply)
#             #     print('whatt')
#             #     self.move_left()
#             # #right
#             # elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and is_in_loopstack(stack_O, pos(self.ply.y, self.ply.x+1)):
#             #     stack_O.push(self.ply)
#             #     self.move_right()
#             # #down
#             # elif not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
#             #     stack_O.push(self.ply)
#             #     self.move_down()
            
#             # else:
#                 # if not is_in_loopstack(stack_O, pos(self.ply.y-1, self.ply.x)):
#                 #     self.move_up()
#                 # #left
#                 # elif not is_in_loopstack(stack_O, pos(self.ply, self.ply.x-1)):
#                 #     self.move_left()
#                 # #right
#                 # elif not is_in_loopstack(stack_O, pos(self.ply, self.ply.x+1)):
#                 #     self.move_right()
#                 # #down
#                 # elif not is_in_loopstack(stack_O, pos(self.ply.y+1, self.ply.x)):
#                 #     self.move_down()
#                 # print('เข้า o')
                
                
#                             # if not is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)) and stack_i.peek().y != self.ply.y-1:
#             #     # stack_O.push(self.ply)
#             #     self.move_up()
#             # elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)) and stack_i.peek().x != self.ply.x-1:
#             #     # stack_O.push(self.ply)
#             #     self.move_left()
#             # elif not is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)) and stack_i.peek().x != self.ply.x+1:
#             #     # stack_O.push(self.ply)
#             #     self.move_right()
#             # elif not is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)) and stack_i.peek().y != self.ply.y+1:
#             #     # stack_O.push(self.ply)
#             #     self.move_down()
#             # else:
#                 # if is_in_loopstack(stack_i, pos(self.ply.y-1, self.ply.x)):
#                 #     stack_O.push(self.ply)
#                 #     self.move_up()
#                 # elif is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x-1)):
#                 #     stack_O.push(self.ply)
#                 #     self.move_left()
#                 # elif is_in_loopstack(stack_i, pos(self.ply.y, self.ply.x+1)):
#                 #     stack_O.push(self.ply)
#                 #     self.move_right()
#                 # elif is_in_loopstack(stack_i, pos(self.ply.y+1, self.ply.x)):
#                 #     stack_O.push(self.ply)
#                 #     self.move_down()
#                 # print('งง')
1
# # Given values
V_S = 5  # Voltage source in volts
I_S = 6   # Current source in amperes
R1 = 8   # Resistor R1 in ohms
R2 = 1    # Resistor R2 in ohms
R3 = 8    # Resistor R3 in ohms

# Step 1: Calculate R_TH
# R1 and R2 are in parallel
R1_2 = (R1 * R2) / (R1 + R2)

# R_TH = R1_2 + R3
R_TH = R1_2 + R3

# Step 2: Calculate V_TH using superposition
# Contribution from V_S (Voltage divider across R1 and R2)
V_TH_vs = V_S * (R2 / (R1 + R2))

# Contribution from I_S (Voltage across R3)
V_TH_is = I_S * R3

# Total V_TH
V_TH = V_TH_vs + V_TH_is

# Step 3: Maximum power delivered to R_L
P_max = (V_TH**2) / (4 * R_TH)

print(R_TH)
print(V_TH)
print(P_max)

# 4


