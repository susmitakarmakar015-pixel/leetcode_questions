class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int count = 0;

        while (true) {
            bool sorted = true;

            for (int i = 0; i < nums.size() - 1; i++) {
                if (nums[i] > nums[i + 1]) {
                    sorted = false;
                    break;
                }
            }

            if (sorted)
                return count;

            int index = 0;
            int minSum = nums[0] + nums[1];

            for (int i = 1; i < nums.size() - 1; i++) {
                int sum = nums[i] + nums[i + 1];

                if (sum < minSum) {
                    minSum = sum;
                    index = i;
                }
            }

            nums[index] = nums[index] + nums[index + 1];
            nums.erase(nums.begin() + index + 1);

            count++;
        }
    }
};