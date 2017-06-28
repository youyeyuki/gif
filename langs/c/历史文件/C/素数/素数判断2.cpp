#include <stdio.h>
bool IsPrime(int val)
{
    int i;
    for(i = 2; i < val ; i++)
    {
        if (val % i == 0)
            break;
    }


    if(val == i)
        return true;
    else
        return false;


}

int main()
{
    int val;
    bool jump;
    printf("请输入一个要判断的素数\n");
    scanf("%d", &val);
    jump = IsPrime(val);

    if(jump)
        printf("是素数");
    else
        printf("不是素数");

    return 0;
}

