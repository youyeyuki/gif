#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define NUM 1000000007


char decToBin(int decNum){
	 

}

/* ȡaΪ�� NΪ���� (NΪ��N�Ķ���) */
double logaN(double a ,double N){
	return log10(a)/log10(N);
} 
/*
ȥĳ��ȡֵ�ļ�� ��Ҫ�ı���
space ���Ĵ�С
һ��flag ���ж���ֵ�Ƿ���������֮�� 
��ȡ res ��һ��ֵ����ȡ��һ����� 



*/


int main(){
	 float space = 0;
     int t=1;
     double res;
     int flag = 1;
     int after ;
	while(t < 1000){
		res = logaN(t,2) ;
		if(flag == 1){
			if(t == 1){
				after = (int)(res) + 1; //������ʼ����һ������ 
			}
			
		}else{
			after = (int)(res) + 1;
		}
		if( flag = (res > (after - space)  &&  res < (after + space))) {
			pff(res);
		}
		t++;
	} 
}
	
