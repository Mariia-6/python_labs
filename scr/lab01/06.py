n = int(input())

count_true = 0
count_false = 0

for i in range(n):
    line = input().split()

    if line[-1] == 'True':
        count_true += 1
    else:
        count_false += 1

print(count_true,count_false)