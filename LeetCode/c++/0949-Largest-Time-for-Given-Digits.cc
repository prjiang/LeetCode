/*
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.

Input: arr = [0,0,0,0]
Output: "00:00"

Input: arr = [0,0,1,0]
Output: "10:00"

Constraints:
    arr.length == 4
    0 <= arr[i] <= 9
*/

class Solution {
public:
    string largestTimeFromDigits(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        string ret;
        do {
            string hour = {char(arr[0] + '0'), char(arr[1] + '0')}, minute = {char(arr[2] + '0'), char(arr[3] + '0')};
            if(hour < "24" && minute < "60") {
                ret = hour + ":" + minute;
            }
        }
        while(next_permutation(arr.begin(), arr.end()));
        return ret;
    }
};