#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define  true 1
#define  false 0
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc ������ϵͳ����������
#include <windows.h>
#include <string.h>

#define MONTHS 13
main(){
	int sleep_time;

	int DAY[MONTHS]={0,31,28,31,30,31,30,31,31,30,31,30,31}; //�����һ�� ����Ϊ13��������Ķ�
    int year = 1970 ,month =1, day =1,showday,showyear,showmonth;
	int toyear,tomonth,today,initmonth,initday,flag = 0;
	int count= 0,i,j;

	printf("���뿪ʼ������ ���� 2010 1 1 \n");
	scanf("%d%d%d",&year,&month,&day);
	printf("������������� ���� 2012 2 1\n");
	scanf("%d%d%d",&toyear,&tomonth,&today);
	printf("����ÿ�δ�ӡ������ʱ�� ���� 30  ��ʾ30ms \n");
	scanf("%d",&sleep_time);
	showyear = year; showmonth = month; showday =day;
	initmonth = month;
	initday = day;
	for(i = year; i <= toyear; i++,year++){
		if(((year % 4 == 0 && year % 100 != 0) ||(year % 400 ==0))&&(year < toyear)){
			count++;
			printf("����������֤\n");
		//�����ǿ����ж�
		}

		if(((year % 4 == 0 && year % 100 != 0) || (year % 400 ==0))&&(year == toyear)&&(tomonth >2)){
			count++;
			printf("���һ��������֤\n");
			//���� ��ͬ��Ƚϼ���1
		}

		if(year == toyear){
			for(j = initmonth; j <= tomonth; j++){
				for(day = initday; day <=DAY[j];day++){
					count++; printf("%d-%d-%d��%d-%d-%2d �Ѿ�����%d��\n",showyear,showmonth,showday,year,j,day,count-1);Sleep(sleep_time);
					if(j == tomonth && day == today)
					break;
				}
				initmonth = 1;
				initday = 1;
			}//day ѭ��
		}else{
		flag = 1;
    for(j = initmonth;j <= 12;j++){
			for(day = initday; day <=DAY[j];day++){
				count++; printf("%d-%d-%d��%d-%d-%2d �Ѿ�����%d��\n",showyear,showmonth,showday,year,j,day,count-1);Sleep(sleep_time);
			}
			initmonth = 1;
			initday = 1; //ÿ�º��ʼ��Ϊ1
		}  //Ĭ��ʮ����ѭ��
	}

	}
	pfi(count-1); //���Ҫ��ȥһ�� ��Ϊ������Ǵӿ�ʼ������ ������֮�������
	system("pause");
}
