class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        l = []

        for i in range(20):
            for j in range(20):
                k = x**i + y**j
                if k <= bound and k not in l:
                    l.append(k)
        return sorted(l)
