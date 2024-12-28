
def adjacency_list(vertex,edge):
  adj_list=[]
  for i in range(vertex+1):
    adj_list.append([])
  for j in range(edge):
    temp=list(map(int,inp.readline().split()))
    row=temp[0]
    col=temp[1]
    adj_list[row].append(col)
  return adj_list

def DFS(adj_list,source,visited,lst):
  visited[source]=True
  for i in adj_list[source]:
    if visited[i]==False:
      DFS(adj_list,i,visited,lst)
      lst.append(i)
  return lst
  


def detect_cycle(adj,source,path):
  global cycle
  if path[source]==True:
    cycle=True
    return 
  else:
    path[source]=True
    for i in adj[source]:
      detect_cycle(adj,i,path)
      path[i]=False

def toposort(vertex,edge):
  global cycle
  adj_list=adjacency_list(vertex,edge)
  visited=[False]*(vertex+1)
  lst=[]
  for i in range(1,len(visited)):
    if visited[i]==False:
      path=[False]*(vertex+1)
      detect_cycle(adj_list,i,path)
      if cycle==True:
        out.write("IMPOSSIBLE")
        return 
      else:
        lst=DFS(adj_list,i,visited,lst)
        lst.append(i)

  if cycle!=True:
    lst.reverse()
    for k in lst:
      out.write(str(k)+" ")


inp=open("input1a.txt","r")
out=open("output1a.txt","w")
arr=list(map(int,inp.readline().split()))
cycle=False
toposort(arr[0],arr[1])
inp.close()
out.close()