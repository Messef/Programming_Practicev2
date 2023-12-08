#include <iostream>
#include <vector>
#include <string>
bool checkWin(std::vector<char> game, char letter, int move) {
    if ((game[0] == letter && game[3] == letter && game[6] == letter) || (game[1] == letter && game[4] == letter && game[7] == letter) || (game[2] == letter && game[5] == letter && game[8] == letter)) {
        return true;
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

void makeMove(std::vector<char> &game, int move, char letter) {
    if (game[move] == ' ' || game[move] == 'T') {
    game[move] = letter;
    //std::cout<<"makeMove was called here asw" << std::endl;
    //std::cout<< game[move] << std::endl;

    } else {
        int myMove;
        std::cout<< "Choose a number 1-8: ";
        std::cin>>myMove;
        makeMove(game, myMove, letter);
    }

    //std::cout<<"makeMove was called" << std::endl;


}


void displayBoard(std::vector<char> game) {
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
        //std:: cout << row*3+col;
        std::cout<<"|" << game[row*3+col] << "|";
        }
        std::cout << std::endl;
    }
    /*for (int i = 0; i<9; i++) {
        std::cout<<game[i] << std::endl;
    }*/
}
bool checkTie(std::vector<char> game) {
    int counter = 0;
    for (char a: game) {

        if (a != ' ')  {
            counter++;
        }
    }
    if (counter == 9) {
        return true;
    }
    else {
        return false;
    }
}

