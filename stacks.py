
size = 10
stack = [0]*size

top = -1


def push_item(item):
    global top, size
    if (top == size - 1):
        print("FULL")
    else:
        top += 1
        stack[top] = item


def pop_item():
    global top, size
    if top == -1:
        print("empty")
    else:
        print(stack[top])
        top -= 1


# ch = int(input("1.display 2.push 3.pop"))
push_item(6)
push_item(4)
push_item(46)
push_item(444)
push_item(40)
push_item(550)
pop_item()
pop_item()
pop_item()


print(stack)
new_stack = stack[0:top+1]
print(*new_stack[::-1])
# for i in range(top):
#     print(stack[i])
# if ch == 1:
#     if top == -1:
#         print("empty")
#     else:
#         for i in range(0, top):
#             print(stack[i])


# if ch == 2:
#     num = int(input("enter number : "))
#     push_item(num)
# if ch == 3:
#     pop_item()
