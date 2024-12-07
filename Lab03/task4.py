f = open("E:\CSE221\input4.txt","r")
f2 = open("E:\CSE221\output4.txt","w")

n = int(f.readline())
arr = list(map(int,f.readline().split()))
def countPair(arr):
  if len(arr) <= 1:
    return arr, 0
  else:
    mid = len(arr) // 2
    left, count_left = countPair(arr[:mid])
    right, count_right = countPair(arr[mid:])
    sorted_arr, count = CheckAndMerge(left, right)
    total_count =  count
    return sorted_arr, total_count

def CheckAndMerge(left, right):          
    merged = []
    maxi = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        maxi = max(maxi,left[i]+right[j]*right[j])
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, maxi
x = countPair(arr)
f2.write(str(x))
f.close()
f2.close()