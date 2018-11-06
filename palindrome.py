def palindrome(pal):
    ar = []
    palList = list(str(pal))
    for i in range(0,int(len(palList)/2)):
        if palList[int(len(palList))-i-1] != palList[i]:
            return False
    return True

max =[]
for i in range(1000,100,-1):
    for x in range(1000,100,-1):
        if palindrome(i*x):
            max.append(i*x)

tmp = sorted(max,reverse=True)

print(tmp)
