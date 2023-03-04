def triangles():
    l = [1]  # 定义前
    while True:
        n = len(l)
        t = list(range(n + 1))
        t[0] = l[0]
        t[n] = l[n - 1]
        yield l
        i = 0
        while i < n - 1:
            t[i + 1] = l[i] + l[i + 1]
            i = i + 1
        l = t


n1 = 0
results = []
for t in triangles():
    results.append(t)
    n1 = n1 + 1
    if n1 == 10:
        break

for i in results:
    print(i)
