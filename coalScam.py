cases = int(input())
for case in range(cases):
    N, m1, m2 = int(input()), int(input()), int(input())
    cost1 = 0
    cost2 = 0
    total = 0
    u1 = []
    uv1 = []
    c1 = []
    u2 = []
    uv2 = []
    c2 = []
    i, j, total = 0, 0, 0
    for others in range(m1):
        u1.append(int(input()))
        u1.append(int(input()))
        uv1.append(u1)
        u1 = []
        c1.append(int(input()))
        
    for chef in range(m2):
        u2.append(int(input()))
        u2.append(int(input()))
        uv2.append(u2)
        u2 = []
        c2.append(int(input()))
               
    total = sum(c1) + sum(c2)
    if m1+m2 == N:
        for i in range(len(uv2)):
            if uv1[i] == uv2[i]:
                total -= c1[i]
        
        print(c2[i], total)
    else:
        print("Impossible")
    
