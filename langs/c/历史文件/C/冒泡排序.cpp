#include <stdio.h>

void sort ( int *pArr , int len)
{
	int i , j ,t ;
	for(i = 0 ; i < len - 1 ; ++i) //��ѭ�����Ƽ�����ѭ�� 
	{
		for(j = 0; j < len - 1 - i ; ++j)//��ѭ�������������Ƚ� 
		{
			if (pArr[j] > pArr[j+1])
			{
				t = pArr[j] ;
				pArr[j] = pArr[j+1];
				pArr[j+1] = t;
			}
		}
	}
}

int main()
{
	int a[6]={-9 , -8 , 6 , 7 ,9 ,0 };
	
	sort( a , 6);
	int i;
	for(i = 0 ; i < 6  ; ++i)
	{
		printf("%d " , a[i]);
	}
}
