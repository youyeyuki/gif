#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc 包含在系统函数库里面

void f(int *p){
	*p = 66;
	pfi(*p);
}
main(){
	int *p;
	
	int i =5;
	p = &i;
	f(&i);
}
