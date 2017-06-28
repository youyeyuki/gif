#include <stdio.h>
/*
1、可以把要解决的问题转化为一个新问题，而这个新的问题的解决方法仍与原来的解决方法相同，只是所处理的对象有规律地递增或递减。
2、可以应用这个转化过程使问题得到解决。
3、必定要有一个明确的结束递归的条件。

*/ 
int fac(int);
int Comb(int,int);
int main(){

 printf("%d",Comb(7,3));
}

int fac(int n){
	if(1 == n)
	   return 1;
	else
	  return n*fac(n-1); //都是用return 作为回归条件的 
}
int Comb(int n, int m){ //c(6,3)
	if( m == n -1 )	
		return m+1;
	   
	 else if(n == m)
	     return 1;
	 else if(n < m)
	     return 0; 
	 else{
	 	return n*Comb(n-1, m);
	 	
	 }
} 
