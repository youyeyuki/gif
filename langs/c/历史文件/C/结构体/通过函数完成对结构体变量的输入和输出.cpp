
/*
通过函数完成对结构体的输入和输出 
*/
#include <stdio.h>
#include <string.h> 
struct Student //使用struct定义一个新的数据类型  复杂的数据类型 结构体 
 
{
	int age;
	float score;
	char name[20]; 
} ; 
/*无法修改 值 因为函数运行完就消失了 并且形参 与 实参没关系 
void InputStudent(struct Student stu)
{
	stu.age =10;
	strcpy(stu.name,"小优"); //不能写成stu.name = "张三"； 
	 stu.score = 99.2;
	
} 
*/
void OutputStudent(struct Student* psto)
{
	printf("%d %f %s " , psto->age ,psto->score,psto->name);
}
void InputStudent(struct Student * pstu)  //pstu 只占四个字节  变量地址用首地址表示 
{
	pstu->age =10;
	strcpy(pstu->name,"小优"); //不能写成stu.name = "张三"； 
	 pstu->score = 99.2;
	
} 
//定义的同时可以整体初始化  定义完只能单个赋值  
int main()
{
	struct Student  st1 ; //st1相当于一个复杂的变量
	struct Student *pst = &st1;
	
	InputStudent(&st1);
//	printf("%d %f %s\n " , st1.age ,st1.score , st1.name);
	OutputStudent(&st1); 
}
