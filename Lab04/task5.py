f = open("E:\CSE221\Lab04\input5.txt","r")
f2 = open("E:\CSE221\Lab04\output5.txt","w")
v,e,d = list(map(int,f.readline().split()))
mat = []
for i in range(v+1):
    mat.append([])
for j in range(e):
     temp = list(map(int,f.readline().split()))
     mat[temp[0]].append(temp[1])
     mat[temp[1]].append(temp[0])


def shortest_path(mat,src,v,dest):
    visited = [False]*(v+1)
    queue = [src]
    visited[src] = True
    parent = [0]*(v+1)

    while len(queue)!=0:
        parent[src] = src
        for i in mat[queue[0]]:
            if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = queue[0]
            if i == dest:
                break
        queue.pop(0)
    temp=[]
    k=dest
    while k != src:
        temp.append(k)
        k=parent[k]
    temp.append(src)
    temp.reverse()
    
    return temp
x = shortest_path(mat,1,v,d)
f2.write(str(x))
f2.close()

