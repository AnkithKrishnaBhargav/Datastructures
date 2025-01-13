def twoStacks(maxSum, a, b):
    m,n,sum,count=0,0,0,0
    while m < len(a) and sum + a[m] <= maxSum:
        sum += a[m]
        m+= 1
        count+= 1
    max_count = count
    while n < len(b) and (m > 0 or sum + b[n] <= maxSum):
        sum+= b[n]
        n+= 1
        count+= 1
        while sum > maxSum and m > 0:
            m -= 1
            sum -= a[m]
            count -= 1
        if sum <= maxSum:
            max_count = max(max_count, count)
    return max_count

g = int(input())
result = []

for _ in range(g):
    n, m, maxSum = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result.append(twoStacks(maxSum, a, b))

for results in result:
    print(results)
