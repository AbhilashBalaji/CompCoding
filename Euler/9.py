# Monte carlo ftw (2 secs btw)
from random import randint

while True :
    a = randint(1,999)
    b = randint(1,999)
    c = (a**2 +b**2)**0.5
    if a+ b + c ==1000:
        print(a*b*c)
        break
