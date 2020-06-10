'''
The problem can be solved using only string replacements.
First, replace each digit D with D (s, 
then the digit itself, then D )s.
Then eliminate all instances of )(, 
collapsing the string each time, 
until there are no more to remove.
'''
for C in range(int(input())):
  rawstr = ''.join([int(x) * '(' + x + ')' * int(x) for x in str(input())])
  for _ in range(9):
    rawstr = rawstr.replace(')(', '')
  print("Case #{}: {}".format(C+1, rawstr))