#include<windows.h>
int main(int argc,char *argv[])
{
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","https://weibo.com/u/3325704142?topnav=1&wvr=6&topsug=1&is_all=1",NULL,NULL,SW_SHOWNORMAL);//不要忘了http或https
	return 0;
}
