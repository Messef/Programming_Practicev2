#include <iostream>
#include <vector>
#include <string>
bool checkWin(std::vector<char> game, char letter, int move) {
    int correct;
    int colCheck[4] = {-3, 3, -6, 6};
    for (int i = 0; i < 4; i++) {
        if ((colCheck[i] + move) < 9 &&  (colCheck[i] + move) > 0) {
            int checker = colCheck[i] + move;
            if (game[checker] == letter) {
                correct++;

            }
       }

    }
    if (game[0] == letter && game[1] == letter && game[2] == letter) {
            return true;
        } else if (game[3] == letter && game[4] == letter && game[5] == letter) {
            return true;
            } else if (game[6] == letter && game[7] == letter && game[8] == letter) {
            return true;
                }
    if (game[0] == letter && game [4] == letter && game [8] == letter) {
        return true;
    } else if (game[2] == letter && game [4] == letter && game [6] == letter) {
        return true;
    }
    
    return false;
}

void makeMove(std::vector<char> game, int move, char letter) {
    if (game[move] == ' ' ) {
    game[move] = letter;
    std::cout<<"makeMove was called here asw";
    std::cout<< game[move];

    }
    std::cout<<"makeMove was called" << std::endl;


}


void displayBoard(std::vector<char> game) {
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
        std::cout<<"|" << game[row*3+col] << "|";
        }
        std::cout << std::endl;
    }
}

