class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = defaultdict(list)
        for s in strs:
            frequency = [0] * 26        

            for c in list(s):
                frequency[ord(c) - ord('a')] += 1
            
            answer_dict[tuple(frequency)].append(s)

        return list(answer_dict.values())
