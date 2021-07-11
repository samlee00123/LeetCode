class Solution:
    def pSort(self, dist, k):
        if len(dist) == 0:
            return {}

        if len(dist) == 1:
            return dist

        pivot = dist[next(iter(dist))]
        left = {}
        mid = {}
        right = {}

        for i in dist:
            if dist[i] < pivot:
                left[i] = dist[i]
            elif dist[i] == pivot:
                mid[i] = dist[i]
            else:
                right[i] = dist[i]

        sl = len(left)
        sm = len(mid)
        sr = len(right)

        if k <= sl:
            return self.pSort(left, k)
        elif sl < k and k <= sl + sm:
            return dict(left.items() | mid.items())
        else:
            return dict(left.items() | mid.items() | self.pSort(right, k - sl - sm).items())

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = {}

        for i in points:
            dist[str(i)] = sqrt(i[0]**2 + i[1]**2)

        return [json.loads(point) for point in self.pSort(dist, k)]
