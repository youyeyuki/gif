#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<malloc.h>
#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define NUM 1000000007


void  decToBin(int decNum){
	 int total = guessSpace(decNum);
	 int i = total;
//ע��*����ȡָ����ָ��ַ���������ֵ ���Թ��� *(ָ��+1 ��ȡֵ) 
char *pArr = (char *)malloc(sizeof(char)*total);
while(i > 0){
	if(decNum != 1){
	    if( decNum % 2){ //����Ϊ����Ϊ1 
	    	*(pArr + i) = '1';
		}else{
			*(pArr + i) = '0';
		}
	decNum /= 2;
	}else{
		*(pArr + i) = '1';
	}


	
	i--;
}

while(i <= total){
	printf("%c",*(pArr + i )); 
	i++;
}
printf("\n");
}

/* ȡaΪ�� NΪ���� (NΪ��N�Ķ���)*/
double logaN(double a ,double N){
	return log10(N)/log10(a);
} 

int guessSpace(int num){

 double res = logaN(2,num);
  //pff(res);

    return  (int)(res) + 1;  //���������� ���� 111 7������2+1 3λ�����ƹ��� ����  8�Ļ� ���� 3+1 �� ����������ô������Ҫ����1  

  

} 

int main(){
int i = 1; 
while(i < 50){
	printf("%dת��������",i);
	decToBin(i);
	i++;
} 
} 

