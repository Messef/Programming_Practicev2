#include <iostream>
#include "tttf.cpp"
std::vector<char> game;
char side = 'X';
int main() {
for (int i = 0; i<9; i++) {
    game.push_back(' ');
}
int move;
while (checkWin(game, side, move) == false) {
    std::cout<< "Choose a number 1-8: ";
    std::cin>>move;
    makeMove(game, move, side);
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
    } else {
        std::cout << "X wins";
    }


}

