/*

ͷ��� 
       ͷ�ڵ���������� ���׽ڵ����� һ��
	   ͷ������׽ڵ�ǰ���һ���ڵ�
	   ͷ��㲻�����Ч����
	    ����ͷ���Ŀ���Ƿ��������Ĳ��� 
ͷָ��
        ���ͷ�ڵ�ĵ�ַ��ָ����� 
�׽ڵ�
       ��ŵ�һ����Ч���ݵĽڵ� 
β�ڵ� 
     ������ һ����Ч���ݵĽڵ� 
*/ 


#include <stdio.h>

struct Node
{
	int data;
	struct Node *pNext;//��һ���ڵ���struct Node ���͵� 
}
//��������
struct Node *CreateList();
void TraverseList(struct Node *);

int main()
{
	 struct Node *pHead = NULL; //ͷָ�� �������ͷ���ĵ�ַ
	 
	 pHead = CreateList(); //������������Ϣ 
	 
	 TraverseList(pHead); 
	  
	 
	return 0;
	
}

struct Node * CreateList()
{
	int len;
	int i;
	int val;
	//ͷ��� 
	struct Node *pHead = (struct Node *)malloc(sizeof(struct Node));
	if(NULL = pHead)
	{
		printf("����ʧ��");
		exit(-1); 
	}
	printf("���������ɸ���len =");
	scanf("%d", &len);
	 //��������
	 for(i = 0 ; i < len ; ++i)
	 {
	 	printf("������%d������ֵ" , i+1);
		scanf("%d",&val); 
		
		struct Node *pNew = (struct Node *)malloc(sizeof(struct Node));
		if(NULL = pNew) 
		{
			printf("����ʧ��");
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
		printf("����Ϊ��"); 
	} 
	else
	{
		
	}
	return ;
}
