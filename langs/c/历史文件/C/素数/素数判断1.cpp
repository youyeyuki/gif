/*
 ʱ�� 2015/7/30 22:34
 ���� �ж������ķ���֮һ 

*/


#include <stdio.h>

int main()
{
    int input, begin;
    int flag = 1;
    scanf("%d", &input);
    for(begin = 2; begin < input; begin++)
    {
        if((input % begin) == 0)
        {
            flag = 0;
            break;
        }

    }

    if (flag != 0)
        printf("������");
    else
        printf("��������");

    return 0;
}
