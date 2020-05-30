import numpy as np

m = int(input())
m_li = []

for i in range(m):
    x, y = map(int, input().split())
    m_li.append((x, y))

m_li = np.array(m_li)
state = (m_li[0][0], m_li[0][1])
m_li -= m_li[0]

n = int(input())
n_li = []

for i in range(n):
    x, y = map(int, input().split())
    n_li.append((x, y))

n_set = set(n_li)

for star in n_set:
    flag = True
    m_li_ = m_li + np.array(star)
    for i in range(m):
        if not tuple(m_li_[i]) in n_set:
            flag = False
            break

    if flag:
        dx = star[0] - state[0]
        dy = star[1] - state[1]
        print(dx, dy)
        break
