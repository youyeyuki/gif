#include <stdlib.h>
#include <string.h>
#include <windows.h>

void ex_3_5(){
	int s = 3.156*pow(10,7);
	int old;
	scanf("%d",&old);
	s = s * old;
	pfi(s);
}

void ex_3_1(){
		float num = 2.200;
	printf("%e",num);
}
void string_link()
{
	printf("the first string \
	ffffffff");
	//通过 \ 连接下一个字符串
}
void jump_two_copy_three(){
	int n;
	scanf("%*d %*d %d",&n);// %*d 跳过该赋值
	pfi(n);
}
void  order(){
	int n = 12;
	pfi(n/3*2);
}
void min_to_sec(){
	#define  SEC_PRE_MIN 60
	int sec,min,left;
	printf("convert seconds to minutes and seconds!\n");
	printf("enter the number of seconds (< =0 to quit)\n");
	scanf("%d",&sec);
	while(sec > 0){
		min = sec / SEC_PRE_MIN;
		left = sec % SEC_PRE_MIN;
		printf("%d seconds is %d minutes %d seconds !\n",sec ,min,left);
		scanf("%d",&sec);

	}
	printf("DONE!\n");
}
void add_one(){
	int i =1;
	while(++i < 10){ //i 的值先增加1 再和 10比较  最后一个使用10 和 10 比较最后 输出的是9
		pfi(i);

	}
	int j = 1;
	while(j++ < 10){ //使用 j =1 比较 后加上1  最后一个 使用9 比较后加上1 输出的是10
		pfi(j);

	}
}

void min_to_sec2(){
	#define  SEC_PRE_MIN 60
	int sec = 5,min,left; //sec 赋值为5 保证第一次能进入循环
	printf("convert seconds to minutes and seconds!\n");
	printf("enter the number of seconds (< =0 to quit)\n");
	while(sec > 0){
		scanf("%d",&sec); //循环后继续循赋值
		min = sec / SEC_PRE_MIN;
		left = sec % SEC_PRE_MIN;
		printf("%d seconds is %d minutes %d seconds !\n",sec ,min,left);
		printf("next num?\n");
		//但是这样退出的时候不能及时退出还是会计算 0时候的值

	}
	printf("DONE!\n");
}

void ex_5(){
	int num = 10;
	pfi(++num);
	pfi(num++);
	pfi(num--);
	pfi(num);
}
void ex_9(){
	int x = 100;
	while(x++ < 103){ //使用103比较不成功 但是使用完后还是会加上1
		pfi(x);
	}
	pfi(x);//104
}

void min_to_hours_sec(){
 #define MIN_PRE_HOUR 60
 int min,left,hour;
 scanf("%d",&min);
 printf("convert minutes to hours and minutes!\n");
	printf("enter the number of minutes (< =0 to quit)\n");
 while(min > 0){
 	hour = min / MIN_PRE_HOUR;
 	left = min % MIN_PRE_HOUR;
	 printf("%d minutes is %d hour %d mintes\n",min,hour,left);
 	printf("next min  \n");
 	scanf("%d",&min);
 }
 printf("done!\n");
}
void sec_to_hour(){
	#define  SEC_PRE_MIN 60
	#define  MIN_PRE_HOUR 60
    int sec,min,hour = 0,sec_left;
    printf("输入sec数\n");
    scanf("%d",&sec);
    while(sec > 0){
     min = sec / SEC_PRE_MIN;
     sec_left = sec % SEC_PRE_MIN;
     if (min >= 60){
     	hour = min /  MIN_PRE_HOUR;
        min = min % MIN_PRE_HOUR; //更新min的值
     }
     printf("%d sec is %d hour %d min %d sec \n",sec,hour,min,sec_left);
     printf("next sec is \n");
	 scanf("%d",&sec);
    }
	printf("DONE!\n");
}

void week_to_day(){
	#define DAY_PRE_WEEK 7
	int day,week,day_left;
	printf("enter days \n");
	scanf("%d",&day); //scanf 不要加上斜杠 否者会出现不写入数据的问题
  while (day > 0) {
  	week = day / DAY_PRE_WEEK;
		day_left  = day % DAY_PRE_WEEK;
		printf("%d day are %d weeks  %d days.\n",day,week,day_left);
		printf("enter the next days\n");
    scanf("%d",&day );

	}
}
void Temperatures(){ //Celsius 摄氏温度 Fahrenheit 华氏温度
	float Celsius,kelvin,Fahrenheit;
	printf("enter Fahrenheit 华氏温度 输入q或其他字符退出\n" );
	while(scanf("%f",&Fahrenheit) == 1){
		Celsius = 1.8*Fahrenheit + 32.0;
		kelvin  = Celsius +  273.16;
		printf("摄氏温度是%10.2f\t 华氏温度是 %10.2f\t \n",Celsius,kelvin);
		printf("enter Fahrenheit 华氏温度 \n");
	}
}
void cmpflt(){
	const double ANSWER = 3.14159;
	double response;
	printf("what is the value of pi ?\n");
	scanf("%lf",&response);
	while (fabs(response - ANSWER) > 0.0001) {
	 printf("try again \n");
	 scanf("%lf",&response);
	}
}

