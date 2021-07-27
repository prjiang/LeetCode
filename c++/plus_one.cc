class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() - 1, carry = 1;
        for ( ; i >= 0 && carry; --i) {
            carry += digits[i];
            digits[i] = carry %10;
            carry /= 10;
        }
        
        if (carry) digits.insert(begin(digits), carry);
        return digits;
    }
};