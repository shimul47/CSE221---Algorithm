import heapq
f1 = open("E:\CSE221\Lab05\inp5.txt","r")
f2 = open("E:\CSE221\Lab05\out5.txt", "w")
def union(l1,l2):
    s = set()
    for x in l1:
        s.add(x)
    for x in l2:
        s.add(x)

    return list(s)

pq = []
n,m = map(int, f1.readline().split())

# create disjoint set
djset = []
for i in range(1,n+1):
    djset.append([i])


for x in range(m):
    s,d,w = map(int, f1.readline().split())
    heapq.heappush(pq, (w,(s,d)))

edge_set = set()
weight_sum = 0


while pq:
    #unpack
    w,t = heapq.heappop(pq)
    s,d = t

    index1 = 0
    index2 = 0

    for i in range(len(djset)):
        if s in djset[i]:
            index1 = i

        if d in djset[i]:
            index2 = i

    # same set
    if index1 == index2:
        continue

    djset.append(union(djset[index1],djset[index2]))
    djset.remove(djset[index1])
    djset.remove(djset[index2])
    weight_sum += w


f2.write(str(weight_sum))


f1.close()
f2.close()