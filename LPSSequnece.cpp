
#include <iostream>
#include <vector>
#include <algorithm>

class longestPalindromeSS{
private:
    std::vector<int> vector;
public:
    longestPalindromeSS(){
        std::fill(vector.begin(),vector.end(),0);
    }
    longestPalindromeSS(std::vector<int> newVector){
        vector = newVector;
    }
    int lpsLength(std::vector<int> vector1){
        std::vector<int> temp = vector1;
        std::reverse(vector1.begin(),vector1.end());
        int len = vector1.size();
        int L[len + 1][len + 1];

        for(int i = 0; i <= len; i++){
            for(int j = 0; j <= len; j++){
                if(i == 0 || j == 0){
                    L[i][j] = 0;
                }
                else if(vector1[i - 1] == temp[j - 1]){
                    L[i][j] = L[i - 1][j - 1] + 1;
                }
                else{
                    L[i][j] = std::max(L[i - 1][j],L[i][j - 1]);
                }
            }
        }
        return L[len][len];
    }
    void lpsPrint(std::vector<int> vector1){
        std::vector<int> temp = vector1;
        std::reverse(vector1.begin(),vector1.end());
        int len = vector1.size();
        int L[len + 1][len + 1];

        for(int i = 0; i <= len; i++){
            for(int j = 0; j <= len; j++){
                if(i == 0 || j == 0){
                    L[i][j] = 0;
                }
                else if(vector1[i - 1] == temp[j - 1]){
                    L[i][j] = L[i - 1][j - 1] + 1;
                }
                else{
                    L[i][j] = std::max(L[i - 1][j],L[i][j - 1]);
                }
            }
        }
        int idx = L[len][len];
        int seq[idx];
        int seqLen = (int)sizeof(seq)/sizeof(seq[0]);
        for(int i = 0; i <= idx; i++){
            seq[i] = 0;
        }
        int i = len;
        int j = len;
        while(i > 0 && j > 0){
            if(vector1[i - 1] == temp[j - 1]){
                seq[idx - 1] = vector1[i - 1];
                i--;
                j--;
                idx--;
            }
            else if(L[i - 1][j] > L[i][j - 1]){
                i--;
            }
            else{
                j--;
            }
        }
        std::cout << "The LPS is: \n";
        for(int k = 0; k < seqLen; k++){
            std::cout << seq[k] << " ";
        }
        std::cout << std::endl;
    }
};

int main(){
    longestPalindromeSS l1;
    std::vector<int> vector1 = {1,2,3,4,5,4,3,2,1,6};
    l1.lpsPrint(vector1);
    return 0;
}