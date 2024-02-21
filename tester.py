
import math
class Solution(object):
    def isHappy(self, n):
        self.n = int(n)
        """
        :type n: int
        :rtype: bool
        """

        if self.n > 0: 
            digits = [int(digit) for digit in str(self.n)]        

            for i in digits: 
                print(i)

                
d1 = Solution()
print(d1.isHappy(19))