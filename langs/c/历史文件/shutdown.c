#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isnum(int num);
void runSysCommand(int select, int time );

	
int main()
{
	printf("218ר���Զ��ػ�����.......\n");
	printf("1.�Զ��ػ�\n\n2.ȡ���Զ��ػ�\n\n��������Ҫִ�еĶ���\n");
	 
	int i, time, flag = 0;
	switch (scanf("%d", &i)){
		case 1 : {
			printf("������ػ��ķ�����");
			scanf("%d", &time);
			flag = isnum(time);
			
			if(flag){
				time =time * 60;
				runSysCommand(time);
			}
			   
			break;
		}
			
		default : printf("��������˰�23333333\n"); 
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
    i = 0;//�ٴγ�ʼ��i 
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
