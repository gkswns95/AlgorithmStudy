n, k = map(int, input().split())

josephus_list = [i for i in range(1, n+1)]
permutation_list = []

idx = k - 1
while len(josephus_list):
    if idx >= len(josephus_list):
        idx = idx % len(josephus_list)
    else:
        permutation_list.append(str(josephus_list.pop(idx)))
        idx += k - 1

print('<' + ', '.join(permutation_list) + '>', sep='')
