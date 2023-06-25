def isEven(num):
  return num&1

num=int(input())
if isEven(num):
    print('odd')
else:
    print('even')