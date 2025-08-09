values = input().split()
k = int(values[0])
m = int(values[1])
max_sum=0
numbers_list=[]
for i in range(k):
    str_numbers = input().split()
    numbers_list.append(list(map(int, str_numbers)))
print(numbers_list)

for a in numbers_list[0]:
    for b in numbers_list[1]:
        for c in numbers_list[2]:
            total = (a**2 + b**2 + c**2) % m
            max_sum = max(max_sum, total)

print(max_sum)