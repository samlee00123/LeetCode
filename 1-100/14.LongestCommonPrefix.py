class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = ""
        i = 0
        while True:
            try:
                char = strs[0][i]
                for s in strs:
                    if s[i] == char:
                        continue
                    else:
                        return prefix
                prefix += char
                i += 1
            except IndexError:
                return prefix
