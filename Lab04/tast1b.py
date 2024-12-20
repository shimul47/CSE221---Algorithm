f = open("E:\CSE221\Lab04\input1b.txt","r")
f2 = open("E:\CSE221\Lab04\output1b.txt","w")
v,e = list(map(int,f.readline().split()))
listt = []
for i in range(v+1):
    listt.append([])
for j in range(e):
    temp=list(map(int,f.readline().split()))
    x = (temp[1],temp[2])
    listt[temp[0]].append(x)
for k in range(len(listt)):
    x=f"{str(k)} : "
    f2.write(x)
    for j in listt[k]:
      f2.write(str(j))
    f2.write("\n")
f2.close()