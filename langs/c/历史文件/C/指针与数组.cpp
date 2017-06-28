/*
功能 ：用函数打印出数组

实现方法 通过指针打印

时间 2015 8 2 20:49
*/


#include<stdio.h>

void arrPrintf(int *arr, int lengh) //知道首地址和长度
{
    int i;
    for(i = 0 ; i < lengh ; i++)
    {
        printf("%d\n" , *(arr + i));	 //不需要分号

    }

}

int main()
{
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    arrPrintf(a, 10); //a[i]类型是int * a   a[i]=*(a+i)
}
