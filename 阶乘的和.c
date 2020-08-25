#include <stdio.h>
main()
{
	int i,n;
	long s=0,t=1;
	printf("ÇëÊäÈëÊı×Ö£º\n");
	scanf("%d",&n);
	for (i=1;i<=n;i++)
	{
		t=t*i;
		s=s+t;
	}
	printf("1!+2!+3!...+%d!=%ld\n",n,s);
	system("pause");
}
