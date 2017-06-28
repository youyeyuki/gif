#define DEBUG  //定义DEBUG 
#include <stdio.h>
#include <stdlib.h> //malloc 包含在系统函数库里面 
typedef struct stu{
	int num;
	char name[5];
	struct stu *next; //因为要指向结构体的数据类型 所以这里指针要用到stuct stu 这货的类型 = = 
}Stu;  //这里用typedef 声明了 即是  struct stu  替换成 Stu  这是一个新数据类型 
Stu *creat();//因为要返回的头地址是这个数据类型的所以也要用这个返回啊 
Stu *output(Stu *); 

main(){
	Stu *head;
	head = creat();
	output(head);

} 
Stu *creat(){
	Stu *head, *last, *p;
	head = last = NULL;
	printf("head   %d %X    last  %d %X ", head,&head,last,&last);
	int num;
	scanf("%d", &num);
	while(num > 0){
		p = (Stu *)malloc(sizeof(Stu));
		p->num = num; p->next = NULL; //第一次p->next 的指向要为空 这样最后一项输入的时候也是NULL 就不用特意指向为空 
		scanf("%s", p->name);          //p->next 是指针类型的存放指针 
		printf("\n");
		if(NULL == head){
			head = p;
            #ifdef DEBUG
			printf("\n head %d p %d  address head %X p %X \n",head,p,&head,&p);
			#endif			
		} 
		else{
			//p->num = num;
			last->next = p; //把现在p的头地址给上一个p的next 指针存放地址 
		
		    }
	    last = p;//把last 指向 p 的内容的地址 
	    scanf("%d", &num);
		}
		return (head);
	}
Stu *output(Stu * head){
	Stu *p = head; //指针指向head 
	if( head != NULL){
		while( p != NULL){  //当head为NULL的时候　打印信息 
			printf("%d %s", p->num,p->name);
            p = p->next;//p指向下一个节点 为什上面 P ！= NULL
		} 
	}
	else{
		printf("空链表");
	}
}

