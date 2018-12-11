//
// Created by Ryan Shen on 2018-12-07.
//

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int pre = 0;
        int post = A.size() - 1;
        while(pre < post) {
            if (A[pre]%2==0)
                pre++;
            else if (A[post]%2==1)
                post--;
            else {
                int temp = A[pre];
                A[pre++] = A[post];
                A[post--] = temp;
            }
        }
        return A;
    }
};