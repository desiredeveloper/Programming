arr = []
for i in range(0,4):
    x =list(map(int,input().split()))
    arr.append(x)
r=0
c=0
N1=3 #N1 is maximum row number
N2=3 #N2 is maximum column number

while r<=N1 and c<=N2:
	for i in range(c,N2+1):
	    print(arr[r][i],end=' ')
	r+=1
	for i in range(r,N1+1):
	    print(arr[i][N2],end=' ')
	N2-=1
	if c<N2:
	    for i in range(N2,c-1,-1):
	        print(arr[N1][i],end=' ')
	    N1-=1
	if r<N1:
	    for i in range(N1,r-1,-1):
	        print(arr[i][c],end=' ')
	    c+=1