l = []
def score(i):
    scr = 0
    word = l[i]
    for char in word :
        scr+=ord(char)-64 
    return scr*(i+1)  

with open('p022_names.txt','r') as f :
    l = f.readlines()
l =list(map(lambda x : x[1:-1] ,l[0].split(',')))
# print(sorted(l)[937]
l = sorted(l)
scrr= 0
for i in range(len(l)):
    scrr+=score(i)
print(l[937],score(937))
print(scrr)


