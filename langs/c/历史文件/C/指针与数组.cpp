/*
���� ���ú�����ӡ������

ʵ�ַ��� ͨ��ָ���ӡ

ʱ�� 2015 8 2 20:49
*/


#include<stdio.h>

void arrPrintf(int *arr, int lengh) //֪���׵�ַ�ͳ���
{
    int i;
    for(i = 0 ; i < lengh ; i++)
    {
        printf("%d\n" , *(arr + i));	 //����Ҫ�ֺ�

    }

}

int main()
{
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    arrPrintf(a, 10); //a[i]������int * a   a[i]=*(a+i)
}
