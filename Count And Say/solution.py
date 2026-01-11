class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        res = "1"
        while n > 1:
            temp = res
            new_res = ""
            left = 0
            count = 0

            for right in range (0, len(temp)):
                if temp[left] != temp[right]:
                    new_res += str(count) + temp[left]
                    left = right
                    count = 1
                else:
                    count += 1
            
            new_res += str(count) + temp[left]
            res = new_res
            n -= 1
                
        return res
