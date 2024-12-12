import re

#EX 1 

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  

#EX2

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


#เราจะใช้ความรู้อันน้อยนิดของเราทำดู