f = open ("E:\CSE221\Lab03\input6.txt","r")
f2 = open("E:\CSE221\Lab03\output6.txt","w")

n = int(f.readline())
arr = list(map(int,f.readline().split()))
m= int(f.readline())

def partition(arr,l,h):
    x = arr[h]
    i = l-1
    for j in range(l,h,1):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1
def find_k_small(arr,k):
    i = 0
    j = len(arr)-1
    while i<=j:
        pivot = partition(arr,i,j)
        if pivot == k-1:
            return arr[pivot]
        elif pivot > k-1:
            j = pivot -1
        else:
            i = pivot+1
    return -1
for i in range(m):
    k = int(f.readline())
    small = find_k_small(arr,k)
    f2.write(str(small)+"\n")
f2.close()
