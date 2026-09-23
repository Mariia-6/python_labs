n = int(input('in_1: '))

count_true = 0
count_false = 0

for i in range(n):
    line = input(f'in_{i +2}: ').split()

    if line[-1] == 'True':
        count_true += 1
    else:
        count_false += 1

print('out:',count_true,count_false)