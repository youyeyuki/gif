#include <stdio.h>
#include <string.h>

int main()
{
	int num,i;
	char str[20];
	scanf("%d", &num);
	itoa(num, str, 10);
	printf("%s\n", str);
	for(i = 0; i < 3; i++)
		printf("%c\n", str[i]);
	char str2[255];
	sprintf(str2, "%x", 100); //将100转为16进制表示的字符串。
	printf("%s", str2);
	return 0;
}
