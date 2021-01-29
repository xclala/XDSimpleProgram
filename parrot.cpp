#include <iostream>
#include <string>
using namespace std;
int main(){
	string m;
	for(;;){
		cout << "输入任何，我重复(输入“ctrl+c”结束程序)：";
		cin >> m;
		cout << m << endl;
	}
	return 0;
}
