class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            s = ''.join(list(str(x))[::-1])
            if int(s) > 2**31 - 1:
                return 0
            else:
                return int(s)
        else:
            x *= -1
            s = ''.join(list(str(x))[::-1])
            if int(s) * -1 < -2**31:
                return 0
            else:
                return int(s) * -1
