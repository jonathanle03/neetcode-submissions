class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        count = 0
        counting = True
        count_str = ""
        result = []
        string = ""
        i = 0

        while i < len(s):
            if counting:
                if s[i] == "#":
                    counting = False
                    count = int(count_str)
                    count_str = ""
                    if count == 0:
                        counting = True
                        result.append("")
                else:
                    count_str += s[i]
            else:
                string += s[i]
                count -= 1
                if count == 0:
                    counting = True
                    result.append(string)
                    string = ""

            i += 1
        
        return result
