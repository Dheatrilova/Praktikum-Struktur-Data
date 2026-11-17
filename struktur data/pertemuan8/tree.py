class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

#membuat node 
root = Node("A")
print("Node A berhasil dibuat sebagai Root.")

node_b = Node("B")
print("Node B berhasil dibuat.")

node_c = Node("C")
print("Node C berhasil dibuat.")

print("\nTree saat ini:")
print("A")
print("B dan C belum terhubung ke A.")

#Menghubungkan Child ke root
root.children.append(node_b)
print("Node B ditambahkan sebagai Child dari A.")

root.children.append(node_c)
print("Node C ditambahkan sebagai Child dari A.")

print("\nTree setelah B dan C terhubung:")
print("    A")
print("   / \\")
print("  B   C")

#Membuat node D dan E
node_d = Node("D")
print("Node D berhasil dibuat.")

node_e = Node("E")
print("Node E berhasil dibuat.")

print("\nNode D dan E belum terhubung ke Tree.")


#Menghubungkan D DAN E KE B
node_b.children.append(node_d)
print("Node D ditambahkan sebagai Child dari B.")

node_b.children.append(node_e)
print("Node E ditambahkan sebagai Child dari B.")

print("\nStruktur Tree sekarang:")
print("      A")
print("     / \\")
print("    B   C")
print("   / \\")
print("  D   E")

#Menampilkan Child dari B
parent = node_b

print("Parent yang dipilih:", parent.data)
print("Daftar Child dari B:")

for child in parent.children:
    print("Child:", child.data)

#Menampilkan child dari root 
print("Parent yang dipilih:", root.data)

for child in root.children:
    print("Child:", child.data)