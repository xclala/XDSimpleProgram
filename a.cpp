#include <iostream>
#include <string>
using namespace std;
int main(){
    string m;
    cout << "你需要一直显示什么？(“ctrl+c”退出)";
    cin >> m;
    for(;;){
        cout << m << endl;
    }
    return 0;
}
