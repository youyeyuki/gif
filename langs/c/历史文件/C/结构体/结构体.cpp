#include <stdio.h>

struct Student //ʹ��struct����һ���µ���������  ���ӵ��������� �ṹ�� 
 
{
	int age;
	float score;
	char sex; 
} ; 
//�����ͬʱ���������ʼ��  ������ֻ�ܵ�����ֵ  
int main()
{
	struct Student  st1 = {8 ,99.5,'f'}; //st1�൱��һ�����ӵı���
	struct Student *pst = &st1;
	printf("%d %f %c\n " , st1.age ,st1.score , st1.sex);
	printf("%d %f %c " , pst->age ,pst->score , pst->sex);
	//pst->age �ȼ��� ��*pst��.age �����ڲ�ת����������ʽ 
}
