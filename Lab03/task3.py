f = open("E:\CSE221\input3.txt","r")
f2 = open("E:\CSE221\output3.txt","w")

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
    total_count = count_left + count_right + count
    return sorted_arr, total_count

def CheckAndMerge(left, right):          
    merged = []
    count = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(left[i])
            count += len(right) - j
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count
x = countPair(arr)
f2.write(str(x))
f.close()
f2.close()