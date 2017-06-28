/*
这样是有问题的 因为在里面才能打印   q是局部的变量 
其他的可以取  访问了不该访问的空间 
*/
#include<stdio.h>
void f(int* *q)//q指针变量 存放p的地址 *q是取出来p的地址   
{
	int i =5;
	//*q 等价与q  q **q不等价与up 
	*q = &i; //p = &i;
	printf("%d\n",**q);//*q  
}

int main()
{
	int *p;
	f(&p); //出去的是&p p的地址 
	printf("%d",*p);//返回之前 i已经释放  返回sys 
	return 0; 
} 
