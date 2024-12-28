import heapq
f = open("E:\CSE221\Lab05\inp2.txt","r")
f2 = open("E:\CSE221\Lab05\out2.txt", "w")
v,e = list(map(int,f.readline().split()))
mat = []
for i in range(v+1):
    mat.append([])
for j in range(e):
    temp = list(map(int,f.readline().split()))
    mat[temp[0]].append((temp[1],temp[2]))
src1,src2=list(map(int,f.readline().split()))
def dijkstra(mat,src,heap,vis,dist):
    lst = mat[src]
    vis[src] = True
    for i in range(len(lst)):
        if vis[lst[i][0]] == False and lst[i][1]+dist[src] < dist[lst[i][0]]:
            dist[lst[i][0]] = lst[i][1]+dist[src]
            heapq.heappush(heap,(dist[lst[i][0]],lst[i][0]))
    return dist
#for src 1
vis1 = [False]*(v+1)
dist1 = [99999]*(v+1)
heap1 = [(0,src1)]
heapq.heapify(heap1)
dist1[src1] = 0
vis1[src1] = True
while len(heap1)>0:
    src1 = heapq.heappop(heap1)[1]
    dist1 = dijkstra(mat,src1,heap1,vis1,dist1)
#for src 2
vis2 = [False]*(v+1)
dist2 = [99999]*(v+1)
heap2 = [(0,src2)]
heapq.heapify(heap2)
dist2[src2] = 0
vis2[src2] = True
while len(heap2)>0:
    src2 = heapq.heappop(heap2)[1]
    dist2 = dijkstra(mat,src2,heap2,vis2,dist2)

time = 99999
node = 0
for i in range(len(dist1)):
    if max(dist1[i],dist2[i])<time:
        time = max(dist1[i],dist2[i])
        node = i
print(dist1,dist2)
if time == 99999:
    f2.write("Impossible")
else:
    f2.write(f"time : {str(time)}\nNode : {str(node)}")
f2.close()
