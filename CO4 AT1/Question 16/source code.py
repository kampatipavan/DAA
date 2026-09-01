# Matrix Chain Multiplication using Dynamic Programming

# Number of dimensions
n = 4

# Matrix dimensions
arr = [10, 20, 30, 40]

# dp[i][j] = minimum cost of multiplying matrices i to j
dp = [[0 for _ in range(n)] for _ in range(n)]

# Chain length starts from 2
for length in range(2, n):

    for i in range(1, n - length + 1):

        j = i + length - 1

        # Set initial cost to infinity
        dp[i][j] = float('inf')

        # Try every possible split
        for k in range(i, j):

            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + arr[i - 1] * arr[k] * arr[j]
            )

            if cost < dp[i][j]:
                dp[i][j] = cost

# Display result
print("Minimum Cost =", dp[1][n - 1])
