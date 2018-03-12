
int main()
{
    int i,N1=9,N2=6,r,c,j;
	int arr[N1][N2];
	for(i=0;i<N1;i++)
	{
		for(j=0;j<N2;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	}
	r=0;
	c=0;
	N1 = N1-1; //N1 is maximum row number
	N2 = N2-1; //N2 is maximum column number
	while(r<=N1 && c<=N2)
	{
		for(i=c;i<=N2;i++)
		{
			printf("%d ", arr[r][i]);
		}
		r++;
		for(i=r;i<=N1;i++)
		{
			printf("%d ", arr[i][N2] );
		}
		N2--;
		if(c<N2)
		{
			for (i=N2; i>=c; --i)
			{
				printf("%d ", arr[N1][i]);
			}
            N1--;
		}
        if(r<N1)
		{
			for (i=N1; i>=r; --i)
			{
				printf("%d ", arr[i][c]);
			}
            c++;
		}
	}
    return 0;
}