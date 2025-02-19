#การหาความลึกของโครงสร้าง Tree (เช่น Binary Tree)
# Recursion มักใช้กับโครงสร้าง ต้นไม้ (Tree) เช่น การหาความลึกของ Binary Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_depth(node):
    if node is None:  # ถ้าถึงโหนดว่าง (Base case)
        return 0
    return 1 + max(tree_depth(node.left), tree_depth(node.right))

# ตัวอย่างใช้งาน
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f"ความลึกของต้นไม้คือ {tree_depth(root)}")