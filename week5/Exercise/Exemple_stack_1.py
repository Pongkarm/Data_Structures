from Stack import *

print("\n\n === Push Value === \n\n")

PROMPT = "Enter an int value (<0 to end): "
myStack = Stack()

value = int(input(PROMPT))
while value >= 0:
    myStack.push(value)
    value = int(input(PROMPT))

print("\n\n === Pop & Print === \n\n")

while not myStack.isEmpty():
    value = myStack.pop()
    print(value)
