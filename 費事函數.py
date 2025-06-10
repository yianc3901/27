def fab(n):
    if n == 0: returm 0
    if n == 1: returm 1
    returm fab(n-1) + fab(n-2)
for i in range(20):
    print(fab(i), " ", end="")