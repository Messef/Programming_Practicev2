#include <iostream>
#include <cmath>

double average(double num1, double num2) {
  return (num1 + num2) / 2;
}

int tenth_power(int num) { //Raises num to 10th power
  return pow(num, 10);
}

bool is_palindrome(std::string text) { //checks if palindrome
  std::string reversed_text = "";
  
  for (int i = text.size() - 1; i >= 0; i--) {
    reversed_text += text[i]; //Creates a reversed string
  }
  
  if (reversed_text == text) {
    return true;
  }
  
  return false;
}