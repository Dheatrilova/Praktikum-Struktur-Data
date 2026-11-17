stack = []

stack.append("A")
stack.append("B")
stack.append("C")

data = stack.pop()


print("TOP:", stack[-1])
print("isempty:", len(stack) == 0)
print("Stack:", stack)