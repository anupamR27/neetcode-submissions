class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]* len(temperatures)

        for i in range(len(temperatures) - 1):
            count = 0
            for j in range (i+1 , len(temperatures)):
                count += 1
                if temperatures[j]>temperatures[i]:
                    result[i] = (count)
                    break
                else:
                    continue

                
        return result