#include<windows.h>
int main(int argc,char *argv[])
{
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","http://www.beijing-time.org/shiqu/",NULL,NULL,SW_SHOWNORMAL);//不要忘了http或https
	return 0;
}
