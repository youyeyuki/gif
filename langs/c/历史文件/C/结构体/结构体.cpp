#include <stdio.h>

struct Student //使用struct定义一个新的数据类型  复杂的数据类型 结构体 
 
{
	int age;
	float score;
	char sex; 
} ; 
//定义的同时可以整体初始化  定义完只能单个赋值  
int main()
{
	struct Student  st1 = {8 ,99.5,'f'}; //st1相当于一个复杂的变量
	struct Student *pst = &st1;
	printf("%d %f %c\n " , st1.age ,st1.score , st1.sex);
	printf("%d %f %c " , pst->age ,pst->score , pst->sex);
	//pst->age 等价与 （*pst）.age 机器内部转化成这种形式 
}
