/*

author:wings
fuction:2 trans 10
first find some error: while condition use while(1 == b) this is a bit misstake  It must loop condition while(1 != b)
test 10  2 1010

*/


#include<stdio.h>

int main()
{
    int _a[20];

    int b = 10;
    int count = 0;
    do
    {
        if (b < 2) break;

        _a[count] = b % 2 ;
        b = b / 2 ;
        count ++ ;
        if(b == 1)
        {
            _a[count] = b;
        }

    }
    while(1 != b);
    
    int pf;
    for (pf = count; pf > -1 ; pf--)
    {
        printf("%d", _a[pf]);
    }
    return 0;
}
