#define DEBUG  //����DEBUG 
#include <stdio.h>
#include <stdlib.h> //malloc ������ϵͳ���������� 
typedef struct stu{
	int num;
	//char name[5];
	struct stu *next; //��ΪҪָ��ṹ����������� ��������ָ��Ҫ�õ�stuct stu ��������� = = 
}Stu;  //������typedef ������ ����  struct stu  �滻�� Stu  ����һ������������ 

main(){
	int i=99;
	Stu *head = NULL;
	Stu *last = NULL;
	Stu *p;  //�ṹ��ָ��4�ֽ� 
	Stu a;
	printf("%d",sizeof(a)); 
	
	p = (Stu *)malloc(sizeof(Stu));
	p->num =22; p->next=NULL;
	head = p; 
	//printf("%x\n", &head);

	printf("\n head %d p %d  address head %X p %X \n",head,p,&head,&p);
	printf("%d",head->num);
	
}
