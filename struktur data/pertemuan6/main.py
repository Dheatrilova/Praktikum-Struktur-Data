class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_awal(self, data):
        new_node = Node(data)

        # Jika Linked List masih kosong
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Data berhasil ditambahkan.")
            return

        # Hubungkan Node baru dengan Head lama
        new_node.next = self.head
        self.head.prev = new_node

        # Pindahkan Head ke Node baru
        self.head = new_node

        print("Data berhasil ditambahkan di awal.")

    def insert_akhir(self, data):
        new_node = Node(data)

        # Jika Linked List masih kosong
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Data berhasil ditambahkan.")
            return

        # Hubungkan Node baru dengan Tail lama
        new_node.prev = self.tail
        self.tail.next = new_node

        # Pindahkan Tail ke Node baru
        self.tail = new_node

        print("Data berhasil ditambahkan di akhir.")

    def insert_setelah(self, data_sebelum, data_baru):
        current = self.head

        # Mencari Node yang datanya sesuai
        while current is not None:
            if current.data == data_sebelum:
                new_node = Node(data_baru)

                # Hubungkan Node baru
                new_node.prev = current
                new_node.next = current.next

                # Jika current bukan Node terakhir
                if current.next is not None:
                    current.next.prev = new_node
                else:
                    # Jika dimasukkan setelah Tail
                    self.tail = new_node

                current.next = new_node
                print("Data berhasil ditambahkan.")
                return

            current = current.next
        print("Data sebelumnya tidak ditemukan.")


    def delete(self, data):
        current = self.head

        # Mencari Node
        while current is not None:
            if current.data == data:

                # Jika hanya ada satu Node
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                # Jika yang dihapus adalah Head
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                # Jika yang dihapus adalah Tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Jika Node berada di tengah
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                print("Data berhasil dihapus.")
                return

            current = current.next
        print("Data tidak ditemukan.")

    def tampil_maju(self):
        if self.head is None:
            print("Linked List masih kosong.")
            return
        current = self.head
        print("\nTraversal Maju:")
        while current is not None:
            print(current.data, end=" ⇄ ")
            current = current.next
        print("None")


    def tampil_mundur(self):
        if self.tail is None:
            print("Linked List masih kosong.")
            return
        current = self.tail
        print("\nTraversal Mundur:")
        while current is not None:
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")

linked_list = DoublyLinkedList()

while True:
    print("\n================================")
    print("     DOUBLY LINKED LIST")
    print("================================")
    print("1. Insert Awal")
    print("2. Insert Akhir")
    print("3. Insert Setelah Data")
    print("4. Delete")
    print("5. Tampilkan Maju")
    print("6. Tampilkan Mundur")
    print("7. Keluar")
    print("================================")

    pilihan = input("Pilih menu: ")


    # INSERT AWAL
    if pilihan == "1":
        data = input("Masukkan data: ")
        linked_list.insert_awal(data)


    # INSERT AKHIR
    elif pilihan == "2":
        data = input("Masukkan data: ")
        linked_list.insert_akhir(data)


    # INSERT SETELAH DATA
    elif pilihan == "3":
        data_sebelum = input("Masukkan data sebelumnya: ")
        data_baru = input("Masukkan data baru: ")
        linked_list.insert_setelah(data_sebelum, data_baru)


    # DELETE
    elif pilihan == "4":
        data = input("Masukkan data yang ingin dihapus: ")
        linked_list.delete(data)


    # TRAVERSAL MAJU
    elif pilihan == "5":
        linked_list.tampil_maju()


    # TRAVERSAL MUNDUR
    elif pilihan == "6": 
        linked_list.tampil_mundur()


    # KELUAR
    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")