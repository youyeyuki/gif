/*
 时间 2015/7/30 22:34
 功能 判断素数的方法之一 

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
        printf("是素数");
    else
        printf("不是素数");

    return 0;
}
