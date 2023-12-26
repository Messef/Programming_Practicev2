#include <iostream>
#include <vector>
class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        
        digits[-1]++;
        if (int(log10(digits[-1]) + 1 == 2)) {
            digits.push_back(0);
            digits[-2] = 1; 
        }
        return digits;
    }
};
int main() {
    Solution myObj;
    std::vector<int> digits;
    digits.push_back(3);
    digits.push_back(4);
    digits.push_back(9);

    std::vector<int> ans = myObj.plusOne(digits);
    for (int i: ans) {
        std::cout<<i;
    }
    
    return 0;
}