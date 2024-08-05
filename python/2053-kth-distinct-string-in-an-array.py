class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        count = 0

        for char in arr:
            freq[char] = 1 + freq.get(char, 0)
        
        for char in arr:
            if freq[char] == 1:
                count += 1
                if count == k:
                    return char
        return ""