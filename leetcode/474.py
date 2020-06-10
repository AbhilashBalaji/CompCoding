def findMaxForm(strs, m, n):
    strings = []
    for i in strs:
        strings.append(list(i))
    # print(strings)
    strings.sort(key=lambda x: x.count("1"))
    # im , in, k = 0, 0 ,0
    im = 0
    inn = 0
    k = 0
    for i in strings:
        im += i.count("0")
        inn += i.count("1")
        if im > m or inn > n:
            break
        k += 1

    return k


print(findMaxForm(strs=["0001","0101","1000","1000"], m=9, n=3))
