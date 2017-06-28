#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define NUM 1000000007

int dp[110][110];

int main(){
	
	int k, l;
	int i, j, m;
	int sum;
	
	scanf("%d %d", &k, &l);
	for(i = 0; i < k; i++){
		dp[1][i] = 1;
		pfi(dp[1][i]);
		
	}
	
	for(i = 2; i <= l; i++){
		for(j = 0; j < k; j++){
			for(m = 0; m < k; m++){
				if(abs(m - j) != 1){
					dp[i][j] = (dp[i][j] + dp[i - 1][m]) % NUM;
					pfi(dp[1][i]);
				}
			}
		}
	}	
	
	sum = 0;
	for(i = 1; i < k; i++){
		sum = (sum + dp[l][i]) % NUM;
	}
	
	printf("%d\n", sum);
	
	return 0;
}

