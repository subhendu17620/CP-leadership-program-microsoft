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
        return -1
    else:
        # print(stack[top])
        top -= 1


n = input("Enter :")
for i in n:
    if i == '(' or i == '{' or i == '[':
        push_item(i)
    if stack[top] == '(' and i == ')':
        pop_item()
    if stack[top] == '{' and i == '}':
        pop_item()
    if stack[top] == '[' and i == ']':
        pop_item()


new_stack = stack[0:top+1]
# print(*new_stack[::-1])

if len(new_stack) == 0:
    print("balanced")
else:
    print("not balanced")
