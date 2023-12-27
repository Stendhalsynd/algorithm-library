class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))] # dp: nums[i] 를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: # nums[i]: 현재 위치 , nums[j]: 이전 위치
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)