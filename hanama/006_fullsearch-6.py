n = int(input())
s = input()

ans = 0

for i in range(100):
    num = str(i).zfill(2)
    k = 0
    for j in range(len(s)):
        if num[k] == s[j]:
            k += 1
        if k == 2:
            ans += len(set(s[j+1:]))
            break

print(ans)
