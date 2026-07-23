class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top = counts.most_common(k)
        res = []
        for pair in top:
            res.append(pair[0])
        return res
