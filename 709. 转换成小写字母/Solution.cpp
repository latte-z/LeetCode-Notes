//
// Created by Ryan Shen on 2018-12-07.
//

class Solution {
public:
    string toLowerCase(string str) {
        transform(str.begin(), str.end(), str.begin(), ::tolower);
        return str;
    }
};