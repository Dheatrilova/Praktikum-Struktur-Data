class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#INSERT NODE
def insert(root, data):
    if root is None:
        print(f"Node {data} berhasil ditambahkan.")
        return Node(data)

    if data < root.data:
        print(f"{data} lebih kecil dari {root.data}, menuju kiri.")
        root.left = insert(root.left, data)

    elif data > root.data:
        print(f"{data} lebih besar dari {root.data}, menuju kanan.")
        root.right = insert(root.right, data)

    else:
        print(f"Data {data} sudah ada, tidak ditambahkan.")
    return root


#SEARCH DATA
def search(root, target):
    if root is None:
        print(f"Data {target} tidak ditemukan.")
        return False

    print(f"Memeriksa Node {root.data}.")

    if target == root.data:
        print(f"Data {target} berhasil ditemukan!")
        return True

    elif target < root.data:
        print(f"{target} lebih kecil dari {root.data}, cari ke kiri.")
        return search(root.left, target)

    else:
        print(f"{target} lebih besar dari {root.data}, cari ke kanan.")
        return search(root.right, target)

#MENCARI NODE DENGAN NILAI TERKECIL
def find_min(root):
    while root.left is not None:
        root = root.left
    return root

#DELETE NODE
def delete(root, data):
    if root is None:
        print(f"Data {data} tidak ditemukan.")
        return None

    if data < root.data:
        print(f"{data} lebih kecil dari {root.data}, cari ke kiri.")
        root.left = delete(root.left, data)

    elif data > root.data:
        print(f"{data} lebih besar dari {root.data}, cari ke kanan.")
        root.right = delete(root.right, data)

    else:
        print(f"Node {data} ditemukan dan akan dihapus.")

        #KASUS 1: Node tidak memiliki Child kiri
        if root.left is None:
            if root.right is None:
                print("Node merupakan Leaf.")
            else:
                print("Node memiliki satu Child kanan.")
            return root.right

        #KASUS 2: Node tidak memiliki Child kanan
        if root.right is None:
            print("Node memiliki satu Child kiri.")
            return root.left

        #KASUS 3 :Node memiliki dua Child
        print("Node memiliki dua Child.")
        successor = find_min(root.right)
        print( "Nilai terkecil pada subtree kanan:",successor.data)
        print(f"Nilai Node {root.data} diganti menjadi {successor.data}.")
        root.data = successor.data
        print(f"Menghapus Node pengganti {successor.data} dari posisi asalnya.")
        root.right = delete(root.right, successor.data)
    return root

#TRAVERSAL PREORDER
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


#TRAVERSAL INORDER
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


#TRAVERSAL POSTORDER
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


#MENAMPILKAN SEMUA TRAVERSAL
def tampilkan_traversal(root):
    if root is None:
        print("BST masih kosong.")
        return

    print("\nHasil Traversal BST")
    print("Preorder  :", end=" ")
    preorder(root)

    print("\nInorder   :", end=" ")
    inorder(root)

    print("\nPostorder :", end=" ")
    postorder(root)

    print()


root = None
while True:
    print("1. Insert Data")
    print("2. Search Data")
    print("3. Delete Data")
    print("4. Tampilkan Preorder")
    print("5. Tampilkan Inorder")
    print("6. Tampilkan Postorder")
    print("7. Tampilkan Semua Traversal")
    print("8. Keluar")
    

    pilihan = input("Pilih menu (1-8): ")

    if pilihan == "1":
        try:
            data = int(input("Masukkan angka yang ingin ditambahkan: "))
            root = insert(root, data)
        except ValueError:
            print("Input harus berupa angka bulat.")

    elif pilihan == "2":
        try:
            target = int(input("Masukkan angka yang ingin dicari: "))
            search(root, target)
        except ValueError:
            print("Input harus berupa angka bulat.")

    elif pilihan == "3":
        try:
            data = int(input("Masukkan angka yang ingin dihapus: "))
            if search(root, data):
                print("\nMemulai proses Delete...")
                root = delete(root, data)
                print("Proses Delete selesai.")
            else:
                print("Tidak ada data yang dihapus.")

        except ValueError:
            print("Input harus berupa angka bulat.")

    elif pilihan == "4":
        if root is None:
            print("BST masih kosong.")
        else:
            print("Preorder:", end=" ")
            preorder(root)
            print()

    elif pilihan == "5":
        if root is None:
            print("BST masih kosong.")
        else:
            print("Inorder:", end=" ")
            inorder(root)
            print()

    elif pilihan == "6":
        if root is None:
            print("BST masih kosong.")
        else:
            print("Postorder:", end=" ")
            postorder(root)
            print()

    elif pilihan == "7":
        tampilkan_traversal(root)

    elif pilihan == "8":
        print("Program BST selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-8.")