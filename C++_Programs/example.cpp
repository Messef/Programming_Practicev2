#include <iostream>
#include <cmath>

int main() {
  double a;
  double b;
  double c;
  std::cout<<"a: ";
  std::cin>> a;
  std::cout<<"b: ";
  std::cin>> b;
  std::cout<<"c: ";
  std::cin>> c;
  double root2 = (-b - std::sqrt(b**2-4*a*c))/(2*a);;
  double root1 = (-b + std::sqrt(b**2-4*a*c))/(2*a);
  std::cout << "root 1 is " << root1 <<std::endl;
  std::cout << "root 2 is " << root2 <<std::endl;
}