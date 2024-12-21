f = open("E:\CSE221\Lab04\input2.txt","r")
f2 = open("E:\CSE221\Lab04\output2.txt","w")
v,e = list(map(int,f.readline().split()))
mat = []
for i in range(v+1):
  mat.append([])
for j in range(e):
  temp=list(map(int,f.readline().split()))
  mat[temp[0]].append(temp[1])
  
def bfs(mat,src,v):
  visited = [False]*(v+1)
  queue = [src]
  visited[src] = True
  path = []
  while len(queue)!=0:
    for i in mat[queue[0]]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True
    path.append(queue[0])
    queue.pop(0)
  return path
path = bfs(mat,1,v)
for i in range(len(path)):
  f2.write(str(path[i])+" ")
f2.close()
