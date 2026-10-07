class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "".join(f"{len(s)}#{s}" for s in strs)
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return result
