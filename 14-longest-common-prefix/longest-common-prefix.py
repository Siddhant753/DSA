class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for char in range(len(strs[0])):
            for words in strs:
                if char == len(words) or words[char] != strs[0][char]:
                    return result
            result += strs[0][char]
        return result