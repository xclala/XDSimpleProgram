#include <windows.h>
int main(int argc, char *argv[])
{
    ShowWindow(FindWindow("ConsoleWindowClass", argv[0]), 0);
    ShellExecute(NULL, "open", "https://www.jianshu.com/p/6049f23ee204", NULL, NULL, SW_SHOWNORMAL); //不要忘了http或https
    return 0;
}
