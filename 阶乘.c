#include <stdio.h>
int factorial(int n)
{
	if (n==0 || n==2)
	return n;
	else return n*factorial(n-1);
}
main()
{
	int n;
	long y;
	printf("ÇëÊäÈëÊı×Ö£º\n");
	scanf ("%d",&n);
	y=factorial(n);
	printf("%d!=%ld\n",n,y);
	system("pause");
}
