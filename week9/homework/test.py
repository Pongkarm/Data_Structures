# pk = [45,46,47]
# pk[1:2] = [3,4]
# print(pk[1:2])

# mylist = ['apple', 'banana', 'cherry']
# mylist.insert(0, 'orange')
# print(mylist[1])

# pk = [45,46,47]
# pk1 = pk.copy() for what!!!!
# print(pk1)

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop("model")
# print(car)


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

def simple_hash(input_string):
    """ สร้างฟังก์ชันแฮชง่าย ๆ โดยใช้การรวมค่า ASCII ของตัวอักษรในสตริง """
    hash_value = 0
    for char in input_string:
        # รวมค่าของแต่ละตัวอักษรคูณด้วยตำแหน่ง
        hash_value += ord(char) * (len(input_string) - input_string.index(char))
    return hash_value % 10  # จำกัดให้ค่าแฮชอยู่ในช่วง 0-99999

# ตัวอย่างการใช้งาน
input_string = "hello"
print(f"Hash value for '{input_string}': {simple_hash(input_string)}")