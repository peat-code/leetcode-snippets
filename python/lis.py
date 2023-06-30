nums = [-1,3,4,5,2,2,2,2]

dp = [1] * len(nums)

for j in range(8):
    for i in range(j):
        if nums[j] >=nums[i]:
            dp[j] = max(dp[i] + 1,dp[j])

print(dp)
print (max(nums))
