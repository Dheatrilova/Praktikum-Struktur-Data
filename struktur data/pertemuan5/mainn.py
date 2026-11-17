class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node("eya")
node2 = Node("adi")
node3 = Node("nia")

# Menghubungkan node-node tersebut
node1.next = node2
node2.next = node3

