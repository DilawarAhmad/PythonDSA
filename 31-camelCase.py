class Solution:
    # Function to convert the given string to Camel Case
    def convertToCamelCase(self, s):
        words = s.strip().split()
        if not words:
            return ""
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
sol = Solution()
print(sol.convertToCamelCase(s = "i got intern at geeksforgeeks"))