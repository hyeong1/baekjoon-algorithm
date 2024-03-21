t = int(input())
stack = []
sp = -1

for i in range(t):
    current = int(input())
    if len(stack) == 0:
        stack.append(current)
        sp += 1
    else:
        if current < stack[-1]:
            stack.append(current)
            sp += 1
        else:
            while sp != -1 and current >= stack[sp]:
                stack.pop()
                sp -= 1
            if len(stack) == 0:
                stack.append(current)
                sp += 1
            elif current != stack[-1]:
                stack.append(current)
                sp += 1

print(sp + 1)