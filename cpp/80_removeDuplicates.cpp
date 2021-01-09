class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        int index = 0;
        for (int i=0; i<nums.size(); ++i) {
            nums[index] = nums[i];
            if (i+1 < nums.size() && nums[i+1] == nums[i]) {
                nums[++index] = nums[++i];
                while (i+1 < nums.size() && nums[i+1] == nums[index]) ++i;
            }
            index++;
        }
        return index;
    }
};

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();

        int index = 2;
        for (int i = 2; i<nums.size(); ++i) {
            if (nums[i] != nums[index-2]) nums[index++] = nums[i];
        }
        return index;
    }
};
