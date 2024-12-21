f = open("E:\CSE221\Lab04\input4.txt","r")
f2 = open("E:\CSE221\Lab04\output4.txt","w")
v,e = list(map(int,f.readline().split()))
mat = []
for i in range(v+1):
    mat.append([])
for j in range(e):
    temp = list(map(int,f.readline().split()))
    mat[temp[0]].append(temp[1])
visited = [False] * (v+1)
track = "No"

def cycle_dfs(mat,src,visited):
    global track
    if visited[src] == True:
        track = "YES"
    else:
        visited[src] = True
        for i in mat[src]:
            cycle_dfs(mat,i,visited)
            visited[i] = False
cycle_dfs(mat,1,visited)
f2.write(track)
f2.close()