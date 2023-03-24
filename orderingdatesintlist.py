
# 04-1967
# 10-2012
# 06-2012
# 01-1989
# 12-2000


n = int(input())
a = []

for _ in range(n):
    a.append(input())

print(a)
ans = []
for i in a:
    p = i.split('-')
    # print(p[::-1])
    temp = '-'.join(p[::-1])
    ans.append(temp)
    # print(temp)

ans.sort()
# print(ans)

for i in ans:
    p = i.split('-')
    # print(p[::-1])
    temp = '-'.join(p[::-1])
    print(temp)


