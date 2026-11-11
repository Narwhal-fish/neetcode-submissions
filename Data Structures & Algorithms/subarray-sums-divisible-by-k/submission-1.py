class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        acc = 0
        ret = 0
        count = {0:1}


        for n in nums:
            acc += n

            if acc%k in count:
                ret += count[acc%k]

            count[acc%k] = count.get(acc%k, 0 )+1

        return ret

