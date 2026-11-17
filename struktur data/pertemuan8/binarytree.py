class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root= Node("A")
print("Node A berhasil dibuat sebagai root")

print("Left Child A :", root.left)
print("Right Child A :", root.right)

print("\nTree saat ini:")
print("A")
print("Node A belum memiliki children")

root.left = Node ("B")
print("Node B berhasil ditambahkan sebagai left child A")

root.right = Node ("C")
print("Node C berhasil ditambahkan sebagai right child A")

print("Root A :", root.data)
print("Left Child A :", root.left.data)
print("Right Child A :", root.right.data)

print("\nTree saat ini :")
print("   A")
print("  /  \\")
print("  B   C")

root.left.left = Node ("D")
print("node D child dri B")

root.left.right = Node ("E")
print("node E child dri B")

print("\n Data pada node B")
print("node B :", root.left.data)
print("Left child b :", root.left.left.data)
print("Right child b :", root.left.right.data)

print("\nTree saat ini :")
print("   A")
print("  /  \\")
print("  B   C")
print("  /\\")
print("  D E")

print("Root:", root.data)
print("Left child dari A:", root.left.data)

print("Left child dari B:", root.left.left.data)
print("Right child dari B:", root.left.right.data)

print("left child dari c:", root.right.left)
print("Right child dari c:", root.right.right)



#bagian preorder
def preorder(node) :
    if node is not None:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)

print("\nPreorder :")
preorder(root)

#bagian inorder
def inorder(node) :
    if node is not None:
        inorder(node.left)
        print(node.data, end="")
        inorder(node.right)

print("\nInorder :")
inorder(root)

#bagian postorder
def postorder(node) :
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end="")

print("\nPostorder :")
postorder(root)