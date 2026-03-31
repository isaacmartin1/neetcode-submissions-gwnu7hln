class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i
        
        for word_idx, word in enumerate(words):
            if word_idx == 0:
                continue
            prev_w = words[word_idx - 1]
            print(word)
            for idx in range(len(word)):
                if idx >= len(prev_w):
                    continue
                prev = prev_w[idx]
                curr = word[idx]
                diff = order_dict[curr] - order_dict[prev]
                
                print(order_dict[curr], order_dict[prev], diff)
                if diff < 0:
                    return False
                elif diff > 0:
                    break

                if idx == len(word) - 1 and len(prev_w) > len(word):
                    return False

        print(order_dict)
        return True
