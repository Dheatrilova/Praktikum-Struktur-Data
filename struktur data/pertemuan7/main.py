class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

# Membuat Node
andi = Node("Andi")
budi = Node("Budi")
citra = Node("Citra")
deni = Node("Deni")

# Menghubungkan Node
andi.next = budi
budi.next = citra
citra.next = deni
deni.next = andi

# Menjalankan giliran
current = andi
while True:
    print("\nGiliran:", current.nama)
    pilihan = input("Tekan Enter untuk lanjut, atau ketik 'q' untuk keluar: ")
    if pilihan.lower() == "q":
        print("Program selesai.")
        break
    current = current.next