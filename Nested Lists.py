x = int(input())
marksheet = []
marks = []
for i in range (x):
    name = input()
    mark = float(input())
    marksheet += [[name, mark]]
    marks += [mark]

search = sorted(set(marks))[1]
for i, j in sorted(marksheet):
    if j == search:
        print(i)