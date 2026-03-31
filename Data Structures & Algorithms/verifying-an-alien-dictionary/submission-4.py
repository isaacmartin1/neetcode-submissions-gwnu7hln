class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i
        for word_idx in range(1, len(words)):
            word = words[word_idx]
            prev_w = words[word_idx - 1]
            for idx in range(len(word)):
                if idx >= len(prev_w):
                    continue
                prev = prev_w[idx]
                curr = word[idx]
                diff = order_dict[curr] - order_dict[prev] 
                if diff < 0:
                    return False
                elif diff > 0:
                    break
                if idx == len(word) - 1 and len(prev_w) > len(word):
                    return False
        return True
