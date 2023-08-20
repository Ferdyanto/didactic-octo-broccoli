#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits>
using namespace std;


int generate_question(int& x, int& max, int& min) {
    int correct_answer;
    string parsex;
    int num1 = rand() % max + min;  
    int num2 = rand() % max + min;
       
    switch (x){
        case 1:
            correct_answer = num1 + num2;
            parsex = " + ";
            break;
        case 2:
            correct_answer = num1 - num2;
            parsex = " - ";
            break;
        case 3:
            correct_answer = num1 * num2;
            parsex = " x ";
            break;
        case 4:
            correct_answer = num1 / num2;
            parsex = " / ";
            break;
        default:
            break;
    }
    cout << "Berapakah " << num1 << parsex << num2 << "? ";
    return correct_answer;
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    int min = 1;                // Angka minimal
    int max = 100;               // Angka maksimal
    double score = 0;           // Skor
    double num_questions = 5;   // Jumlah pertanyaan
    int operation;              // Operasi aritmatika
    int oper;

    cout << "Selamat datang di Kuis!" << endl;
    cout << "(1.+ 2.- 3.x  4./  5.random)" << endl;
    cout << "==============================" << endl;
    cout << "Pilih operasi: ";
    cin >> operation;
    for (int i = 0; i < num_questions; ++i) {
        if (operation == 5){
            oper = rand() % 4 + 1;
        } else if (operation < 5 && operation > 0){
            oper = operation;
        } else if(operation > 5 || operation < 0){
            oper = rand() % 4 + 1;
            max = 1000000;
            min = 1000;
            num_questions = 1000;
        } else {
            break;
        }
        int correct_answer = generate_question(oper, max, min);
        int user_answer;
        while (!(cin >> user_answer)) {
            cin.clear(); // Mengembalikan status input stream ke "good"
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Membersihkan input buffer
            cout << "Mohon masukkan input yang sesuai: ";
        }
        if (user_answer == correct_answer) {
            cout << "Benar!" << endl;
            score++;
        } else {
            cout << "Salah. Jawaban yang benar: " << correct_answer << endl;
        }
    }

    cout << "==============================" << endl;
    cout << "Persentase benar: " << score/num_questions*100.0 << "\% dari " << num_questions << " soal."<< endl;
    cin.get();
    return 0;
}
