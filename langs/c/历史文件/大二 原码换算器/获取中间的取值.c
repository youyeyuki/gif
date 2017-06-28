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

/* 取a为底 N为真数 (N为底N的对数) */
double logaN(double a ,double N){
	return log10(a)/log10(N);
} 
/*
去某个取值的间距 需要的变量
space 间距的大小
一个flag 来判断数值是否在这里间距之间 
获取 res 加一的值来获取下一个间距 



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
				after = (int)(res) + 1; //用来初始化第一个参数 
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
	
