#include <iostream>
#include <cmath>
using namespace std;

struct n{
    const double PI = 3.14159;
    double w, x, y;
    string a, b, c[3];
     /* 
    double power(double basis, double eksponen){
        double res = 1;
        for (int i = 0; i < eksponen; i++){
            res *= basis;
        }
        return res;
    }*/
    void tunggu(char* ptr){
        cout <<"\nmasukkan apa saja atau 'q' untuk keluar..";
        cin >> *ptr;
    }
    double lingkaran(double& r){ // dengan reference
        return PI*pow(r,2);
    }
    double segitiga(double* ptr, double* prt){ //dengan pointer
        return 0.5*(*ptr)*(*prt);
    }
    double persegi(double& sisi){
        return pow(sisi, 2);
    }
    double psg_panjang(double& pjg, double& lbr){ 
        return pjg*lbr;
    }
    double trapesium(double& atas, double& bawah, double* tinggi){
        return 0.5*(atas+bawah)*(*tinggi);
    }
};

int main() {
    n a;
    int act;
    char dummy;
    a.a = "----------------Penghitung Luas----------------\n";
    a.b = "-----------------------------------------------\n";
    a.c[0] = "1.segitiga   |   4.persegi panjang\n";
    a.c[1] = "2.lingkaran  |   5.trapesium\n";
    a.c[2] = "3.persegi    |   (0) untuk keluar";

    while (true){
        do {
            cout << a.a;
            for (int i=0; i<size(a.c);i++){
                cout << a.c[i];
            }
            cin >> act;
        } while (act<0 || act>5);
        cout << "\x1B[2J\x1B[H"; // ANSI escape sequence untuk cls layar
        cout << a.a;

        switch (act){
            case 0:
                break;
            case 1:
                cout << "Masukkan panjang segitiga: ";
                cin >> a.x;
                cout << "Masukkan lebar segitiga: ";
                cin >> a.y;
                cout << "Luas segitiga: " << a.segitiga(&a.x, &a.y) << endl;
                a.tunggu(&dummy);
                break;
            case 2:
                cout << "Masukkan radius lingkaran: ";
                cin >> a.w;
                cout << "Luas lingkaran: " << a.lingkaran(a.w)<< endl;
                a.tunggu(&dummy);
                break;
            case 3:
                cout << "Masukkan sisi persegi; ";
                cin >> a.x;
                cout << "Luas persegi: " << a.persegi(a.x) << endl;
                a.tunggu(&dummy);
                break;
            case 4:
                cout << "Masukkan panjang persegi panjang: ";
                cin >> a.x;
                cout << "Masukkan lebar persegi panjang: ";
                cin >> a.y;
                cout << "Luas persegi panjang: " << a.psg_panjang(a.x, a.y) << endl;
                a.tunggu(&dummy);
                break;
            case 5:
                cout << "Masukkan sisi atas: ";
                cin >> a.x;
                cout << "Masukkan sisi bawah: ";
                cin >> a.y;
                cout << "Masukkan tinggi: ";
                cin >> a.w;
                cout << "Luas trapesium: " << a.trapesium(a.x, a.y, &a.w);
                a.tunggu(&dummy);
                break;
        }
        if (dummy=='q' || act==0){break;}
        cout << "\x1B[2J\x1B[H";
    }
    cout << a.b;
    system("pause");
    return 0;
}