void ex_for(){
	int x,y = 55;
	for (x = 1; y <= 75 ; y=(++x*5)+50 ) {
		printf("%10d %10d \n",x,y );
	}
}

void zone() {
	int t_ct;
	double time,x;
	int limit;
	printf("enter the number of terms you want \n");
	scanf("%d",&limit);
	for(time = 0,x =1,t_ct = 1; t_ct <= limit; t_ct++,x*=2.0){
		time += 1.0/x;
		printf("time = %f when terms =%d.\n",time,t_ct);
	//	Sleep(15);
	}

}
void printf_value(){
	int value ;
	for(value = 36; value > 0 ; value/=2){
		pfi(value);
	}
}
void printf_what(){
	int i =0;
	while(++i < 4){
		printf("Hi  ");
	}
}

void for_use(){
 int row,col;
	for(row = 1; row <= 5; row ++ ){
		for(col = 0 ;col < row ;col++)
		printf("$");
		printf("\n");
	}

}
void printf_triangle(){
	int row, character;
	for(row =1; row <=6; row++){
		for(character =0; character < row; character++){
			printf("%c",'F'-character);
		}
		printf("\n");
	}
}
void printf_triangle2(){
	char character; int row,i;
	scanf("%c",&character);
	for(row = 1; row <= 9; row+=2){
		for(i = 0; i <(9-row)/2 ;i++) printf(" ");
		for(i = 0; i < row/2+1;i++) printf("%c",character+i);
		for(i = 0; i < row/2;i++) printf("%c",row/2+character-i);
		printf("\n");
	}
}

void reverse(){
	int i; char character[50];
	scanf("%s",&character);
	for(i = strlen(character)-1; i >=0; i--)
	printf("%c", character[i]);
	printf("\n");
}
void reverse2(){
	int i,tmp,len; char s[50];
	scanf("%s",s);
	len = strlen(s);
	for(i = 0; i < len/2; i++){
		tmp = s[i];
		s[i] = s[len-i-1];
		s[len-i-1] = tmp;
	}
 for(i =0; i < len; i++){
	 printf("%c",s[i]);
 }

}


void printf_unknown(){
	int num;
	for ( num = 1; num <= 11; num++) {
	if(num %3 == 0)
	      putchar('$');
	else
	    putchar('*');

			putchar('#');

	}
	printf("\n");
}

void recur(){
	void up_and_down(int n){
		printf("Level %d n location %p\n",n,&n);
		if(n < 4)
		   up_and_down(n+1);
		printf("Level %d n location %p\n",n,&n);
	}

	up_and_down(1);

}

void swap(int *first , int *second){
	int tmp;
	tmp = *first;
	*first = *second;
	*second = tmp;

}
void date(){
	#define sleep_time 30
	#define MONTHS 13
	int DAY[MONTHS]={0,31,28,31,30,31,30,31,31,30,31,30,31}; //闰年多一天 设置为13方便计算阅读
    int year = 1970 ,month =1, day =1,showday,showyear,showmonth;
	int toyear,tomonth,today,initmonth,initday,flag = 0;
	int count= 0,i,j,k;
	printf("输入开始的日期 例如 2010 1 1 \n");
	scanf("%d%d%d",&year,&month,&day);
	printf("输入结束的日期 例如 2012 2 1\n");
	scanf("%d%d%d",&toyear,&tomonth,&today);
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
}
void point_add(){
	char *s = "I am ye jiang  i like the world and i hope can make friend with you ! ";
	 while (*(s) != '\0')
	 	putchar(*(s++));

}
void ntom(){
	#define N 10 //代转换的进制
	#define M 4 //目的进制
	int arry[100],num,len,i;

	scanf("%d",&num);
	len =num;
	for(i=0;; i++){
		 arry[i] = num % M;
		 num = num / M;
		 //printf("获取的数据%d\n",arry[i]);
		 if(num < M){
			 break;
		 }
	}
	i++;
	arry[i] = num;
	printf("%d转换是",len);
	for(;i >=0 ; i--)
	    printf("%d",arry[i]);

	    printf("\n");

}
void ntom2(int num){
	#define N 10 //代转换的进制
	#define M 4 //目的进制
	int arry[100],len,i;
	len =num;
	for(i=0;; i++){
		 arry[i] = num % M;
		 num = num / M;
		 //printf("获取的数据%d\n",arry[i]);
		 if(num < M){
			 break;
		 }
	}
	i++;
	arry[i] = num;
	printf("%d转换是",len);
	for(;i >=0 ; i--)
	 printf("%d",arry[i]);

	    printf("\n");
}
