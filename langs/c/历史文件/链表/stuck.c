#define DEBUG  //定义DEBUG 
#include <stdio.h>
#include <stdlib.h> //malloc 包含在系统函数库里面 
typedef struct stu{
	int num;
	//char name[5];
	struct stu *next; //因为要指向结构体的数据类型 所以这里指针要用到stuct stu 这货的类型 = = 
}Stu;  //这里用typedef 声明了 即是  struct stu  替换成 Stu  这是一个新数据类型 

main(){
	int i=99;
	Stu *head = NULL;
	Stu *last = NULL;
	Stu *p;  //结构体指针4字节 
	Stu a;
	printf("%d",sizeof(a)); 
	
	p = (Stu *)malloc(sizeof(Stu));
	p->num =22; p->next=NULL;
	head = p; 
	//printf("%x\n", &head);

	printf("\n head %d p %d  address head %X p %X \n",head,p,&head,&p);
	printf("%d",head->num);
	
}
