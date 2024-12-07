f = open("E:\CSE221\Lab03\input2.txt","r")
f2 = open("E:\CSE221\Lab03\output2.txt","w")

n = int(f.readline())
arr = list(map(int,f.readline().split()))
def mergeSort(arr):
    if (len(arr)<=1):
        return arr[0]
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[0:mid]) 
        a2 = mergeSort(arr[mid:]) 
        return merge(a1, a2)
def merge(arr1,arr2):
    if arr1>arr2:
        return arr1
    else:
        return arr2

x = mergeSort(arr)
f2.write(str(x))
f.close()
f2.close()