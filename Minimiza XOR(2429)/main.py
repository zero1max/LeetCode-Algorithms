class Solution(object):
    def minimizeXor(self, num1, num2):
        num2_bits = bin(num2).count('1')
        
        result = 0
        for i in range(31, -1, -1):  
            if num2_bits > 0 and (num1 & (1 << i)) != 0: 
                result |= (1 << i)
                num2_bits -= 1

        for i in range(32):
            if num2_bits > 0 and (result & (1 << i)) == 0:
                result |= (1 << i)
                num2_bits -= 1

        return result
