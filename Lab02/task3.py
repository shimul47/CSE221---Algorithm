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

f = open("E:\CSE221\Lab02\input3.txt","r")
f2 = open("E:\CSE221\Lab02\output3.txt","w")
n = int(f.readline())
arr = []
fin_arr = []
count = 1

for i in range(n):
    arr.append(list(map(int,f.readline().split())))

arr = merge_sort(arr)
fin_arr.append(arr[0])
# print(arr)
for i in range(1,len(arr)):
    if (arr[i][0]>=fin_arr[len(fin_arr)-1][1]):
        fin_arr.append(arr[i])
        count+=1
f2.write(f"{str(count)}\n")
# print(fin_arr)
for i in range(len(fin_arr)):
    f2.write(f"{str(fin_arr[i][0])} {str(fin_arr[i][1])}\n")
# print(selectionSort(arr))
f.close()
f2.close()