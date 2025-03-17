class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        counter = 0
        for char in s:
            if char == "(":
                if counter > 0:
                    result.append(char)
                counter += 1

            else:
                counter -= 1
                if counter > 0:
                    result.append(char)
        return "".join(result) # Convert List into String