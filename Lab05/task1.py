import heapq
f = open("E:\CSE221\Lab05\inp1.txt","r")
f2 = open("E:\CSE221\Lab05\out1.txt", "w")
v,e = list(map(int,f.readline().split()))
mat = []
for i in range(v+1):
    mat.append([])
for j in range(e):
    temp = list(map(int,f.readline().split()))
    x = (temp[1],temp[2])
    mat[temp[0]].append(x)
def dijkstra(mat,src,heap,dist,vis):
    lst = mat[src]
    vis[src] = True
    for j in range(len(lst)):
        if vis[lst[j][0]] == False and lst[j][1]+dist[src] < dist[lst[j][0]]:
            dist[lst[j][0]] = lst[j][1]+dist[src]
            heapq.heappush(heap,(dist[lst[j][0]],lst[j][0]))
    return dist
src = int(f.readline())

heap = [(0,src)]
heapq.heapify(heap)
dist = [999999]*(v+1)
vis = [False]*(v+1)
dist[src] = 0
vis[src] = True
while len(heap)>0:
    src = heapq.heappop(heap)[1]
    dist = dijkstra(mat,src,heap,dist,vis)
for i in range(1,len(dist)):
   if dist[i]!=999999:
       f2.write(str(dist[i])+" ")
   else:
       f2.write("-1"+" ")
f2.close()