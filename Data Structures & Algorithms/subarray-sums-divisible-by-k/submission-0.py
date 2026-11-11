class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        acc = 0
        ret = 0
        count = {0:1}


        for n in nums:
            acc += n
        
            for key in count.keys():
                if (acc - key)%k == 0:
                    print(acc, key)
                    ret += count[key]

            count[acc] = count.get(acc, 0) + 1

        return ret

