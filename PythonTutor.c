#include<windows.h>
int main(int argc,char *argv[])
{
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","https://blog.csdn.net/xiemanR/article/details/78237171",NULL,NULL,SW_SHOWNORMAL);
	return 0;
}