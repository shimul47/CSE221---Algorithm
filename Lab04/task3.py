f = open("E:\CSE221\Lab04\input3.txt","r")
f2 = open("E:\CSE221\Lab04\output3.txt","w")
v,e = list(map(int,f.readline().split()))
mat = []
for i in range(v+1):
    mat.append([])
for j in range(e):
    temp = list(map(int,f.readline().split()))
    mat[temp[0]].append(temp[1])
visited = [False] * (v+1)

def dfs(mat,src,visited):
    visited[src] = True
    f2.write(str(src)+" ")
    for i in mat[src]:
        if visited[i] == False:
            dfs(mat,i,visited)
dfs(mat,1,visited)
f2.close()