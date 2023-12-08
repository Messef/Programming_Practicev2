#include <iostream>
#include "tttf.cpp"
using namespace std;
std::vector<char> game;
char side = 'O';
int main() {
for (int i = 0; i<9; i++) {
    game.push_back(' ');
    //std::cout << "here" << std::endl;
}
int move;
while (checkWin(game, side, move) == 0 && checkTie(game) == 0) {
    if (side == 'X') {
        side = 'O';
    } else {
        side = 'X';
    }
    std::cout<< "Choose a number 1-8: ";
    std::cin>>move;
    makeMove(game, move, side);
    /*for (int i = 0; i<9; i++) {
        std::cout<<game[i] << std::endl;
    }*/
    displayBoard(game);
    
    checkWin(game, side, move);



}
if (side == 'O' && checkTie(game) == 0) {  
    std::cout << "O wins" << std::endl;
    } else if (side == 'X' && checkTie(game) == 0) {
        std::cout << "X wins" << std::endl;
    } else {
        std::cout << "tie" << std::endl;
    }


}

