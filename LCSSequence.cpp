#include <iostream>
#include <vector>
#include <math.h>
class longestCommonSS{
private:
    std::vector<int> List1;
    std::vector<int> List2;
public:
    longestCommonSS(){
        std::fill(List1.begin(),List1.end(),0);
        std::fill(List2.begin(),List2.end(),0);
    }
    longestCommonSS(std::vector<int>& inputList1,std::vector<int>& inputList2){
        List1 = inputList1;
        List2 = inputList2;
    }
    int lcsLength(std::vector<int>& inputList1, std::vector<int>& inputList2){
        int length1 = inputList1.size();
        int length2 = inputList2.size();
        int L[length1 + 1][length2 + 1];
        for(int i = 0; i <= length1; i++){
            for(int j = 0; j <= length2; j++){
                if(i==0 || j==0){
                    L[i][j] = 0;
                }
                else if(inputList1[i - 1] == inputList2[j - 1]){
                    L[i][j] = L[i - 1][j - 1] + 1;
                }
                else{
                    L[i][j] = std::max(L[i - 1][j],L[i][j - 1]);
                }
            }
        }
        return L[length1][length2];
    }
    void printLCS()
};

int main(){
    longestCommonSS l1;
    std::vector<int> List1 = {1,2,3,4,5,6,7,8,9};
    std::vector<int> List2 = {5,6,7,8};
    std::cout << "The Longest Common Subsequence has the length: " << l1.lcsLength(List1,List2) <<"\n";
    return 0;
}