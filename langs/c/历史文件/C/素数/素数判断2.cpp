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
    printf("������һ��Ҫ�жϵ�����\n");
    scanf("%d", &val);
    jump = IsPrime(val);

    if(jump)
        printf("������");
    else
        printf("��������");

    return 0;
}

