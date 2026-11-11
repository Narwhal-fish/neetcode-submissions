class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxLen = 0

        for r in range(len(s)):
            print(s[r])
            count[s[r]] = count.get(s[r], 0) + 1
            maxCount = max(count.values())
            while (r - l + 1) - maxCount > k :
                count[s[l]] -= 1
                l += 1
                maxCount = max(count.values())

            maxLen = max(maxLen, r-l+1)

        return maxLen