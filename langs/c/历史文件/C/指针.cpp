#include<stdio.h>
int main()
{
	int *p;
	printf("&pָ��ĵ�ַ %d\n",&p);
	int  i = 5 ;
	p=&i;
	printf("i�ĵ�ַ��%d\n",&i); 
	printf("ֱ�Ӵ�ӡָ���ӡ����pָ��ĵ�ַ%d\n",p);
	printf("*p��ͨ����ַ�ҵ����ֵ %d\n",*p);
	printf("*&p ����p����pָ��ĵ�ַ %d\n",*&p);
	*p = 10;
	printf("�޸�pָ���ַ��ֵ��%d\n", *p);
    printf("��ʱi��ֵ��%d\n", i);
} 
