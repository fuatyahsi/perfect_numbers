def perfect_list(n):
    return [k for k in range(1, n) if sum([i for i in range(1, k) if k % i == 0]) == k]
