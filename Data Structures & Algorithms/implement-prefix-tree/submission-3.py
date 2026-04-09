class PrefixTree:

    def __init__(self):
        self.word_set = set()
        self.prefix_set = set()

    def insert(self, word: str) -> None:
        self.word_set.add(word)
        for idx in range(len(word)):
            self.prefix_set.add(word[:idx + 1])

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_set
        