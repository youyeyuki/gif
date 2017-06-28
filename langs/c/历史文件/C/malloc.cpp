/*
malloc  memory allocate 内存分配
 

*/

#include<stdio.h>
#include<malloc.h>
int main()
{
	int i = 5;
	int *p = (int*)malloc(4);//12行 分配了8个字节 左边p malloc 4个 加起来8个 
	/*                       //p 本身所占的内存是静态的  P所指向的内存是动态的 
	1.使用添加头文件
	 2.malloc 	整形形参
	 3. 4为请求系统分配的 字节
	 4.malloc 函数只能 返回第一个字节的地址
	  5.前面int 表示返回整形的地址   动态分布 
	  6. 
	*/ 
	*p = 5; //*p代表的是int变量  内存分配方式不一样 
	free(p); //把p所指向的内存所释放掉   p本身的内存不能释放 只能在程序之后释放 
	
	return 0; 
} 
