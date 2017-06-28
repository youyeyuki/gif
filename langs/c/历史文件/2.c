#include <stdlib.h>
#include <stdio.h>
#define N 10
int main(){


int a[N], tmp, min, i, j ;


for(i = 0 ; i< N ; i++)
	scanf("%d", &a[i] );
	
	for(i = 1; i < N ; i++)
	{
		min = i -1;
		
		for(j = i; j < N  ; j++) //比较次数重第二个开始比较 
			if(a[min] > a[j])
			  min = j;
	
	    tmp = a[i-1]; a[i-1] = a[min];  a[min]=tmp;
	}
	

for(i = 0 ; i< N ; i++)
	printf("%d \n", a[i] );
	
}

