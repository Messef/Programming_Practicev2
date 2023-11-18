#include <iostream>

// Define is_palindrome() here:
bool is_palindrome(std::string text) {
  std::string counter_text;

  int n = text.length(); 
  while(n--)
       counter_text+=text[n];
  
  if (counter_text == text) {
    return true;
  }
  return false;
}

int main() {
  
  std::cout << is_palindrome("madam") << "\n";
  std::cout << is_palindrome("ada") << "\n";
  std::cout << is_palindrome("lovelace") << "\n";
  
}