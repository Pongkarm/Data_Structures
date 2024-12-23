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