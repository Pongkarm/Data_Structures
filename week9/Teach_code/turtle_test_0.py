# Python program to draw square 
# using Turtle Programming 
# 1.
import turtle 
skk = turtle.Turtle() 

for i in range(4): 
	skk.forward(50) 
	skk.right(90) 
	

# Python program to draw star 
# using Turtle Programming 
# 2.
star = turtle.Turtle() 

star.right(75) 
star.forward(100) 

for i in range(4): 
	star.right(144) 
	star.forward(100) 
	

# Python program to draw hexagon 
# using Turtle Programming
# 3. 
polygon = turtle.Turtle() 

num_sides = 6
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides): 
	polygon.forward(side_length) 
	polygon.right(angle) 
	

# 4.
# Initialize the turtle 
t = turtle.Turtle() 

# Set the turtle's speed 
t.speed(1) 

# Draw the parallelogram 
for i in range(2): 
	t.forward(100) 
	t.left(60) 
	t.forward(50) 
	t.left(120) 

t.done() 