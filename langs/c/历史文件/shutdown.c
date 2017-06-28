#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isnum(int num);
void runSysCommand(int select, int time );

	
int main()
{
	printf("218专用自动关机程序.......\n");
	printf("1.自动关机\n\n2.取消自动关机\n\n请输入你要执行的动作\n");
	 
	int i, time, flag = 0;
	switch (scanf("%d", &i)){
		case 1 : {
			printf("请输入关机的分钟数");
			scanf("%d", &time);
			flag = isnum(time);
			
			if(flag){
				time =time * 60;
				runSysCommand(time);
			}
			   
			break;
		}
			
		default : printf("输入错误了吧23333333\n"); 
	}
	
	 return 0;
}

int isnum(int num){
 
int count = 0; int a[30],i,flag = 1;
while(num!=0){
	a[count] = num % 10;
	num = num / 10;
	count++; 
}
	int *arry = (int*)malloc(count*sizeof(int));
	for(i = 0 ; i < count; i++)
	     arry[i] = a[i];
//
    i = 0;//再次初始化i 
	while(i < count){
		if(0<= arry[i] <=9)
		     printf("%d", arry[i]);
	     else{
	     	flag = 0;
	     	break;
	     }
	     i++;
	}
	return flag;
}
void runSysCommand(int time){
	
	char c[100]= "shutdown -s -t ",time_str[10];
	itoa(time, time_str, 10);
	strcat(c, time_str);
	system(c);

}
