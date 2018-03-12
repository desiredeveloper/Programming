#code
n = int(input())
s = 0
for i in range(0,n):
    p = int(input())
    x = input()
    arr = [0 for i in range(0,26)]
    s=0
    for j in x:
        arr[ord(j)-ord('a')]+=1
    for z in x:
        if(arr[ord(z)-ord('a')]==1):
            s=1
            break
    if(s==1):
        print(z)
    else:
        print(-1)
    