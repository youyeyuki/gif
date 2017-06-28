/*

头结点 
       头节点的数据类型 与首节点类型 一样
	   头结点是首节点前面的一个节点
	   头结点不存放有效数据
	    设置头结点目的是方便对链表的操作 
头指针
        存放头节点的地址的指针变量 
首节点
       存放第一个有效数据的节点 
尾节点 
     存放最后 一个有效数据的节点 
*/ 


#include <stdio.h>

struct Node
{
	int data;
	struct Node *pNext;//下一个节点是struct Node 类型的 
}
//函数声明
struct Node *CreateList();
void TraverseList(struct Node *);

int main()
{
	 struct Node *pHead = NULL; //头指针 用来存放头结点的地址
	 
	 pHead = CreateList(); //创建链表返回信息 
	 
	 TraverseList(pHead); 
	  
	 
	return 0;
	
}

struct Node * CreateList()
{
	int len;
	int i;
	int val;
	//头结点 
	struct Node *pHead = (struct Node *)malloc(sizeof(struct Node));
	if(NULL = pHead)
	{
		printf("分配失败");
		exit(-1); 
	}
	printf("请输入生成个数len =");
	scanf("%d", &len);
	 //创建链表
	 for(i = 0 ; i < len ; ++i)
	 {
	 	printf("请输入%d个结点的值" , i+1);
		scanf("%d",&val); 
		
		struct Node *pNew = (struct Node *)malloc(sizeof(struct Node));
		if(NULL = pNew) 
		{
			printf("分配失败");
			exit(-1); 
		}
		
		pNew->data =val;
		pTail->pNext = pNew;
		pNew->pNext =NULL;
		 pTaul = pNew;
	 } 
	 
	 return pHead;
	
}

bool empty_list(struct Node *pHead)
{
	if(pHead->pNext == NULL)//pHead->pNext ==(*pHead).pNext
	return true;
	else 
	return false;
}
void TraverseList(struct Node *pHead)
{
	if(empty_list())
	{
		printf("链表为空"); 
	} 
	else
	{
		
	}
	return ;
}
