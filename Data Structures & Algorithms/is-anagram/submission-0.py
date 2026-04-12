class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map={}
        for i in range(len(s)):
            char_s=s[i]
            char_t=t[i]

            hash_map[char_s]=hash_map.get(char_s,0)+1
            hash_map[char_t]=hash_map.get(char_t,0)-1
        
        for count in hash_map.values():
            if count!=0:
                return False
        return True
        