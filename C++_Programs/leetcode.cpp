#include <map>
#include <iostream>
#include <vector>
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::map<int, int> numMap;
        int n = nums.size();

        // Build the hash table
        for (int i = 0; i < n; i++) {
            numMap[nums[i]] = i;
        }

        std::vector<int> returner;
        // Find the complement
        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.count(complement) && numMap[complement] != i) {
                returner.push_back(numMap[complement]);
                returner.push_back(i);
                return returner;
            }
        }

        return returner; // No solution found
    }
};
int main() {
    std::vector<int> solution;
    for (int i = 0; i < 10; i++) {
        solution.push_back(i);
    }
    int target = 17;
    Solution myObj;
    std::vector<int> result = myObj.twoSum(solution, target);
    
    // Print the result
    for (int num : result) {
        std::cout << num << std::endl;
    }
    
    return 0;
}