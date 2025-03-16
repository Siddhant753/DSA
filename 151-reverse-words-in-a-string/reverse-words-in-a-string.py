class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        word = ""
        result = "" 

        while left <= right:
            char = s[left]
            if char != " ":
                word += char
            else:
                if word:
                    if result:
                        result = word + " " + result # Then the new word will be added to left side
                    else:
                        result = word # Word is added to result for 1st word
                    word = "" # This resets the word to null
            left += 1

        if word:
            if result:
                result = word + " " + result
            else:
                result = word
        
        return result