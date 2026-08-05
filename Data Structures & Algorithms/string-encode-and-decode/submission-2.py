class Solution:

    def encode(self, strs: List[str]) -> str:
        
        final = ""
        for string in strs:
            final += "¥"
            for c in string:
                final += c
        return final


    def decode(self, s: str) -> List[str]:
        result = []
        curr = ""
        for c in s:
            if c == "¥":
                if curr != "¥" or result:
                    result.append(curr)
                curr = ""
            else:
                curr += c
        result.append(curr)


        
        return result[1:]