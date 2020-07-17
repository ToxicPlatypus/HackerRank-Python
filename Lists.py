r = int(input())
l = []
for i in range (r):
    inp = input().split()
    if inp[0] == 'insert':
        l.insert(int(inp[1]), int(inp[2]))
    if inp[0] == 'print':
        print(l)
    if inp[0] == 'remove':
        l.remove(int(inp[1]))
    if inp[0] == 'append':
        l.append(int(inp[1]))
    if inp[0] == 'sort':
        l.sort()
    if inp[0] == 'reverse':
        l.reverse()
    if inp[0] == 'pop':
        if l != 0:
            l.pop()