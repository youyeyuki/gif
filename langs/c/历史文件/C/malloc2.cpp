

#include<stdio.h>
#include<malloc.h>
void f(int *q)  //q��p�Ŀ��� ���Ǹ���
 
{
	//*p= 200; //error
	//q=200; //error qֻ�������̬����ĵ�ַ
	//**q=200; //error  *q ������ǰ���*  ���� ���α��� ǰ�治�ܼ���*
	*q=200; 
   // free(q);//��qָ����ֽ��ͷ���
}

  int main()
  {
  	int *p=(int*)malloc(4);
  	
  	*p=10;
  	printf("%d\n", *p);
  	f(p);                //ͨ����̬�����޸ĺ�����ֵ 200
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
