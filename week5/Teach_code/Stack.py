class Stack:

    def __init__(self):
        self._top = None
        self._size = 0
    #เช็คว่าใน List ว่างไหม คืนค่าเป็น True False
    def isEmpty(self):
        return self._top is None
    #นับจำนวนว่ามีกี่อัน
    def __len__(self):
        return self._size
    #เช็คข้อมูล
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item
    #ลบข้อมูลด้านบนสุดออกจาก Stack และคืนค่าของข้อมูลนั้น
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size = self._size - 1
        return node.item
    #เพิ่มข้อมูลใหม่ลงไปใน Stack ด้านบนสุด
    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size = self._size + 1
class _StackNode:
    def __init__(self, item, link):
        self.item = item    #เก็บข้อมูลของโหนด
        self.next = link    #ชี้ไปยังโหนดถัดไปใน Stack

#form Teacher