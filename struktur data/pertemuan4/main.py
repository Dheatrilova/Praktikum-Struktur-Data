queue = []

# Enqueue
queue.append("Andi")
queue.append("Budi")
queue.append("Citra")

print("Queue:", queue)

# Front
print("Front:", queue[0])

# Rear
print("Rear:", queue[-1])

# Dequeue
data = queue.pop(0)

print("Data keluar:", data)
print("Queue setelah dequeue:", queue)