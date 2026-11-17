SIZE = 7

hash_table = [None] * SIZE

def hash_function(key):
    return int(key) % SIZE

def insert(key, value):
    index = hash_function(key)
    start_index = index

    print(f"\nKey: {key}")
    print(f"Index awal: {index}")

    while hash_table[index] is not None:

        if hash_table[index][0] == key:
            hash_table[index] = (key, value)
            print("Data berhasil diperbarui!")
            return

        print(f"Index {index} sudah terisi!")

        index = (index + 1) % SIZE

        if index == start_index:
            print("Hash Table penuh!")
            return

    hash_table[index] = (key, value)

    print(f"Data disimpan pada index {index}")

def search(key):
    index = hash_function(key)
    start_index = index

    while hash_table[index] is not None:

        if hash_table[index][0] == key:
            print(f"Data ditemukan: {hash_table[index][1]}")
            print(f"Berada pada index: {index}")
            return

        index = (index + 1) % SIZE

        if index == start_index:
            break

    print("Data tidak ditemukan!")

def display():
    print("\n=== ISI HASH TABLE ===")

    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")

insert("231001", "Andi")
insert("231002", "Budi")
insert("231003", "Citra")
insert("231004", "Dinda")

insert("231008", "Eko")

display()

print("\n=== PENCARIAN DATA ===")
search("231008")
search("231015")