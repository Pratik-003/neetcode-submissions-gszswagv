class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={")":"(","}":"{","]":"["}
        for element in s:
            if stack and(element in hash_map and stack[-1]==hash_map[element]):
                stack.pop()
            else:
                stack.append(element)
        return not stack