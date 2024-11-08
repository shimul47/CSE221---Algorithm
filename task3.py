def insertion(arr):
    for i in range(1, len(arr),1):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
        
input_file = open("E:\CSE221\input3.txt","r")
output_file = open("E:\CSE221\output3.txt","w")
n = int(input_file.readline())
id = list(map(int,input_file.readline().split()))
number = list(map(int,input_file.readline().split()))

pair = {}
for i in range(n):
    if (number[i] in pair.keys()):
        pair[number[i]].append(id[i])
    else:
        pair[number[i]] = [id[i]]
print(pair)
sorted_number = insertion(number)
descending_sorted_numbers = sorted_number[::-1]
for i in pair:
    print(pair[i])
    insertion(pair[i])

idx_c = 0
i = 0
while (i<n):
    for num,id in pair.items():
        if descending_sorted_numbers[i] == num:          
            for j in range(len(id)):
                output_file.write(f"ID: {id[j]} Mark: {num}\n")  
                idx_c += 1
    i = idx_c     
input_file.close()
output_file.close()