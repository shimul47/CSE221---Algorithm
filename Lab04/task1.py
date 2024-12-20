f = open("E:\CSE221\Lab04\input1.txt","r")
f2 = open("E:\CSE221\Lab04\output1.txt","w")
v,e = list(map(int,f.readline().split()))
adj_mat = [0]*(v+1)
for i in range(v+1):
    adj_mat[i] = [0]*(v+1)
for j in range(e):
    temp=list(map(int,f.readline().split()))
    adj_mat[temp[0]][temp[1]] = temp[2]
for x in range(len(adj_mat)):
    for y in adj_mat[x]:
        f2.write(str(y)+" ")
    f2.write("\n")    

f2.close()