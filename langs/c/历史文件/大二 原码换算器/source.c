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
//注意*就是取指针所指地址处保存的数值 可以功过 *(指针+1 获取值) 
char *pArr = (char *)malloc(sizeof(char)*total);
while(i > 0){
	if(decNum != 1){
	    if( decNum % 2){ //整除为余数为1 
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

/* 取a为底 N为真数 (N为底N的对数)*/
double logaN(double a ,double N){
	return log10(N)/log10(a);
} 

int guessSpace(int num){

 double res = logaN(2,num);
  //pff(res);

    return  (int)(res) + 1;  //这里估算错了 例如 111 7代表是2+1 3位二进制构成 的数  8的话 是由 3+1 个 所以无论怎么样都是要加上1  

  

} 

int main(){
int i = 1; 
while(i < 50){
	printf("%d转二进制是",i);
	decToBin(i);
	i++;
} 
} 

