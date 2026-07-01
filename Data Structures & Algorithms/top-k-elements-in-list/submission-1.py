class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, item in counts.items():
            buckets[item].append(key)

        result = []
        for bucket in buckets[::-1]:
            if k == 0:
                break
            
            if not bucket:
                continue
            if len(bucket) <= k:
                result.extend(bucket)
                k -= len(bucket)
            else:
                result.extend(bucket[:k])
                k = 0

        return result