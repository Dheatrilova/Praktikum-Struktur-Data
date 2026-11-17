# CLASS NODE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# CLASS CIRCULAR LINKED LIST
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # INSERT DI AWAL
    def insert_awal(self, data):
        new_node = Node(data)

        # Jika Linked List masih kosong
        if self.head is None:
            self.head = new_node
            self.tail = new_node

            # Karena Circular
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node

            # Tail harus tetap menunjuk ke Head
            self.tail.next = self.head

        print("Data berhasil ditambahkan di awal.")

    # INSERT DI AKHIR
    def insert_akhir(self, data):
        new_node = Node(data)

        # Jika Linked List masih kosong
        if self.head is None:
            self.head = new_node
            self.tail = new_node

            # Membuat hubungan circular
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        print("Data berhasil ditambahkan di akhir.")

    # DELETE DATA
    def delete(self, data):

        # Jika Linked List kosong
        if self.head is None:
            print("Linked List masih kosong.")
            return

        current = self.head
        previous = self.tail

        while True:

            # Jika data ditemukan
            if current.data == data:

                # Jika hanya ada satu Node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # Jika yang dihapus adalah Head
                elif current == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head

                # Jika yang dihapus adalah Tail
                elif current == self.tail:
                    self.tail = previous
                    self.tail.next = self.head

                # Jika Node berada di tengah
                else:
                    previous.next = current.next
                print("Data berhasil dihapus.")
                return

            previous = current
            current = current.next

            # Sudah kembali ke Head
            if current == self.head:
                break

        print("Data tidak ditemukan.")

    # TRAVERSAL
    def tampilkan(self):

        if self.head is None:
            print("Linked List masih kosong.")
            return

        current = self.head

        print("\nIsi Circular Linked List:")

        while True:
            print(current.data, end=" → ")

            current = current.next

            if current == self.head:
                break

        print("(kembali ke Head)")

# PROGRAM UTAMA
linked_list = CircularLinkedList()

while True:
    print("\n================================")
    print("     CIRCULAR LINKED LIST")
    print("================================")
    print("1. Insert Awal")
    print("2. Insert Akhir")
    print("3. Delete")
    print("4. Tampilkan Data")
    print("5. Keluar")
    print("================================")

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