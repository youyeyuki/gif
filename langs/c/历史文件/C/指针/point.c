#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define  true 1
#define  false 0
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc ������ϵͳ����������
#include <windows.h>
#include <string.h>
void pointto_intNumber(){
	int *p; int a = 9;
	p = &a;
	printf("p�ĵ�ַ��%x  a �ĵ�ַ�� %x p�����������%d \n", &p,p,*p);
	system("pause");
}
void pointtopoint(){
	int a = 9; int *p,**p2; int b =3;
	p = &a;
	p2 = &p; 
	printf(" a�ĵ�ַ(&a)�� %x  \n pָ��ĵ�ַ�� %x \n p�ĵ�ַ��&p���� %x  \n", &a, p, &p);
	printf(" p�ĵ�ַ(&p)�� %x  \n p2ָ��ĵ�ַ��p %x \n p2�ĵ�ַ��&p2���� %x  \n", &p, p2, &p2);
	//change point 

	system("pause");
}
main(){

	pointtopoint();
}
