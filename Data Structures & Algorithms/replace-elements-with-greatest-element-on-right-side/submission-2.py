class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_array = []
        largest = 0

        for i in range(len(arr) - 1, 0, -1):
            largest = max(largest, arr[i])
            new_array.insert(0, largest)
        new_array.append(-1)
        return new_array