#include <stdio.h>
/*
1�����԰�Ҫ���������ת��Ϊһ�������⣬������µ�����Ľ����������ԭ���Ľ��������ͬ��ֻ��������Ķ����й��ɵص�����ݼ���
2������Ӧ�����ת������ʹ����õ������
3���ض�Ҫ��һ����ȷ�Ľ����ݹ��������

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
	  return n*fac(n-1); //������return ��Ϊ�ع������� 
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
