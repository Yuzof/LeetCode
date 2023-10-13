#include <iostream>
#include <vector>

class Solution {
public:
    int minCostClimbingStairs(std::vector<int>& cost) {
        const int n = cost.size();
        std::vector<int> dp(n + 1, 0);
        int i = 2;
        while (i <= n){
          dp[i] = std::min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
          i++;
        }
        return dp[n];
    }
};

int main(){
  Solution A;
  std::vector<int> task{1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
  std::cout << A.minCostClimbingStairs(task) << '\n';
  return 0;
}