/*
原理  通过malloc创建一个变量 并且通过修改该变量的地址来修该数值 
*/

#include <stdio.h>
#include <malloc.h>
void f(int * *q)
{
	printf("传进函数后q的地址是%d\n",&q);
	printf("q指向的地址%d\n",q);
	printf("此*q取出p中地址的值%d\n",*q);  //*q 是p的值  p=5; 
	*q = (int *)malloc(sizeof(int)); //返回给q 
    printf("q指向的动态内存地址%d\n",*q);
	//q = 5 ; q是p的地址 即是&p 
	//*q = 5 ; *q = *&p ; 即是代表p 指向一个地址  该地址已经被malloc 函数创建的动态内存分配了 
	**q = 5;
	//**q 代表 **q  **&p *p 取出p指向地址的值  即说就是可以通过这个修改值 达到动态分配 

}


int main()
{
	
	int * p;

	printf("p的地址是%d\n",&p);
	f(&p);//传递p的地址 
}
