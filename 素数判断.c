#include <stdio.h>
#include <math.h>
main(){
    int m; 
    int i; 
    int k;   
    printf("����һ��������");
    scanf("%d",&m);
    k=(int)sqrt( (double)m );
    for(i=2;i<=k;i++)
        if(m%i==0)
            break; 
    if(i>k){
        printf("%d��������\n",m);
        system("pause");
        }
    else{
        printf("%d����������\n",m);
        system("pause");
        }
}
