def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    sorted_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index][1] < right_half[right_index][1]:
            sorted_arr.append(left_half[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_half[right_index])
            right_index += 1

    sorted_arr.extend(left_half[left_index:])
    sorted_arr.extend(right_half[right_index:])

    return sorted_arr

f = open("E:\CSE221\Lab02\input3.txt","r")
f2 = open("E:\CSE221\Lab02\output3.txt","w")
n = int(f.readline())
arr = []
fin_arr = []
count = 1

for i in range(n):
    arr.append(list(map(int,f.readline().split())))

arr = merge_sort(arr)
fin_arr.append(arr[0])
# print(arr)
for i in range(1,len(arr)):
    if (arr[i][0]>=fin_arr[len(fin_arr)-1][1]):
        fin_arr.append(arr[i])
        count+=1
f2.write(f"{str(count)}\n")
# print(fin_arr)
for i in range(len(fin_arr)):
    f2.write(f"{str(fin_arr[i][0])} {str(fin_arr[i][1])}\n")
# print(selectionSort(arr))
f.close()
f2.close()