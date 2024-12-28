f = open("E:\CSE221\Lab05\inp4.txt","r")
f2 = open("E:\CSE221\Lab05\out4.txt", "w")
v,e = list(map(int,f.readline().split()))
q = []
for i in range(e):
    temp = list(map(int,f.readline().split()))
    q.append([temp[0],temp[1]])
k = []
print(q)
for i in range(1,v+1):
    k.append([i])
def find(arr,ls):
    for i in arr:
        if ls in i:
            return i
for i in q:
    a = find(k,i[0])
    b = find (k,i[1])
    if a != b:
        new = a+b
        k.remove(a)
        k.remove(b)
        k.append(new)
        print(k)
        count = len(new)
        f2.write(str(count)+"\n")
    else:
        count = len(a)
        f2.write(str(count)+"\n")
f2.close()
    