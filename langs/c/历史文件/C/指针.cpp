#include<stdio.h>
int main()
{
	int *p;
	printf("&p指针的地址 %d\n",&p);
	int  i = 5 ;
	p=&i;
	printf("i的地址是%d\n",&i); 
	printf("直接打印指针打印的是p指向的地址%d\n",p);
	printf("*p是通过地址找到这个值 %d\n",*p);
	printf("*&p 等于p就是p指向的地址 %d\n",*&p);
	*p = 10;
	printf("修改p指向地址的值是%d\n", *p);
    printf("此时i的值是%d\n", i);
} 
