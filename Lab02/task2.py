f = open("E:\CSE221\Lab02\input2.txt" ,"r")
f2 = open("E:\CSE221\Lab02\output2.txt" ,"w")
n1 = int(f.readline())
arr1 = list(map(int,f.readline().split()))
n2 = int(f.readline())
arr2 = list(map(int,f.readline().split()))
arr3 = []
i = 0
j=0
while i<n1 and j<n2:
    if (arr1[i]<arr2[j]):
        arr3.append(arr1[i])
        i+=1
    else:
        arr3.append(arr2[j])
        j+=1
while i<n1:
    arr3.append(arr1[i])
    i+=1
while j < n2:
    arr3.append(arr2[j])
    j+=1
for i in range(len(arr3)):
    f2.write(f"{str(arr3[i])} ")

f.close()
f2.close()


