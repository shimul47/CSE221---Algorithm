f = open("E:\CSE221\Lab02\input1.txt","r")
f2 = open("E:\CSE221\Lab02\output1.txt","w")
x = list(map(int,f.readline().split()))
n = x[0]
sum = x[1]

arr = list(map(int,f.readline().split()))
i = 0
j = len(arr)-1
flag = False
while i<=j:
    if arr[i] + arr[j] == sum:
        f2.write(f"{str(i+1)}  {str(j+1)}")
        flag = True
        break
    if arr[i] + arr[j] > sum:
        j-=1
    else:
        i+=1
if flag == False:
    f2.write("Impossible")
f.close()
f2.close()
