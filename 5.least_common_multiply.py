def divisibleSumPairs(n, k, ar):

    sums = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                sums += 1
    return sums
    #return sum(1 for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j])%k == 0)

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
