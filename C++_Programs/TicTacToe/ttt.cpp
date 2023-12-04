#include <iostream>
#include "tttf.cpp"
using namespace std;
std::vector<char> game;
char side = 'X';
int main() {
for (int i = 0; i<9; i++) {
    game.push_back(' ');
    //std::cout << "here" << std::endl;
}
int move;
while (checkWin(game, side, move) == false) {
    std::cout<< "Choose a number 1-8: ";
    std::cin>>move;
    std::cout << move << std::endl;
    makeMove(game, move, side);
    /*for (int i = 0; i<9; i++) {
        std::cout<<game[i] << std::endl;
    }*/
    displayBoard(game);
    
    checkWin(game, side, move);
    if (side == 'X') {
        side = 'O';
    } else {
        side = 'X';
    }



}
if (side == 'X') {  
    std::cout << "O wins";
    } else if (side == 'O') {
        std::cout << "X wins";
    } else {
        std::cout << "tie";
    }


}

