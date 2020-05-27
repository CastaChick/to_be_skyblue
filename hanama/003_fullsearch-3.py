s = input()

acgt = set("ACGT")

ans = 0

for i in range(len(s)):
    l = 0
    for j in range(i, len(s)):
        if s[j] in acgt:
            l += 1
            if j == len(s)-1:
                ans = max(ans, l)
        else:
            ans = max(ans, l)
            break

print(ans)
