#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define max 10
double operate(double a,double b,char ch) //运算操作
{
if(ch=='+')
return a+b;
else if(ch=='-')
return a-b;
else if(ch=='/')
return a/b;
else if(ch=='*')
return a*b;
else
return 0;
}
int precede(char a,char b) //判断优先级
{
if(a=='+'||a=='-')
{
if(b=='*'||b=='/')
return 1;
if(b=='+'||b=='-')
return 0;
}
if(a=='*'||a=='/')
return 0;
return 0;
}
int check(double A,double B,double C,double D)
{
int i,j,k;
char d[4]={'+','-','*','/'};
double a[max],b[max][max],c[max][max][max];
for(i=0;i<4;i++)
a[i]=operate(A,B,d[i]);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
b[i][j]=operate(a[i],C,d[j]);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
for(k=0;k<4;k++)
c[i][j][k]=operate(b[i][j],D,d[k]);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
for(k=0;k<4;k++)
{
if(c[i][j][k]==24.0)
return 1;
}
return 0;
}
void SHOW(double A,double B,double C,double D)
{
 int i,j,k;
 char d[4]={'+','-','*','/'};
 double a[max],b[max][max],c[max][max][max];
 for(i=0;i<4;i++)
a[i]=operate(A,B,d[i]);
for(i=0;i<4;i++)
 for(j=0;j<4;j++)
b[i][j]=operate(a[i],C,d[j]);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
for(k=0;k<4;k++)
c[i][j][k]=operate(b[i][j],D,d[k]);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
for(k=0;k<4;k++)
{
if(c[i][j][k]==24.0)
{
if(precede(d[i],d[j]))
{
printf("(%.0f%c%.0f)%c%.0f%c%.0f",A,d[i],B,d[j],C,d[k],D);
printf("\n");
}
else if(precede(d[j],d[k]))
{
printf("(%.0f%c%.0f%c%.0f)%c%.0f",A,d[i],B,d[j],C,d[k],D);
printf("\n");
}
else
{
printf("%.0f%c%.0f%c%.0f%c%.0f",A,d[i],B,d[j],C,d[k],D);
printf("\n");
}
}
}
}
void game_24()
{
 double A=0,B=0,C=0,D=0;
 char j;
 char d[4]={'+','-','*','/'};
 srand((unsigned)time(NULL));
 while(1)
 {
while((A==0||B==0)||(C==0||D==0))
{
A=rand()%10*1.0;
 B=rand()%10*1.0;
C=rand()%10*1.0;
D=rand()%10*1.0;
}
if((check(A,B,C,D)||check(B,C,A,D))||(check(C,B,D,A)||check(D,A,B,C)))
 break;
else
{
A=0;
B=0;
C=0;
D=0;
}
}
 printf("%.0f %.0f %.0f %.0f\n",A,B,C,D);
 printf("是否要看答案(y/n):");
 while(1)
{
scanf("%s",&j);
if(j=='y'||j=='Y')
{ SHOW(A,B,C,D);
SHOW(A,B,D,C);
SHOW(A,D,B,C);
SHOW(A,D,C,B);
SHOW(A,C,B,D);
SHOW(A,C,D,B);
SHOW(B,A,C,D);
SHOW(B,A,D,C);
SHOW(B,C,A,D);
SHOW(B,C,D,A);
SHOW(B,D,A,C);
SHOW(B,D,C,A);
SHOW(C,A,B,D);
SHOW(C,A,D,B);
SHOW(C,B,A,D);
SHOW(C,B,D,A);
SHOW(C,D,A,B);
SHOW(C,D,B,A);
SHOW(D,A,B,C);
SHOW(D,A,C,B);
SHOW(D,B,A,C);
SHOW(D,B,C,A);
SHOW(D,C,A,B);
SHOW(D,C,B,A);
break;
}
else
printf("我知道你试不出，看答案吧(y/n):");
}
}
void menu()
{
int i;
while(1)
{
system("cls");
printf("***********************\n");
printf("\n");
printf("智力游戏24点\n");
printf("\n");
printf("1.开始游戏\n");
printf("2.游戏规则\n");
printf("3.退出游戏\n");
printf("\n");
printf("你敢来挑战吗？\n");
printf("***********************\n");
printf("输入你的选择:");
scanf("%d",&i);
if(i==3)
break;
switch(i)
{
case 1:
game_24();
system("PAUSE");
break;
case 2:
printf("给你4个数,运用加减乘除括号等操作使结果为24\n");
system("PAUSE");
break;
default:
printf("error input\n");
system("PAUSE");
}
}
}
int main()
{
menu();
return 0;
}

