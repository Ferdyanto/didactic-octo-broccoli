#include <iostream>

struct myClass{
    short x, y;
    char b;
    double operate(double n1, double n2, char x){
        b = x;
        double hasil;
        /* if (b == '/'){
            hasil = n1/n2;
        } else if (b == 'x' | b == '*'){
            hasil = n1*n2;
        } else if (b == '+'){
            hasil = n1+n2;
        } else if (b == '-'){
            hasil = n1-n2;
        } */
        switch (b){
            case '/':
                hasil = n1/n2;
                break;
            case 'x':
                hasil = n1*n2;
                break;
            case '*':
                hasil = n1*n2;
                break;
            case '+':
                hasil = n1+n2;
                break;
            case '-':
                hasil = n1-n2;
                break;
        }
        return hasil;
    }
    void out(int n1, int n2, double n3){
        std::cout << n1 << b << n2 << " = " << n3 << std::endl;
    }
};

int main(){
    myClass k;
    char con;
    while (true){
        std::cout << "Ini adalah kalkulator" << std::endl;
        std::cout << "angka pertama : ";
        std::cin >> k.x;
        std::cout << "angka kedua : ";
        std::cin >> k.y;
        std::cout << "operasi: ";
        std::cin >> k.b;
        k.out(k.x, k.y, k.operate(k.x, k.y, k.b));
        std::cout << "Apakah anda ingin keluar?(q) ";
        std::cin >> con;
        if (con == 'q'){
            std::cout << "\033[2J";
            break;
        }
    }
    return 0; 
}