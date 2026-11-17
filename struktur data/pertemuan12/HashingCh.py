SIZE = 7

hash_table = [[] for _ in range(SIZE)]

def hash_function(key):
    return int(key) % SIZE

def insert(key, value):
    index = hash_function(key)

    print(f"\nKey: {key}")
    print(f"Index: {index}")

    for i, data in enumerate(hash_table[index]):
        if data[0] == key:
            hash_table[index][i] = (key, value)
            print("Data berhasil diperbarui!")
            return

    hash_table[index].append((key, value))

    print(f"Data disimpan pada index {index}")

def search(key):
    index = hash_function(key)

    for data in hash_table[index]:
        if data[0] == key:
            print(f"Data ditemukan: {data[1]}")
            print(f"Berada pada index: {index}")
            return

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