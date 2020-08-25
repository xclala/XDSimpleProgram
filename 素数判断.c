#include <stdio.h>
#include <math.h>
main(){
    int m; 
    int i; 
    int k;   
    printf("输入一个整数：");
    scanf("%d",&m);
    k=(int)sqrt( (double)m );
    for(i=2;i<=k;i++)
        if(m%i==0)
            break; 
    if(i>k){
        printf("%d是素数。\n",m);
        system("pause");
        }
    else{
        printf("%d不是素数。\n",m);
        system("pause");
        }
}
