class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # #time complexity is O(k*n^2)
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for j in range(1, n + 1):
            dp[1][j] = j

        # i starts from two since there are no break and no break scenarios being calculated
        for i in range(2, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = float("inf")
                # check permutations for different floors as well
                for f in range(1, j + 1):
                    break_case = dp[i - 1][f - 1]  # Egg breaks
                    no_break_case = dp[i][j - f]  # Egg doesn't break
                    worst_case = 1 + max(break_case, no_break_case)
                    dp[i][j] = min(dp[i][j], worst_case)

                # check break and no break scenarios and take max of this

        return dp[k][n]
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        attempts = 0

        # While the maximum floors we can check with `k` eggs and `attempts` trials is less than `n`
        while dp[attempts][k] < n:
            attempts += 1
            for j in range(1, k + 1):  # For each egg count (1 to k)
                dp[attempts][j] = 1 + dp[attempts - 1][j - 1] + dp[attempts - 1][j]

        return attempts
