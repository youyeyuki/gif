

#include<stdio.h>
#include<malloc.h>
void f(int *q)  //q是p的拷贝 或是副本
 
{
	//*p= 200; //error
	//q=200; //error q只是这个动态分配的地址
	//**q=200; //error  *q 不能在前面加*  就像 整形变量 前面不能加上*
	*q=200; 
   // free(q);//把q指向的字节释放了
}

  int main()
  {
  	int *p=(int*)malloc(4);
  	
  	*p=10;
  	printf("%d\n", *p);
  	f(p);                //通过动态分配修改函数的值 200
  	printf("%d\n", *p);
  	
  	return 0;
  } 
  
  /*
10
200

--------------------------------
Process exited with return value 0
Press any key to continue . . .

free q


  
  */
