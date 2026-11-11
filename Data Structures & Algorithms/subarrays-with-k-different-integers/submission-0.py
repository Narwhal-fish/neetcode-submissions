class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(limit):
            l = 0
            count = {}
            ret = 0
            for r in range(len(nums)):
                count[nums[r]] = count.get(nums[r], 0) + 1

                while len(count.keys()) > limit:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]

                    l+=1
                    
                ret += r - l + 1
                
            return ret

        return atMost(k) - atMost(k-1)