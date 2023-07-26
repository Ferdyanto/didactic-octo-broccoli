#include <iostream>
using namespace std;

int main(){
    int m,n,r,fpb;
    do {
        cin >> m;
        cin >> n;
    } while (m<n);
    r = m%n;
    if (r==0) fpb = n;
    else{
        while (r!=0){
            m = n;
            n = r;
            r = m%n;
            fpb = n;
        }
    }
    cout << "FPB: " << fpb << endl;
    return 0;
}