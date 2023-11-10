#include <iostream>

int main() {
  // Add your code below  
  double weight;
 std::cout<<"weight of an item? " <<std::endl;
std::cin>>weight;
double dist;
 std::cout<<"distance in miles? " <<std::endl;
std::cin>>dist;
std::cout << "obj would weight: " << .38 * weight << std::endl;
std::cout << "miles to km: " << dist * 1.609 << std::endl;
return 0;
}