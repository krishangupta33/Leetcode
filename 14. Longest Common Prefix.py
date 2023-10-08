class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        common_count = 0

        for i in range(min_len):
            char_to_match = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char_to_match:
                    return strs[0][:common_count]

            common_count += 1

        return strs[0][:common_count] if common_count > 0 else ""
