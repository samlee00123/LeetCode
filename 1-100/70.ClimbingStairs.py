class Solution:
    def choose(self, n: int, k: int) -> int:
        if 0 <= k <= n:
            ntok = 1
            ktok = 1
            for t in range(1, min(k, n - k) + 1):
                ntok *= n
                ktok *= t
                n -= 1
            return ntok // ktok
        else:
            return 0

    def climbStairs(self, n: int) -> int:
        ways = 0
        x = n // 2
        y = n - 2 * x

        for i in range(x+1):
            ways += self.choose(x+i+y, x-i)

        return ways
