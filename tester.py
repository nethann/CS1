class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                sum_ = mul + result[p2]

                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0')  # Strip leading zeros

# Example usage:
sol = Solution()
print(sol.multiply("2", "3"))  # Output: "56088"
