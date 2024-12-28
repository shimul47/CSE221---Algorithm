def kahns_algo(vertex,edge):
  lst=[]
  in_deg=[0]*(vertex+1)
  for i in range(vertex+1):
    lst.append([])
  for j in range(edge):
    temp=list(map(int,inp.readline().split()))
    row=temp[0]
    print(row)
    col=temp[1]
    print(col)
    lst[row].append(col)
    in_deg[col]+=1
  print(in_deg)
  in_deg[0]=None
  print(in_deg)
  
  queue=[]
  for k in range(len(in_deg)):
    if in_deg[k]==0:
      queue.append(k)

  travarsal=[]
  while len(queue)!=0:
    x=queue[0]
    for i in (lst[x]):
      if in_deg[i]>1:
        in_deg[i]-=1
      else:
        queue.append(i)
    travarsal.append(x)
    queue.pop(0)
  return travarsal

inp=open("E:\CSE221\input9a.txt","r")
out=open("E:\CSE221\output9a.txt","w")

arr=list(map(int,inp.readline().split()))
x=kahns_algo(arr[0],arr[1])
if len(x)==arr[0]:
  for i in range(len(x)):
    k=str(x[i])+" "
    out.write(k)
else:
    out.write("IMPOSSIBLE")
inp.close()
out.close()