#include <stdio.h>
#include <stdlib.h>
struct Data{
	int data;
	struct Data  *next; //占用4字节 
};
main(){
	struct Data *head, *last, *p;//每个占用四字节
	head = last = NULL;
	int num;
	
    scanf("%d",&num);
    while(num > 0){
    	p = (struct Data *)malloc(sizeof(struct Data));
    	p->data = num; p->next =NULL;
    	if( head == NULL){
		     head = p;
		     
	     }else{
	     	p->data = num;
	     	last->next = p;
	     	
	     }
	     
	     last = p;
	     scanf("%d",&num);
	
    }
    last->next = NULL;
    
    if(head != NULL){
    	p = head;
    	while( p!= NULL){
    	printf("%d\n",p->data);
		p = p->next;
    	}				
    }else{
		printf("空链表"); 
	}
	
}


