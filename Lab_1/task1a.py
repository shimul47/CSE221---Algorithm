input_file = open("E:\CSE221\LAb01\input1a.txt","r")
output_file = open("E:\CSE221\LAb01\output1a.txt","w")

count = int(input_file.readline())
for i in range(count):
    num = int (input_file.readline())
    if (num%2 == 0):
        output_file.write(f"{str(num)} is a Even number\n")
    else:
       output_file.write(f"{str(num)} is Odd number\n") 

input_file.close()
output_file.close()