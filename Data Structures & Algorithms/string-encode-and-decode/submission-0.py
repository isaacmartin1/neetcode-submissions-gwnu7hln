class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        print('encode', strs)
        for segment in strs:
            encoded_string += segment + ";"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        print('decode', s)
        strs = []
        current_string = ""
        for idx in range(len(s)):
            if s[idx] != ";":
                current_string += s[idx]
            elif s[idx] == ';':
                strs.append(current_string)
                current_string = ""
        return strs