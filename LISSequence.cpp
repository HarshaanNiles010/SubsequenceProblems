#include <iostream>
#include <vector>
#include <set>
#include <iterator>
#include <algorithm>

class longestIncreasingSS{
private:
    std::vector<int> vector;
public:
    longestIncreasingSS(){
        std::fill(vector.begin(),vector.end(),0);
    }
    longestIncreasingSS(std::vector<int> inputVector){
        vector = inputVector;
    }
    int lisLength(std::vector<int> inputVector){
        int len = inputVector.size();
        std::vector<int> b;
        std::set<int> s;
        std::set<int>::iterator it;
        for(int i = 0; i < len; i++){
            s.insert(inputVector[i]);
        }
        for(it = s.begin(); it != s.end(); it++){
            b.push_back(*it);
        }
        int m = b.size();
        int dp[m + 1][len + 1];

        for(int i = 0; i < m + 1; i++){
            for(int j = 0; j < len + 1; j++){
                dp[i][j] = -1;
            }
        }
        for(int i = 0; i < m + 1; i++){
            for(int j = 0; j < len + 1; j++){
                if(i == 0 || j == 0){
                    dp[i][j] = 0;
                }
                else if(inputVector[j - 1] == b[i - 1]){
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                }
                else{
                    dp[i][j] = std::max(dp[i - 1][j],dp[i][j - 1]);
                }
            }
        }
        return dp[m][len];
    }
    void LISprint(std::vector<int> inputVector){
        std::vector<std::vector<int>> L(inputVector.size());
        L[0].push_back(inputVector[0]);
        for(int i = 1; i < inputVector.size(); i++){
            for(int j = 0; j < i; j++){
                if((inputVector[i] > inputVector[j]) && (L[i].size() < L[j].size() + 1)) {
                    L[i] = L[j];
                }
            }
            L[i].push_back(inputVector[i]);
        }
        std::vector<int> maxx = L[0];
        for(std::vector<int> x: L){
            if(x.size() > maxx.size()){
                maxx = x;
            }
        }
        for(int x:maxx){
            std::cout << x << " ";
        }
        std::cout << "\n";
    }
};

int main(){
    longestIncreasingSS l1;
    std::vector<int> inputVector = {10,22,9,33,21,50,41,60};
    std::cout << "Length of LIS: " << l1.lisLength(inputVector) << "\n";
    l1.LISprint(inputVector);
    return 0;
}