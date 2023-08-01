#include <iostream>
#include <cctype>
#include <limits>
using namespace std;

double celcius(char* skala, double& n){
    double hasil = 0;
    switch (*skala){
        case 'C':
            hasil = n;
            break;
        case 'R':
            hasil = 5/4*n;
            break;
        case 'F':
            hasil = 5/9*(n-32);
            break;
        case 'K':
            hasil = n-273;
            break;
        default:
            break;
    }
    return hasil;
}
double reamur(char* skala, double& n){
    double hasil = 0;
    switch (*skala){
        case 'C':
            hasil = 4/5*n;
            break;
        case 'R':
            hasil = n;
            break;
        case 'F':
            hasil = 4/9*(n-32);
            break;
        case 'K':
            hasil = 4/5*(n-273);
            break;
        default:
            break;
    }
    return hasil;
}
double fahrenheit(char* skala, double& n){
    double hasil = 0;
    switch (*skala){
        case 'C':
            hasil = 9/5*n+32;
            break;
        case 'R':
            hasil = 9/4*n+32;
            break;
        case 'F':
            hasil = n;
            break;
        case 'K':
            hasil = 9/5*(n-273)+32;
            break;
        default:
            break;
    }
    return hasil;
}
double kelvin(char* skala, double& n){
    double hasil = 0;
    switch (*skala){
        case 'C':
            hasil = n+273;
            break;
        case 'R':
            hasil = 5/4*n+273;
            break;
        case 'F':
            hasil = 5/9*(n-32)+273;
            break;
        case 'K':
            hasil = n;
            break;
        default:
            break;
    }
    return hasil;
}


int main(){
    char skir, skal, quit;
    auto n = 1.0;
    string header = "---------Konversi Suhu---------\n";
    string footer = "-------------------------------\n";

    do {
        cout << header << "1. C    2. R    3. F    4. K\n";
        cout << "\nMasukkan suhu: "; //Input suhu
        while (!(cin >> n)) {
            cin.clear(); // Mengembalikan status input stream ke "good"
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Membersihkan input buffer
            cout << "Masukkan suhu: ";
        }
        //Input skala awal dari suhu
        do{
            cout << "Skala awal: ";
            cin >> skal;
            if (toupper(skal)=='C' || skal=='1'){
                skal = 'C';
            } else if (toupper(skal)=='R' || skal=='2'){
                skal = 'R';
            } else if (toupper(skal)=='F' || skal=='3'){
                skal = 'F';
            } else if (toupper(skal)=='K' || skal=='4'){
                skal = 'K';
            } else{
                skal = 'o';
            }
        } while (skal=='o');
        //Input skala tujuan konversi
        skir = 'o';
        while (skir=='o'){
            cout << "Skala akhir: ";
            cin >> skir;
            if (toupper(skir)=='C' || skir=='1'){
                cout << n << " " << skal << " ==> " << celcius(&skal, n) << " C\n";
            } else if (toupper(skir)=='R' || skir=='2'){
                cout << n << " " << skal << " ==> " << reamur(&skal, n) << " R\n";
            } else if (toupper(skir)=='F' || skir=='3'){
                cout << n << " " << skal << " ==> " << fahrenheit(&skal, n) << " F\n";
            } else if (toupper(skir)=='K' || skir=='4'){
                cout << n << " " << skal << " ==> " << kelvin(&skal, n) << " K\n";
            } else{
                skir = 'o';
            }
        }
        //Keluar
        cout << footer << "\ntekan (q) untuk keluar ";
        cin >> quit;
        system("cls");
    }while (tolower(quit)!='q');

    return 0;
}