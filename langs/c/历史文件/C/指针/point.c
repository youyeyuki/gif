#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define  true 1
#define  false 0
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc 包含在系统函数库里面
#include <windows.h>
#include <string.h>
void pointto_intNumber(){
	int *p; int a = 9;
	p = &a;
	printf("p的地址是%x  a 的地址是 %x p里面的内容是%d \n", &p,p,*p);
	system("pause");
}
void pointtopoint(){
	int a = 9; int *p,**p2; int b =3;
	p = &a;
	p2 = &p; 
	printf(" a的地址(&a)是 %x  \n p指向的地址是 %x \n p的地址（&p）是 %x  \n", &a, p, &p);
	printf(" p的地址(&p)是 %x  \n p2指向的地址是p %x \n p2的地址（&p2）是 %x  \n", &p, p2, &p2);
	//change point 

	system("pause");
}
main(){

	pointtopoint();
}
