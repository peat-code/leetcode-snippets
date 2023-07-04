# return ans if not (ans >> 31) & 1 else -((~ret + 1) & 0xffffffff)
# https://leetcode.com/problems/single-number-ii/solutions/43297/java-o-n-easy-to-understand-solution-easily-extended-to-any-times-of-occurance/comments/159988
# If you're working with python, you'll need to modify the return statement.

# I used:
# return ret if not (ret >> 31) & 1 else -((~ret + 1) & 0xffffffff)

# The above line checks to see if the sign bit is set, and takes the two's compliment with a 32 bit mask if it is.
# This is necessary in python because integers are not locked to n bits, they grow dynamically.

# Python does not know if the answer we constructed is in two's compliment or not without us explicitly telling it where the sign bit is.

# example
# leetcode 137
# run through all nums checking 1 bit at a time, sum and mod to find the single occuring number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for j in nums:
                if (1<< i ) & j:
                    sum += 1
            if sum % 3:
                ans = ans + (1<<i)
        return ans if not (ans >> 31) & 1 else -((~ret + 1) & 0xffffffff)
