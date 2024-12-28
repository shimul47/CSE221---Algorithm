import heapq
f = open("E:\CSE221\Lab05\inp3.txt","r")
f2 = open("E:\CSE221\Lab05\out3.txt", "w")
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
        if vis[lst[j][0]] == False and max(lst[j][1],dist[src]) < dist[lst[j][0]]:
            dist[lst[j][0]] = max(lst[j][1],dist[src])
            heapq.heappush(heap,(dist[lst[j][0]],lst[j][0]))
    return dist
dist = [99999]*(v+1)
vis = [False] * (v+1)
vis[1] = True
dist [1] = 0
heap = [(0,1)]
heapq.heapify(heap)
for i in range(len(dist)):
    src = heapq.heappop(heap)[1]
    dist = dijkstra(mat,src,heap,dist,vis)
if dist[-1] != 99999:
    f2.write(str(dist[-1]))
else:
    f2.write("Impossible")
f2.close()