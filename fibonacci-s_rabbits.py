n, k = list(map(int, input().split()))

m1 = {"children": 1, "adults": 0}
m2 = {"children": 0, "adults": 1}
for month in range(n-2):
    m3 = {"children": m2["adults"]*k, "adults": m2["children"] + m2["adults"]}
    m1 = m2
    m2 = m3

print(m3["children"] + m3["adults"])