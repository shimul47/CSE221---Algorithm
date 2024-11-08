def bubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = False 
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if flag == False: 
            break

input_file = open("E:\\CSE221\\input2.txt", "r")
output_file = open("E:\\CSE221\\output2.txt", "w")

n = int(input_file.readline())
arr = input_file.readline().split()
arr = list(map(int, arr))
bubbleSort(arr)

for i in range(len(arr)):
    output_file.write(f"{arr[i]}\n")
input_file.close()
output_file.close()