#define DEBUG  //����DEBUG 
#include <stdio.h>
#include <stdlib.h> //malloc ������ϵͳ���������� 
typedef struct stu{
	int num;
	char name[5];
	struct stu *next; //��ΪҪָ��ṹ����������� ��������ָ��Ҫ�õ�stuct stu ��������� = = 
}Stu;  //������typedef ������ ����  struct stu  �滻�� Stu  ����һ������������ 
Stu *creat();//��ΪҪ���ص�ͷ��ַ������������͵�����ҲҪ��������ذ� 
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
		p->num = num; p->next = NULL; //��һ��p->next ��ָ��ҪΪ�� �������һ�������ʱ��Ҳ��NULL �Ͳ�������ָ��Ϊ�� 
		scanf("%s", p->name);          //p->next ��ָ�����͵Ĵ��ָ�� 
		printf("\n");
		if(NULL == head){
			head = p;
            #ifdef DEBUG
			printf("\n head %d p %d  address head %X p %X \n",head,p,&head,&p);
			#endif			
		} 
		else{
			//p->num = num;
			last->next = p; //������p��ͷ��ַ����һ��p��next ָ���ŵ�ַ 
		
		    }
	    last = p;//��last ָ�� p �����ݵĵ�ַ 
	    scanf("%d", &num);
		}
		return (head);
	}
Stu *output(Stu * head){
	Stu *p = head; //ָ��ָ��head 
	if( head != NULL){
		while( p != NULL){  //��headΪNULL��ʱ�򡡴�ӡ��Ϣ 
			printf("%d %s", p->num,p->name);
            p = p->next;//pָ����һ���ڵ� Ϊʲ���� P ��= NULL
		} 
	}
	else{
		printf("������");
	}
}

