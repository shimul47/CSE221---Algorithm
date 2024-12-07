# task 4 (nlogn) solution
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]

    l = merge_sort(l)
    r = merge_sort(r)
    arr = []
    li, ri = 0, 0

    while li < len(l) and ri < len(r):
        if l[li][1] < r[ri][1]:
            arr.append(l[li])
            li += 1
        else:
            arr.append(r[ri])
            ri += 1

    arr.extend(l[li:])
    arr.extend(r[ri:])

    return arr

f = open("E:\CSE221\Lab02\input4.txt","r")
f2 = open("E:\CSE221\Lab02\output4.txt","w")

n = list(map(int,f.readline().split()))
task = n[0]
people = n[1]
arr = []

for i in range(task):
    arr.append(list(map(int,f.readline().split())))
arr = merge_sort(arr)

f.close()
f2.close()

