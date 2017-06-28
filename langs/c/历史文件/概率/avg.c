#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc 包含在系统函数库里面
float avg(int n,float arry[]){
	float sum = 0; int i;
 for (i = 0; i < n; i++) {
  	sum = sum + arry[i];
     }
		 printf("平均数为");
	return (sum/n);

}
float standard_Deviation(int n, float arry[],float avgrage_value) {
	float sum = 0,pre_square; int i;
	for (i = 0; i < n; i++) {
   	pre_square = arry[i] - avgrage_value;
	sum = sum + pow(pre_square,2);
    }
		return sqrt(sum / n);
}
main(){
  float standard_value,avg_value,variance;
   
  int allNum,i;
  //初始化输入的数据 
	scanf("%d\n",&allNum);
	float *arry = (float *)malloc(allNum*sizeof(float));
  for (i = 0; i < allNum; i++) {
  	scanf("%f",&arry[i]);
  }
  
 
  avg_value = avg(allNum,arry);
  standard_value = standard_Deviation(allNum,arry,avg_value);
  variance = pow(standard_value,2);
  pff(avg_value);
  pff(standard_value);
  pff(variance);
  
}
