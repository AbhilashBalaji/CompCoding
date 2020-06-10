t = int(input())

for _i in range(1,t+1):
    n = int(input())
    arr2d = []
    for i in range(n):
        arr2d.append([int(j) for j in input().split()])

    trace = 0

    nr  = 0
    nc = 0
    sr = set()
    sc = set()
    for i in range(n):

        sr = set(arr2d[i])
        sc = set(list(map(lambda x : x[i],arr2d)))
        trace += arr2d[i][i]
        if len(sr) != n :
            nr+=1
        if len(sc) != n :
            nc+=1
    
    print("Case #"+str(_i)+": "+str(trace)+" "+str(nr)+" "+str(nc))
        