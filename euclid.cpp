#include <iostream>
using namespace std;

int fpb(int a, int b) {
    if (b == 0) {
        return a;
    }
    return fpb(b, a % b); //rekursi
}

int kpk(int a, int b) {
    return (a * b) / fpb(a, b);
}

int main(){
    int m,n,fp,kp;
    char ask;

    //int r;
    // do {
    //     cin >> m;
    //     cin >> n;
    // } while (m<n);
    // r = m%n;
    // if (r==0) fpb = n;
    // else{
    //     while (r!=0){
    //         m = n;
    //         n = r;
    //         r = m%n;
    //         fpb = n;
    //     }
    // }

do{
    cout << "\n-----------KPK & FPB-----------\n";
    cout << "Masukkan dua bilangan: ";
    cin >> m >> n;
    cout << "Tentukan KPK atau FPB?(1/2) ";
    cin >> ask;
    fp = fpb(m,n);
    kp = kpk(m,n);
    if (ask=='1') {
        cout << "KPK: " << kp << endl;
    } else if (ask=='2'){
        cout << "FPB: " << fp << endl;
    } else if (ask=='3'){
        cout << "KPK: " << kp << endl;
        cout << "FPB: " << fp << endl;
    } else {
        cout << "Ulangi!\n";
        continue;
    }
    cout << "\nMulai lagi?(n untuk keluar)";
    cin >> ask;
} while (ask!='n');
    
    return 0;
}