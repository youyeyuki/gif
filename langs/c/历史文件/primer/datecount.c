#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define  true 1
#define  false 0
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc 包含在系统函数库里面
#include <windows.h>
#include <string.h>

#define MONTHS 13
main(){
	int sleep_time;

	int DAY[MONTHS]={0,31,28,31,30,31,30,31,31,30,31,30,31}; //闰年多一天 设置为13方便计算阅读
    int year = 1970 ,month =1, day =1,showday,showyear,showmonth;
	int toyear,tomonth,today,initmonth,initday,flag = 0;
	int count= 0,i,j;

	printf("输入开始的日期 例如 2010 1 1 \n");
	scanf("%d%d%d",&year,&month,&day);
	printf("输入结束的日期 例如 2012 2 1\n");
	scanf("%d%d%d",&toyear,&tomonth,&today);
	printf("输入每次打印出来的时间 例如 30  表示30ms \n");
	scanf("%d",&sleep_time);
	showyear = year; showmonth = month; showday =day;
	initmonth = month;
	initday = day;
	for(i = year; i <= toyear; i++,year++){
		if(((year % 4 == 0 && year % 100 != 0) ||(year % 400 ==0))&&(year < toyear)){
			count++;
			printf("跨年闰年认证\n");
		//以上是跨年判断
		}

		if(((year % 4 == 0 && year % 100 != 0) || (year % 400 ==0))&&(year == toyear)&&(tomonth >2)){
			count++;
			printf("最后一年闰年认证\n");
			//以上 是同年比较加上1
		}

		if(year == toyear){
			for(j = initmonth; j <= tomonth; j++){
				for(day = initday; day <=DAY[j];day++){
					count++; printf("%d-%d-%d到%d-%d-%2d 已经过了%d天\n",showyear,showmonth,showday,year,j,day,count-1);Sleep(sleep_time);
					if(j == tomonth && day == today)
					break;
				}
				initmonth = 1;
				initday = 1;
			}//day 循环
		}else{
		flag = 1;
    for(j = initmonth;j <= 12;j++){
			for(day = initday; day <=DAY[j];day++){
				count++; printf("%d-%d-%d到%d-%d-%2d 已经过了%d天\n",showyear,showmonth,showday,year,j,day,count-1);Sleep(sleep_time);
			}
			initmonth = 1;
			initday = 1; //每月后初始化为1
		}  //默认十二月循环
	}

	}
	pfi(count-1); //最后要减去一天 因为计算的是从开始到结束 而不是之间的日期
	system("pause");
}
