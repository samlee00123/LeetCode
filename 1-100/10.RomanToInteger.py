class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0

        while s:
            try:
                if s[1]:
                    if s[0] + s[1] == "IV":
                        ans += 4
                        s = s[2:]
                    elif s[0] + s[1] == "IX":
                        ans += 9
                        s = s[2:]
                    elif s[0] + s[1] == "XL":
                        ans += 40
                        s = s[2:]
                    elif s[0] + s[1] == "XC":
                        ans += 90
                        s = s[2:]
                    elif s[0] + s[1] == "CD":
                        ans += 400
                        s = s[2:]
                    elif s[0] + s[1] == "CM":
                        ans += 900
                        s = s[2:]
                    else:
                        ans += d.get(s[0])
                        s = s[1:]
            except IndexError:
                ans += d.get(s[0])
                s = s[1:]
        return ans
