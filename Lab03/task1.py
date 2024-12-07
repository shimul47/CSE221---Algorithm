def merge(a, b):
    listt = []
    i = 0
    j = 0
    while i<len(a) and j < len(b):
        if (a[i]<b[j]):
            listt.append(a[i])
            i+=1
        else:
            listt.append(b[j])
            j+=1
    while i < len(a):
        listt.append(a[i])
        i+=1
    while j < len(b):
        listt.append(b[j])
        j+=1
    return listt

def mergeSort(arr):

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[0:mid])
        a2 = mergeSort(arr[mid:len(arr)])
        return merge(a1, a2)

f = open("E:\CSE221\Lab03\input1.txt","r")
f2 = open("E:\CSE221\Lab03\output1.txt","w")

n = int(f.readline())
arr = list(map(int,f.readline().split()))
sorted_arr = mergeSort(arr)
for i in range(len(sorted_arr)):
    f2.write(str(sorted_arr[i])+" ")

f.close()
f2.close()