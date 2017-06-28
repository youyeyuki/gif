#include "stdio.h"
#include "string.h"
#include "stdlib.h"

int main()
{
    int low,i,j,hi,N;
    int a[80][80];
    while(scanf("%d",&N))
    {
        if(N==0)
            break;
        low=0;
        hi=N;
        for(j=1;j<=N*(N+1)/2;low++,hi--)
        {
            for(i=low;i<hi-low;i++)
                a[low][i]=j++;
            for(i=low+1;i<hi-low;i++)
                a[i][hi-i-1]=j++;
            for(i=(hi-low)-2;i>low;i--)
                a[i][low]=j++;
        }
        for(i=0;i<N;i++)
        {
            for(j=0;j<N-i;j++)
               printf("%4d ",a[i][j]);
            printf("\n");
        }
    }
    return 0;
}
