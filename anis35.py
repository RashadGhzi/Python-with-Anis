"""

## This is stack data structure.
stack = ["Anisur Islam", "Pial Uddin", "Manik Hossein"]
print(stack)

stack.pop()
print(stack)

stack.append("Selim Islam")  # Push is (Append).
print(stack)

stack.pop()
print("Now the top stack is ", stack[-1])

stack.pop()
print(stack)

stack.pop()
if not stack:
    print("No items left.")

"""




## This is Queue data structure.
from collections import deque
queue = deque(["Porimol", "Asif Islam", "Murad"])
print("Now, The top item is ", queue[0])

queue.popleft()
print(queue)

queue.appendleft("Jotish")
print(queue)

queue.popleft()
queue.popleft()
queue.popleft()

if not queue:
    print("No items left.")


