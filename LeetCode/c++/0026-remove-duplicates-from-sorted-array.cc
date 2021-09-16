class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()) return 0;
        int fast, slow;
        fast = slow = 0;
        
        while(fast != nums.size()){
            if(nums[fast] == nums[slow]) fast++;
            else {
                slow++;
                nums[slow] = nums[fast];
                fast++;
            }
        }
        return slow + 1;
    }
};