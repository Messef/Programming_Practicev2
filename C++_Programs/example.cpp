#include <iostream>
#include <vector>

int main() {
  std::vector<int> challenge;
  challenge.push_back(2);
  challenge.push_back(4);
  challenge.push_back(3);
  challenge.push_back(6);
  challenge.push_back(1);
  challenge.push_back(9);
  int even;
  int odd = 1;
  for (int i = 0; i<challenge.size(); i++) {
    if (challenge[i]%2==0) {
      even+=challenge[i];
    } else {

      odd*=challenge[i];
    }
  }
  std:: cout<< "Sum of all even nums: " << even << std::endl;
  std:: cout<< "Product of all odd nums: " << odd << std::endl;
  return 0;

}