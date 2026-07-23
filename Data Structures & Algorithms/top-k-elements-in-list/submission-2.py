class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        pairs = counts.most_common(k)
        return [pair[0] for pair in pairs]
