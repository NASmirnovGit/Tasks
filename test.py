n = int(input())
num_max = 0
num_min = 0
num_per = 0
for i in range(1, n + 1):
    num = int(input())
    if i == 1:
        num1 = num
    if num_max < num:
        num_max = num
    if i != 1:
            if num_min < num_max and num_min < num:
                num_min = num
if num_min == num_max and num_min < num1:
    num_min = num1
print(num_max, num_min, sep='\n')