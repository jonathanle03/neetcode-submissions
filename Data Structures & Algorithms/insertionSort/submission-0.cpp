// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> result;
        if (pairs.size() == 0) {
            return result;
        }

        vector<Pair> curr = pairs;
        result.push_back(curr);
        for (int i = 1; i < pairs.size(); ++i) {
            Pair p = curr[i];
            int j = i - 1;

            while (j >= 0 && curr[j].key > p.key) {
                curr[j + 1] = curr[j];
                j--;
            }

            curr[j + 1] = p;

            result.push_back(curr);
        }
        return result;
    }
};
