
/*
ͨ��������ɶԽṹ����������� 
*/
#include <stdio.h>
#include <string.h> 
struct Student //ʹ��struct����һ���µ���������  ���ӵ��������� �ṹ�� 
 
{
	int age;
	float score;
	char name[20]; 
} ; 
/*�޷��޸� ֵ ��Ϊ�������������ʧ�� �����β� �� ʵ��û��ϵ 
void InputStudent(struct Student stu)
{
	stu.age =10;
	strcpy(stu.name,"С��"); //����д��stu.name = "����"�� 
	 stu.score = 99.2;
	
} 
*/
void OutputStudent(struct Student* psto)
{
	printf("%d %f %s " , psto->age ,psto->score,psto->name);
}
void InputStudent(struct Student * pstu)  //pstu ֻռ�ĸ��ֽ�  ������ַ���׵�ַ��ʾ 
{
	pstu->age =10;
	strcpy(pstu->name,"С��"); //����д��stu.name = "����"�� 
	 pstu->score = 99.2;
	
} 
//�����ͬʱ���������ʼ��  ������ֻ�ܵ�����ֵ  
int main()
{
	struct Student  st1 ; //st1�൱��һ�����ӵı���
	struct Student *pst = &st1;
	
	InputStudent(&st1);
//	printf("%d %f %s\n " , st1.age ,st1.score , st1.name);
	OutputStudent(&st1); 
}
