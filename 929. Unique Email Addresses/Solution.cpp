//
// Created by Ryan Shen on 2018-12-06.
//

class Solution {
public:
    int numUniqueEmails(vector <string> &emails) {
        vector <string> filter_emails;
        for (const auto &i : emails) {
            string splice_emails;
            for (int j = 0; j < i.size(); ++j) {
                auto atPos = i.find('@');
                switch (i[j]) {
                    case '.': {
                        if (j > atPos) {
                            splice_emails += i[j];
                            break;
                        } else
                            break;
                    }
                    case '+': {
                        j = static_cast<int>(atPos);
                        splice_emails += i[j];
                        break;
                    }
                    default:
                        splice_emails += i[j];
                        break;
                }
            }
            filter_emails.push_back(splice_emails);
        }
        sort(filter_emails.begin(), filter_emails.end());
        auto iterator = unique(filter_emails.begin(), filter_emails.end());
        filter_emails.erase(iterator, filter_emails.end());
        return static_cast<int>(filter_emails.size());
    }
};