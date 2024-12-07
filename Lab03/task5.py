f = open("E:\CSE221\input5.txt","r")
f2 = open("E:\CSE221\output5.txt","w")

n = int(f.readline())
arr = list(map(int,f.readline().split()))
def quick (arr,l,h):
    if l<h:
        q = partition(arr,l,h)
        quick(arr,l,q-1)
        quick(arr,q+1,h)
    return arr
def partition(arr,l,h):
    x = arr[h]
    i = l-1
    for j in range(l, h, 1):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]  
    return i+1
x = quick(arr,0,n-1)
f2.write(str(x))
f2.close()
