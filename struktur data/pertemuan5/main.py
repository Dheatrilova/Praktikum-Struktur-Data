# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

# Insert di awal
    def insert_awal(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Data berhasil ditambahkan di awal.")



# Insert di akhir
    def insert_akhir(self, data):
        new_node = Node(data)

# Jika Linked List masih kosong
        if self.head is None:
            self.head = new_node
            print("Data berhasil ditambahkan.")
            return

# Mencari Node terakhir
        current = self.head
        while current.next is not None:
            current = current.next

# Hubungkan Node terakhir dengan Node baru
        current.next = new_node
        print("Data berhasil ditambahkan di akhir.")



# Delete berdasarkan data
    def delete(self, data):

        # Jika Linked List kosong
        if self.head is None:
            print("Linked List masih kosong.")
            return

        # Jika data yang dihapus berada di Head
        if self.head.data == data:
            self.head = self.head.next
            print("Data berhasil dihapus.")
            return

        # Mencari data
        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                print("Data berhasil dihapus.")
                return

            current = current.next

        print("Data tidak ditemukan.")



# Traversal
    def tampilkan(self):
        if self.head is None:
            print("Linked List masih kosong.")
            return

        current = self.head
        print("\nIsi Linked List:")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")





# Membuat Linked List
linked_list = LinkedList()

# Menu program
while True:
    print("\n===== PROGRAM LINKED LIST =====")
    print("1. Insert Awal")
    print("2. Insert Akhir")
    print("3. Delete")
    print("4. Tampilkan Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        linked_list.insert_awal(data)

    elif pilihan == "2":
        data = input("Masukkan data: ")
        linked_list.insert_akhir(data)

    elif pilihan == "3":
        data = input("Masukkan data yang ingin dihapus: ")
        linked_list.delete(data)

    elif pilihan == "4":
        linked_list.tampilkan()

    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")