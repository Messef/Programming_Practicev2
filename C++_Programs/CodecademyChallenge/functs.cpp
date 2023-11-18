#include <iostream>

std::string codeword = "codecademy";
std::string answer;
void greeting() {
    std::cout << "Welcome to password!" << std::endl;
    std::cout << "Instructions: save your friend from alien abduction by guessing the letters in the codeword." << std::endl;
    std::cout << "Good luck!" << std::endl;

}
bool gotPass(std::string password) {
    if (password == codeword) {
        return true;
    }
    return false;
}   
int main() {
int misses;
    for (int i = 0; i <codeword.length(); i++) {
  answer+="__ ";
  
}
while (!gotPass(answer) && misses<7) {
    misses++;
    std::cout << "Guess? " << std::endl;
    std::cin >>answer;

}
std::cout<<answer<<std::endl;

    return 0;
}

