#include<windows.h>
int main(int argc,char *argv[])
{
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","https://blog.csdn.net/sinat_31580685/article/details/93011227",NULL,NULL,SW_SHOWNORMAL);
	return 0;
}




