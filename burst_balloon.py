class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * n for _ in range(n)]

        for le in range(1, n - 1):  # size of burstible arr
            for i in range(n - le):  # start indices of burstible arr
                j = i + le  # end index of burstible arr
                for k in range(i + 1, j):  # iterate over balloon in burstible arr
                    # before+balloon itself+after
                    before = 0
                    after = 0
                    # before: dp[i][k-1]
                    # after: dp[k+1][j]
                    # if i==k, before val is 0
                    # if j==k, after val is 0
                    before = dp[i][k - 1] if i != k else 0
                    after = dp[k + 1][j] if k != j else 0

                    prev = nums[i] if i != 0 else 1
                    next = nums[j] if j != n - 1 else 1
                    balloonItself = prev * nums[k] * next

                    dp[i][j] = max(dp[i][j], before + balloonItself + after)

        return dp[0][n - 1]

        nums = [1] + nums + [1]
        n = len(nums)

        # Create a DP table initialized to 0
        dp = [[0] * n for _ in range(n)]

        # Iterate over lengths of subarrays to consider
        for length in range(1, n - 1):
            for i in range(n - length):
                j = i + length  # Define the end index of the subarray
                # Iterate over possible last balloons to pop in the subarray
                for k in range(i + 1, j):
                    # Calculate the maximum coins for popping the balloon k last
                    before = dp[i][k - 1] if i != k else 0
                    after = dp[k + 1][j] if k != j else 0

                    prev = nums[i] if i != 0 else 1
                    next = nums[j] if j != n - 1 else 1
                    balloonItself = prev * nums[k] * next

                    dp[i][j] = max(dp[i][j], before + balloonItself + after)

        # Return the maximum coins that can be collected
        return dp[0][n - 1]
