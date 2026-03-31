class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        bucket_array = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            frequency_dict[n] = 1 + frequency_dict.get(n, 0)
        for n, c in frequency_dict.items():
            bucket_array[c].append(n)
        
        final = []
        for idx in range(len(nums), 0, -1):
            for n in bucket_array[idx]:
                final.append(n)
                if len(final) == k:
                    return final

        return final
