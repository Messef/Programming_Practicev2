#include <iostream>
#include <vector>
void change_value(std::vector<int>* v) {
  (*v)[0] = 10;
}
int main() {
std::cout<< "Hello world!" << std::endl;
}