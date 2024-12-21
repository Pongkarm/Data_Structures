class Queue:
    #สร้างตัวแปรชนิด List
    def __init__(self):
        self._qList = list()
    #เช็คว่าใน List ว่างไหม คืนค่าเป็น True False
    def isEmpty(self):
        return len(self) == 0
    #นับจำนวนว่ามีกี่อัน
    def __len__(self):
        return len(self._qList)
    #เพิ่มข้อมูลใหม่เข้าไปในคิว
    def enqueue(self, item):
        self._qList.append(item)
    #ใช้ดึงข้อมูลออกจากคิว เช็คก่อนว่าว่าไหม
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop(0)

#form Teacher