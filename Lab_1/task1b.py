input_file = open("input1b.txt","r")
output_file = open("output1b.txt","w")
n = int(input_file.readline())
for i in range(n):
    s = input_file.readline().split()
    num1 = int(s[1])
    sign = s[2]
    num2 = int(s[3])
    if (sign == "+"):
        output_file.write(f"The result of {str(num1)} {sign} {str(num2)} is {str(num1+num2)}\n")
    if (sign == "-"):
        output_file.write(f"The result of {str(num1)} {sign} {str(num2)} is {str(num1-num2)}\n")
    if (sign == "*"):
        output_file.write(f"The result of {str(num1)} {sign} {str(num2)} is {str(num1*num2)}\n")
    if (sign == "/"):
        output_file.write(f"The result of {str(num1)} {sign} {str(num2)} is {str(num1/num2)}\n")

input_file.close()
output_file.close()