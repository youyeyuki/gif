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
		printf("请输入第%d个学生的信息 ：\n", i+1);
		printf("请输入学生的姓名: "); 
        scanf("%s" , pArr[i].name); //这里不要加上\n 否者程序不能读进去数据 
		printf("请输入年龄：");
		scanf("%d" ,&pArr[i].age);
		printf("请输入分数：");
		scanf("%f", &pArr[i].score);
		
		printf("\n"); 
	}
}

void OutPut(struct Student *pArr ,int len)
{
	int i;
	   	for(i =0 ; i < len; i++)
	{
		
	
        printf(" 学生的姓名:%s\n" , pArr[i].name);
	
		printf(" 学生的年龄:%d\n " ,pArr[i].age);
	
		printf("学生的分数:%f\n ", pArr[i].score);
		
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
	 	 	if(pArr[j].score >  pArr[j+1].score)  // > 按成绩从小到大排列  < 从大到小排列 
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
	
	printf("请输入学生的人数\n");
	printf("len =  ");
	scanf("%d", &len); //这里scanf后面不能加上空格 scanf("%d ",&len); 这样不能执行下一步 
	
	pArr = (struct Student * )malloc(len * sizeof(struct Student) );
	//输入 
    InPut(pArr , len); 
	
	//排序 
	sort(pArr , len );
	
	 
//输出
   OutPut(pArr ,  len);
	return 0;
	
}
