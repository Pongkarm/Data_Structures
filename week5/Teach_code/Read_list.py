mam = [[3, 5, 7, 8],
        [4, 6, 9, 10],
        [1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mam[2])   #[1, 2, 3, 4]
print(mam[2][1]) # 2
print(mam[3][3]) # 8
#[]ตำแหน่งแรกจะเป็น Y และ [] ตัวที่ 2 จะเป็น X
# แต่เวลาเรามองเราจะมองแบบแนวนอนและตั้ง (x,y) มองปกติเลยแค่เวลาใสหาตำแหน่งให้ใส่เลขสลับกัน

#            [[3, 5, 7, 8],
#            [4, 6, 9, 10],
#            [1, 2, 3, 4],
#            [5, 6, 7, 8]]
#                   ^ มองแนวนอน ตำแหน่งของมันคือ x=2 ในแนวตั้งคือ y=3 ใช่ไหม เพราะฉนั้นเวลาใส่เลข
# ก็ต้องใส่ว่า mem[3][2] = 7
#              ^  ^
#              y  x

print(mam[3][2]) #ต้องได้ 7 นะ

# ไหนลองดุสิว่าคุณเข้าาใจเรื่อง list มากแค่ไหน
# print(mam[1][1]) #  ???
# print(mam[2][1]) #  ???
# print(mam[3][2]) #  ???
# print(mam[2][3]) #  ???
# print(mam[1][3]) #  ???


# by Pongkarm