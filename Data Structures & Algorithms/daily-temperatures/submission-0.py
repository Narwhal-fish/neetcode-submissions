class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = []
        temp = []

        ret = [0 for _ in range(len(temperatures))]

        

        for i in range(len(temperatures)):

            while temp and temp[-1] < temperatures[i]:
                temp.pop()
                tmp = index.pop()
                ret[tmp] = i-tmp

            temp.append(temperatures[i])
            index.append(i)


        return ret
