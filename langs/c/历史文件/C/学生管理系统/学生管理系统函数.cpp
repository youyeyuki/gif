#include <stdio.h>
#include <malloc.h> 
struct Student {
	int age ;
	float score;
	char name [20];
	
};
void InPut(struct Student *pArr ,int len)
{
	int i; 
		for(i =0 ; i < len; i++)
	{
		printf("�������%d��ѧ������Ϣ ��\n", i+1);
		printf("������ѧ��������: "); 
        scanf("%s" , pArr[i].name); //���ﲻҪ����\n ���߳����ܶ���ȥ���� 
		printf("���������䣺");
		scanf("%d" ,&pArr[i].age);
		printf("�����������");
		scanf("%f", &pArr[i].score);
		
		printf("\n"); 
	}
}

void OutPut(struct Student *pArr ,int len)
{
	int i;
	   	for(i =0 ; i < len; i++)
	{
		
	
        printf(" ѧ��������:%s\n" , pArr[i].name);
	
		printf(" ѧ��������:%d\n " ,pArr[i].age);
	
		printf("ѧ���ķ���:%f\n ", pArr[i].score);
		
		printf("\n");
	}
}

void sort(struct Student *pArr ,int len)
{
	int i, j;
	struct Student t;
	for(i = 0 ; i < len ; ++i)
	 {
	 	 for(j = 0; j < len -i -1 ; j++)
	 	 {
	 	 	if(pArr[j].score >  pArr[j+1].score)  // > ���ɼ���С��������  < �Ӵ�С���� 
			  {
			  	t = pArr[j];
			    pArr[j] = pArr[j+1];
			    pArr[j+1] =  t;
			  } 
	 	 }
	 }
}

int main()
{
	int len;
	struct Student * pArr , t;
	int i , j ;
	
	printf("������ѧ��������\n");
	printf("len =  ");
	scanf("%d", &len); //����scanf���治�ܼ��Ͽո� scanf("%d ",&len); ��������ִ����һ�� 
	
	pArr = (struct Student * )malloc(len * sizeof(struct Student) );
	//���� 
    InPut(pArr , len); 
	
	//���� 
	sort(pArr , len );
	
	 
//���
   OutPut(pArr ,  len);
	return 0;
	
}
