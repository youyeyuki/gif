#include<stdio.h>
int main(){
	int M = 4, i = 0, g = 0 , b = 0, g1;
	while(M > 0 ){
		M = M - 2 ;
		i = i + 1 ;
		g++;
		b++;
		if(4 == g)
		{
		i = i + 1 ;
		b = 0;
		b++;
		g++;		
		}
	
        if(2 == b)
		{
		i = i + 1 ;
		b = 0;
		b++;
		g++;	
		}
		if(g > 4 )
		{
			i = i + (g/4);
			g = g%4;
			b = b + (g/4);
			
		}else if(b > 2){
		   i = i + (b/2);
		   b = b%2;
		   g = g + (b/2);
		}
		
		
	}
	printf("%d %d %d ", i, g, b);
	return 0;
}
